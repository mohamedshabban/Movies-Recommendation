from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import Http404, JsonResponse
from .models import Movie, Myrating
from django.contrib import messages
from .forms import UserForm
from django.db.models import Case, When
from .recommendation import Myrecommend
import numpy as np
import pandas as pd
from django.core.paginator import Paginator


# for recommendation
def recommend(request):
    try:
        if not request.user.is_authenticated:
            return redirect("login")
        if not request.user.is_active:
            raise Http404
        df = pd.DataFrame(list(Myrating.objects.all().values()))
        nu = df.user_id.unique().shape[0]
        current_user_id = request.user.id
        # if new user not rated any movie
        if current_user_id > nu:
            movie = Movie.objects.get(id=15)
            q = Myrating(user=request.user, movie=movie, rating=0)
            q.save()

        print("Current user id: ", current_user_id)
        prediction_matrix, Ymean = Myrecommend()
        my_predictions = prediction_matrix[:, current_user_id - 1] + Ymean.flatten()
        pred_idxs_sorted = np.argsort(my_predictions)
        pred_idxs_sorted[:] = pred_idxs_sorted[::-1]
        pred_idxs_sorted = pred_idxs_sorted + 1
        print(pred_idxs_sorted)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pred_idxs_sorted)])
        movie_list = list(Movie.objects.filter(id__in=pred_idxs_sorted, ).order_by(preserved)[:10])
        return render(request, 'web/recommend.html', {'movie_list': movie_list})
    except:

        return render(request, 'web/list.html')

# List view
def index(request):
    movies = Movie.objects.all()  # .delete()
    # 15 =number of movies to display
    paginator = Paginator(movies, 15)
    paginator2 = Paginator(movies, 15)

    query = request.GET.get('q')
    query2 = request.GET.get('s')

    movies = paginator.get_page(query)
    movies2 = paginator2.get_page(query2)
    if query:
        #movies = Movie.objects.filter(Q(title__icontains=query)).distinct()
        return render(request, 'web/list.html', {'movies': movies})
    elif query2:
        movies2 = Movie.objects.filter(Q(title__icontains=query2)).distinct()
        return render(request, 'web/list.html', {'movies': movies2})
    return render(request, 'web/list.html', {'movies': movies})




# detail view
def detail(request, movie_id):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404
    movies = get_object_or_404(Movie, id=movie_id)
    # for rating
    if request.method == "POST":
        rate = request.POST['rating']
        ratingObject = Myrating()
        ratingObject.user = request.user
        ratingObject.movie = movies
        ratingObject.rating = rate
        ratingObject.save()
        messages.success(request, "Your Rating is submited ")
        return redirect("index")
    return render(request, 'web/detail.html', {'movies': movies})


# Register user
def signUp(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("index")
    context = {
        'form': form
    }
    return render(request, 'web/signUp.html', context)


# Login User
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("index")
            else:
                return render(request, 'web/login.html', {'error_message': 'Your account disable'})
        else:
            return render(request, 'web/login.html', {'error_message': 'Invalid Login'})
    return render(request, 'web/login.html')


# Logout user
def Logout(request):
    logout(request)
    return redirect("login")

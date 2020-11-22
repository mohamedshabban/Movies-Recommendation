from django.contrib import admin
from .models import Movie,Myrating
from import_export.admin import ImportExportModelAdmin
@admin.register(Movie)
class MovieImportExport(ImportExportModelAdmin):
    pass

# admin.site.register(Movie)
@admin.register(Myrating)
class MyratingImportExport(ImportExportModelAdmin):
    pass
# admin.site.register(Myrating)
# Register your models here.

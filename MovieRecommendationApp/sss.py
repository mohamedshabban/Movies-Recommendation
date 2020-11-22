import pandas as pd
import os

# list1 = []
# list2 = []
#
# df = pd.read_csv('file.csv')
# for i in range(len(df.iloc[:, 3])):
#     string = ''
#     if (len(df.iloc[i, 2]) != 0):
#         for j in range(len(df.iloc[i, 2])):
#             if df.iloc[i, 2][j] == '[' or df.iloc[i, 2][j] == ']':
#                 continue
#             elif df.iloc[i, 2] == "'":
#                 continue
#             elif df.iloc[i, 2][j] == ',':
#                 string = string + '|'
#                 continue
#             else:
#                 string += df.iloc[i, 2][j]
#     list1.append(string)
# df['genre']=list1
# df.to_csv('file1.csv',index=False)

# for i in os.listdir(r'E:\4th,2nd\poster_downloads'):
#     list1.append(i)
# for i in os.listdir(r'E:\4th,2nd\poster_downloads'):
#     list1.append(i)
# df['movie_logo']=list1[:9219]
# df.to_csv('file.csv',index=False)

# df1 = pd.read_csv('file.csv')
# df=pd.read_csv('tmdbId.csv')
# df3=pd.merge(df,df1,how='inner',left_on=['tmdbId'],right_on=['id'])
# print(df3.loc[:,'title'])

# list1 = []
# for i in df.iloc[:,3] :
#     name=i.split('.jpg')
#     tmdbId=name[0].split('_')
#     list1.append(tmdbId[1])

# print(df.columns)
# exit()
# d={'tmdbId':list1}
# df1=pd.read_csv(r'C:\Users\Mohamed Shaban\Downloads\movies-master\data\movies_metadata.csv')
# df1=df1[['original_title','id']]
# print(df1.head())
# dataframe=pd.DataFrame(data=d)
# dataframe.to_csv('tmdbId.csv',index=False)

# df3=pd.merge(df,df1,how='inner',left_on=['tmdbId'],right_on=['id'])

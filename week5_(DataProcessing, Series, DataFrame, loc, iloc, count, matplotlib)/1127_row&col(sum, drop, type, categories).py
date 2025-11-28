import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
import random

# np.random.seed(1)
# df = pd.DataFrame(np.random.randint(10, size = (4, 8)))
# print(f"{df} \n")

# df['total'] = df[0:7].sum(axis=1)
# print(df)

# df['mean'] = df[0:7].mean(axis=0)
# print(df)

# print(df.mean(axis = 1))

# print(df.min(axis = 0), df.min(axis=1))
# print(f"==============================")
# print(df.max(axis = 0), df.max(axis=1))
# df.loc['max_data'] = df[0:7].max(axis=0)
# print(df)
# print(df.drop('total', axis =1, inplace=True))
# print(df)
# print(df.drop('max_data', axis=0, inplace=True))
# print(df)
# print(df)
# df.iloc[0, 0] = np.nan
# print(df)
# print(df.fillna(0).astype(float))

# df3 = pd.DataFrame({
# 'a':[1,3,4,3,4],
# 'b':[2,3,1,4,5],
# 'c':[1,5,2,4,4]
# })
# print(df3)

# print(np.sum(df3['a']))
# print(np.sum(df3['b']))
# print(np.sum(df3['c']))

# for i in ['a', 'b' ,'c']:
    # print(np.sum(df3[i]))
# print(df3. apply(np.sum, axis=1))
# def diff(x):
#     return x.max() - x.min()
# print(df3.apply(diff, axis=0))

# print(df3.apply(lambda x: x.max() - x.min(), axis = 0))

# print(np.square([1, 2, 3]))
# print(df3.apply(np.square, axis=0))
# ages=[0,0.5,4,6,4,5,2,10,21,23,37,15,38,31,61,20,41,31,100]
# data = ages
# bins = [0,4,18,25,35,60,100]
# labels = ['영유아', '미성년자', '청년', '중년', '장년', '노년']
# cats = pd.cut(data, bins, labels=labels)
# # print(cats)
# # print(type(cats))
# cat_list = list(cats)
# print(cat_list)

# test = pd.DataFrame({'나이': ages, '연령대': cat_list})
# print(test['연령대'].value_counts())

# print(cats.categories)
# print(cats.codes)

# df3 = pd.DataFrame({
# 'a':[1,3,4,3,4],
# 'b':[2,3,1,4,5],
# 'c':[1,5,2,4,4]
# })

# print(f"{df3}\n")

# df3.rename(index={0:'1반', 1:'2반'}, inplace=True)
# print(f"{df3}\n")
# df3.rename(columns={'b':'학생'}, inplace=True)
# print(f"{df3}\n")

# df1 =pd.DataFrame({
# '고객번호' : [1001,1002,1003,1004,1005,1006,1007],
# '이름' : ['둘리','도우너','또치','길동','희동','마이콜','영희']
# },
# columns=['고객번호','이름'])
# print(f"{df1}\n")

# df2 = pd.DataFrame({
# '고객번호':[1001,1001,1005,1006,1008,1001],
# '금액' : [10000,20000,15000,5000,100000,30000]
# },columns=['고객번호','금액'])
# print(f"{df2}\n")

# print(pd.merge(df1, df2, how='right'))

# df1 = pd.DataFrame({
# '품종':['setosa','setosa','virginica','virginica'],
# '꽃잎길이':[1.4,1.3,1.5,1.3]
# }, columns=['품종','꽃잎길이'])
# print(df1)

# df2 = pd.DataFrame({
# '품종': ['setosa','virginica','virginica','ersicolor'],
# '꽃잎너비':[0.4,0.3,0.5,0.3]
# },columns=['품종','꽃잎너비'])
# print(df2)

# print(pd.merge(df1, df2, how='outer'))


# df1 = pd.DataFrame({
# '고객명':['춘향','춘향','몽룡'],
# '날짜' : ['2018-01-01','2018-01-02','2018-01-01'],
# '데이터':[20000,30000,100000]
# })
# print(df1)

# df2 = pd.DataFrame({
# '고객명':['춘향','몽룡'],
# '데이터':['여자','남자']
# })
# print(df2)
# print(pd.merge(df1, df2, how='inner', on='고객명'))

# df1=pd.DataFrame({
# '이름' :['영희','철수','철수'],
# '성적' :[90,80,80]
# })
# df2 = pd.DataFrame({
# '성명' :['영희','영희','철수'],
# '성적2':[100,80,90]
# })
# print(df1)
# print(df2)

# df1 = pd.DataFrame({
# '도시': ['서울','서울','서울','부산','부산'],
# '연도': [2000,2005,2010,2000,2005],
# '인구':[9853972,9762546,9631482,3655437,3512547]
# })
# df2=pd.DataFrame(
# np.arange(12).reshape((6,2)),
# index=[['부산','부산','서울','서울','서울','서울'],
# [2000,2005,2000,2005,2010,2015]],
# columns=['데이터1','데이터2']
# )

# print(f"df1: \n{df1} \n")

# print(f"df2: \n{df2} \n")

# print(pd.merge(df1, df2, left_on=['도시', '연도'], right_index= True, how='outer'))

# df1 = pd.DataFrame(
# [[1.,2.],[3.,4.],[5.,6.]],
# index=['a','c','e'],
# columns=['서울','부산'])

# df2=pd.DataFrame(
# [[7.,8.],[9.,10.],[11.,12.],[13.,14.]],
# index=['b','c','d','e'],
# columns=['대구','광주'])

# print(pd.merge(df1, df2, left_index=True, right_index=True ,how='outer'))

# s1=pd.Series([0,1],index=['A','B'])
# s2=pd.Series([2,3,4],index=['A','B','C'])
# print(s1)
# print(s2)
# print(pd.concadf1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
# df1 = pd.DataFrame({
#     'A': ['A0', 'A1', 'A2', 'A3'],
#     'B': ['B0', 'B1', 'B2', 'B3'],
#     'C': ['C0', 'C1', 'C2', 'C3'],
#     'D': ['D0', 'D1', 'D2', 'D3']
# },
# index=[0, 1, 2, 3])

# df2 = pd.DataFrame({
#     'A': ['A4', 'A5', 'A6', 'A7'],
#     'B': ['B4', 'B5', 'B6', 'B7'],
#     'E': ['C4', 'C5', 'C6', 'C7'],
#     'F': ['D4', 'D5', 'D6', 'D7']
# },
# index=[0, 1, 2, 3])

# df3 = pd.DataFrame({
#     'A': ['A8', 'A9', 'A10', 'A11'],
#     'B': ['B8', 'B9', 'B10', 'B11'],
#     'C': ['C8', 'C9', 'C10', 'C11'],
#     'O': ['D8', 'D9', 'D10', 'D11']
# },
# index=[1,2,3,4])
# print(f"df1: \n{df1}\n")
# print(f"df2: \n{df2}\n")
# print(f"df3: \n{df3}\n")

# result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
# print(f"{result}\n")
# print(result.loc['y'].loc[1])
# print(result.loc['y'].loc[1:2])

df1=pd.DataFrame(
np.arange(6).reshape(3,2),
index=['a','b','c'],
columns=['데이터1','데이터2']
)

df2=pd.DataFrame(
5+np.arange(4).reshape(2,2),
index=['a','c'],
columns=['데이터2','데이터4']
)
print(f"{df1}\n")
print(f"{df2}\n")
print(pd.concat([df1, df2], axis=0))
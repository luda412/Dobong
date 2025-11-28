import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# data = {
#     "2015": [9904312, 3448737, 2890451, 2466052],
#     "2010": [9631482, 3393191, 2632035, 2000002],
#     "2005": [9762546, 3512547, 2517680, 2456016],
#     "2000": [9853972, 3655437, 2466338, 2473990],
#     "지역": ["수도권", "경상권", "수도권", "경상권"],
#     "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
# }
# columns =['지역','2000','2005','2010','2015', '2010-2015 증가율']
# index = ['서울','부산','인천','대구']
# df = pd.DataFrame(data, index=index, columns=columns)
# print(df)

# df1 = df.drop(index=['인천'], axis=0)
# print(df1)

# df2 = df.drop(index=['대구'], inplace = True)
# print(df)

# df3 = df.copy()
# df3.loc['부산', '2010'] = np.nan
# print(df3)

df = pd.DataFrame(np.arange(10,22).reshape(3,4),
index=['a','b','c'],
columns = ["A","B","C","D"])
# print(f"{df}\n")

# df_loc1 = df.loc['a':'c', 'A':'C']
# print(f"df_loc1:\n{df_loc1}")

# df_loc2 = df.loc[['a','c'], ['A','C']]
# print(f"df_loc2:\n{df_loc2}")


# df_iloc1 = df.iloc[0:2, 0:2]
# print(f"df_iloc1:\n{df_iloc1}")

# df_iloc2 = df.iloc[[0,2], [0,2]]
# print(f"df_iloc2:\n{df_iloc2}")

# print(df.loc['a'])
# print(df.loc["A": "C"])

titanic = pd.read_csv("week5/titanic.csv")
titanic = pd.DataFrame(titanic)
# print(titanic.dtypes)
# print(titanic['alive'].value_counts())
# print(titanic['alive'].value_counts(normalize=True) * 100)
# print(titanic['sex'].value_counts())
# print(titanic['sex'].value_counts(normalize=True) * 100)
# print(titanic[['sex', 'alive']].value_counts())

np.random.seed(1) #항상 같은 값이 나오게 설정
s2=pd.Series(np.random.randint(6,size=100))
# print(len(s2))
# print(s2.value_counts())
# print(s2.value_counts().sort_index())
# print(s2.value_counts().sort_index(ascending=False))
# print(s2.value_counts().sort_values(ascending=False))

# data = [
#     [2, 0, 1, 3.0],
#     [0, 0, 0, 3.0],
#     [2, 3, 1, np.nan],
#     [2, 0, 4, 4.0]
# ]

# df = pd.DataFrame(data, columns=[0, 1, 2, 3])
# print(df)
# print(df.sort_values(by=0, ascending=False))
# print(df.sort_values(by=[0,2], ascending=True))

df = pd.DataFrame({'num_legs': [2, 4, 4, 6],
                   'num_wings': [2, 0, 0, 0]},
index=['falcon', 'dog', 'cat', 'ant'])
# print(df.sort_index())
# print(df.sort_index(ascending=False))

print(df.sort_values(by='num_legs', ascending=False))

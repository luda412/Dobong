import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
import seaborn as sns
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# data = {
#     "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
#     "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
#     "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
#     "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
# }
# columns = ["도시", "연도", "인구", "지역"]
# df1 = pd.DataFrame(data, columns=columns)

# pt_df = df1.pivot_table(index=['지역', '도시'], columns='연도', values='인구')
# print(pt_df)

# df = sns.load_dataset('titanic')[['age', 'sex', 'class', 'fare', 'survived']]
# # print(df.head())
# pdf1 = pd.pivot_table(
#     df,
#     index = ['sex', 'class'],
#     columns= 'survived',
#     values= ['age' ,'fare'],
#     aggfunc=['mean', 'max'] #데이터 집계 함수
# )
# print(pdf1)

# np.random.seed(0)
# df2 = pd.DataFrame({
# 'key1': ['A', 'A', 'B', 'B', 'A'],
# 'key2': ['one', 'two', 'one', 'two', 'one'],
# 'data1': [1, 2, 3, 4, 5],
# 'data2': [10, 20, 30, 40, 50]
# })
# print(f"{df2}\n")

# gd = df2.groupby(df2.key1)
# print(gd.groups.keys())
# print(pd.DataFrame(gd).loc[1].values[1])
# print(gd.sum()['data1'])
# print(gd.sum()['data2'])

iris = sns.load_dataset("iris")
print(f"iris original data: \n{iris} \n")
i_gs = iris.groupby(iris.species)
# print(type(i_gs))
i_gs_df = pd.DataFrame(i_gs)
# print(f"\n======================= setosa groups =======================\n")
# print(i_gs_df.loc[0].values[1].head())
# print(f"\n======================= versicolor groups =======================\n")
# print(i_gs_df.loc[1].values[1].head())
# print(f"\n======================= virginica groups =======================\n")
# print(i_gs_df.loc[2].values[1].head())

# print(f"\n======================= setosa groups =======================\n")
# print(i_gs.sepal_width.max())
# print(f"\n======================= versicolor groups =======================\n")
# print(i_gs_df.loc[1].values[1]['sepal_width'].max())
# print(f"\n======================= virginica groups =======================\n")
# print(i_gs_df.loc[2].values[1]['sepal_width'].max())

# print(i_gs.petal_length.sum())

def peak_to_peak_ratio(x):
    return x.max()/x.min()
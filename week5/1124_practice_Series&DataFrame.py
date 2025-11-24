import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc  ### 이 줄과
rc('font', family='AppleGothic') 			## 이 두 줄을
plt.rcParams['axes.unicode_minus'] = False  ## 추가해줍니다.

s1 = pd.Series([1, 2, 3])
# print(s1)

s2 = pd.Series((1.0, 2.0, 3.0))
# print(s2)

s3 = pd.Series(['a', 'b', 'c'])
# print(s3)

s4 = pd.Series([90, 85, 100], index = ['lee', 'kim', 'park'])
# print(s4.index)
# print(s4.values)

scity = pd.Series([9904312,3448737,289045,2466052],index=["서울","부산","인천","대구"])
scity.index.name = '광역시'
scity.name = '인구수'
# print(s.index)
# print(s.values)
# print(s['인천'])
# print(s5['부산'])
# print(s5[1], s5['대구'])
# print(s5[0:3])
# s5[0] = 10000000
# print(s5.서울)

# for k, v in scity.items():
#     print(f"{k} = {v}")

s6 = pd.Series([1, 2, 3], index=[1, 2, 3])
# print(s6)
# print(s6[2])

s7 = pd.Series([100, 200, 300, 400], index=["1", "2", "3", "4"])
# print(s7)
# print(s7['2'])
# print(s7[1:4])


s8 = pd.Series(range(3), index = ['a', 'b', 'c'])
# print(s8)
# print(s8.a)

s9 = pd.Series(np.arange(10), np.arange(10)+1)
# print(s9[s9.index>5])

a = pd.Series(['a ', 'a', 'a', 'b', 1, 2, 3])
# print(a.value_counts())

num_s1 = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
# print(num_s1)

num_s2 = pd.Series([5, 6, 7, 8], index = ['d', 'c', 'b', 'a'])
# print(num_s2)

num_s3=pd.Series([5,6,7,8],index=['e','b','f','g'])
num_s4=pd.Series([1,2,3,4],index=['a','b','c','d'])

result = num_s3.values - num_s4.values
# print(result)

city = {'서울':9631482,'부산':3393191,'인천':2632035,'대전':1490158}
s = pd.Series(city, index = city.keys())
s['부산'] = 1630000
del s['서울']
s['대구'] = 1875000
# print(s)

df = pd.DataFrame([['a', 'b', 'c'], ['a', 'a', 'g'], ['a', 'a']])
# print(df)

data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}
columns =['지역','2000','2005','2010','2015', '2010-2015 증가율']
index = ['서울','부산','인천','대구']
df3 = pd.DataFrame(data, index=index, columns=columns)
print(df3)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)

# 제목과 축 라벨
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 그래프 표시
plt.show()


s3 = pd.Series([1, 2, 3, 4])
s4 = pd.Series([10, 20, 30, 40, 50])
print(s4/s3)

rain_data_four_seasons = {'봄':  [256.5, 264.3, 215.9, 223.2, 312.8],
              '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
              '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
              '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}
columns_list_four_seasons = ['봄', '여름', '가을', '겨울']
index_list_four_season = ['2012', '2013', '2014', '2015', '2016']

df_rains = pd.DataFrame(rain_data_four_seasons, columns=columns_list_four_seasons, index=index_list_four_season)
print(df_rains)
print(f"mean = \n{df_rains.mean()}")
print(f"mean(axis) = \n{df_rains.mean(axis=1)}")
print(f"{df_rains.describe()}")


KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
columns_list_ktx = ['경부선 KTX','호남선 KTX','경전선 KTX','전라선 KTX','동해선 KTX']
index_list_ktx = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_ktx = pd.DataFrame(KTX_data, columns=columns_list_ktx, index=index_list_ktx)
print(df_ktx)
print(df_ktx.head())
print(df_ktx.tail())
print(df_ktx[2:5])
print(df_ktx.loc['2011'])
print(df_ktx['동해선 KTX']['2011'])
print(df_ktx[['경부선 KTX','호남선 KTX']]['2012':'2014'])
print(df_ktx.loc['2012':'2014'][['경부선 KTX','호남선 KTX','전라선 KTX']])
print(df_ktx.loc['2015'] >= 41702)
print(df_ktx.T['2012']['경부선 KTX'])

df1 = pd.DataFrame({"Class1": [95, 92, 98, 100],
                    'Class2': [91, 93, 97, 99]})
print(df1)
print(f"df3: \n{df1}")
df2 = pd.DataFrame({'Class1': [87, 89],
                    'Class2': [85, 90]})

print(df2)
print(f"df3: \n{df2}")
concated_df = pd.concat([df1, df2])
print(concated_df)
df3 = pd.DataFrame({'Class1': [96, 83]})
print(f"df3: \n{df3}")

df4 = pd.DataFrame({'Class3': [93, 91, 95, 98]})
print(f"df4: \n{df4}")

print('==========================')
concated_less_df = pd.concat([df2, df3])
print(concated_less_df)
joined_df = df1.join(df4)
print(joined_df.join)

index_label = ['a', 'b', 'c', 'd']
df1a = pd.DataFrame({'Class1': [95, 92, 98, 100],
                     'Class2': [91, 93, 97, 99]}, index = index_label)
print(df1a)
df4a = pd.DataFrame({'Class3': [93, 91, 95, 98]}, index = index_label)
print(df4a)
df5 = pd.DataFrame({'Class4': [82, 92]})
print(df5)

print("=====================")
joined_df = df1a.join(df4a)
print(joined_df)
joined_df2 = df1.join(df5)
print(joined_df2)

df_A_B = pd.DataFrame({
    'month':['Jan', 'Feb', 'Mar', 'Apr'],
    'productA': [100, 150, 200, 130],
    'productB': [90, 110, 140, 170]
})
print(f"df_A_B:\n{df_A_B}")

df_C_D = pd.DataFrame({
    'month':['Jan', 'Feb', 'Mar', 'Apr'],
    'productC': [200, 130, 80, 190],
    'productD': [123, 140, 160, 60]
})
print(f"df_C_D:\n{df_C_D}")
merged_df1 = df_A_B.merge(df_C_D)
print(f"merged_df1:\n{merged_df1}")
df_left = pd.DataFrame({
    'key': ["A", "B", "C"],
    "left": [1, 2, 3]
})
print(f"df_left:\n{df_left}")

df_right = pd.DataFrame({
    "key":["A", "B", "D"],
    'right': [4, 5, 6]
})
print(f"df_right: \n{df_right}")
print(df_left.merge(df_right, how='inner', on='key'))

temp = pd.read_csv('sea_rain1.csv', index_col ='동해')
print(temp)


df_WH = pd.DataFrame({
    'Weight':[62, 67, 55, 74],
    'Height':[165, 177, 160, 180]
    },index=['ID_1', 'ID_2', 'ID_3', 'ID_4'])
df_WH.index.name = 'User'
print(df_WH)
bmi = df_WH['Weight']/(df_WH['Height']/100)**2
print(bmi)
df_WH['BMI'] = bmi
print(df_WH)
df_WH.to_csv('save_DataFrame.csv')

df_pr = pd.DataFrame({
    'price': [2000, 3000, 5000, 10000],
    'mount': [32, 53, 40, 25]}, index = ['P1001', 'P1002', 'P1003', 'P1004'])
df_pr.index.name = 'ProductNumber'
print(df_pr)
file_name = 'save_DataFrame_cp949.txt'
df_pr.to_csv(file_name, sep=" ", encoding='cp949')

data1 = [10, 14, 19, 20, 25]
plt.plot(data1)
plt.show()
from matplotlib import rc  ### 이 줄과
rc('font', family='AppleGothic') 			## 이 두 줄을
plt.rcParams['axes.unicode_minus'] = False  ## 추가해줍니다.

x = np.arange(-4.5, 5, 0.5)
y1 = 2*x**2
y2 = 5*x + 30
y3 = 4*x**2 + 10
plt.plot(x, y1)

plt.figure()
plt.plot(x, y2)

plt.show()

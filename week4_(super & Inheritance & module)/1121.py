import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc  ### 이 줄과
rc('font', family='AppleGothic') 			## 이 두 줄을
plt.rcParams['axes.unicode_minus'] = False  ## 추가해줍니다.

# height = [165, 177, 160, 180, 185, 155, 172]
# weight = [62, 67, 55, 74, 90, 43, 64]
#
# size = 100 * np.arange(1,8)
# colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y']
#
# plt.scatter(height, weight, s=size, c=colors)
# plt.xlabel('Height(m)')
# plt.ylabel('Weight(kg)')
# plt.title('Height & Weight')
# plt.grid(True)
# plt.show()

# city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']
# # 위도(latitude)와 경도(longitude)
# lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
# lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]
# # 인구 밀도(명/km^2): 2017년 통계청 자료
# pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]
# print(f"den type: {type(pop_den)}")
# size = np.array(pop_den) * 0.2 # 마커의 크기 지정
# print(f"size type: {type(size)}")
# print(f"size values: {size}")
# colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y'] # 마커의 컬러 지정
# print(f"colors type: {type(colors)}")
# plt.scatter(lon, lat, s=size, c=colors, alpha=0.5)
# plt.xlabel('경도(longitude)')
# plt.ylabel('위도(latitude)')
# plt.title('지역별 인구 밀도(2017)')
# for x, y, name in zip(lon, lat, city):
#     plt.text(x, y, name)
# plt.show()

# member_IDs = ['m_01', 'm_02', 'm_03', "m_04"]
# before_ex = [27, 35, 40, 33]
# after_ex = [30, 38, 42, 37]
# colors = ['r', 'g', 'b', 'm']
#
# n_data = len(member_IDs)
# index = np.arange(n_data)
#
# bar_width = 0.4
#
# plt.bar(index, before_ex, color = 'c', align='edge', width = bar_width, label='before')
# plt.bar(index + bar_width, after_ex, color = 'm', align='edge', width = bar_width, label='after')
#
# plt.xticks(index + bar_width, member_IDs)
# plt.legend()
# plt.xlabel('Member ID')
# plt.ylabel('윗몸일으키기 횟수')
# plt.title('운동 시작 전과 후의 근지구력(복근) 변화 비교')
# plt.show()

# math = [76, 82, 84, 83, 90, 86, 85, 92, 72, 71, 100,
#         87, 81, 76, 94, 78, 81, 60, 79, 69, 74, 87, 82, 68, 79]
# plt.hist(math, bins = 50)
# plt.xlabel('시험 점수')
# plt.ylabel('도수(frequency)')
# plt.title('수학 시험의 히스토그램')
# plt.grid()
# plt.show()

# fruit = ['apple', 'banana', 'strawberry', 'orange', 'grape']
# result = [7, 6, 3, 2, 2]
# explode_value = (0.1, 0, 0, 0, 0)
# plt.figure(figsize=(5,5))
# plt.pie(result, labels = fruit, autopct='%.1f%%', startangle=90, counterclock=False,
#         explode = explode_value, shadow = True)
# plt.savefig('saveFigTest2.png', dpi = 200)
# plt.show()

# x = np.arange(0, 5, 1)
# y1 = x
# y2 = x + 1
# y3 = x + 2
# y4 = x + 3
#
# plt.plot(x, y1, x, y2, x, y3, x, y4)
#
# plt.grid(True)
# plt.xlabel('x')
# plt.ylabel('한국어', rotation=0)
# plt.title('Saving a figure')
#
# plt.savefig('saveFigTest1.png', dpi=300)
# plt.show()
file_name = 'notExercise.csv'

temp = pd.read_csv(file_name, sep=",")
df_temp = pd.DataFrame(temp)
# print(df_temp['여자'][2])
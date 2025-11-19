import numpy as np
import pandas as pd
#
# pr1 = np.zeros(10)
# # print(pr1)
#
# pr2 = np.zeros((4, 3))
# # print(pr2)
#
# pr3 = np.ones(5)
# # print(pr3)
#
# pr4 = np.ones((4, 3))
# # print(pr4)
#
# pr5 = np.eye(4)
# # print(pr5)
#
# a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]).reshape(3, 3)
# b = np.array([8, 7, 6, 5, 4, 3, 2, 1, 0]).reshape(3, 3)
# # print(a)
# # print(a.dot(b))
# # print(np.transpose(a))
# # temp = np.linalg.inv(a)
# # print(temp)
#
# # t = np.array([0,1,2,3]).reshape(2,2)
# # print(np.linalg.inv(t))
# # print(a[1:,:2])
#
# s1 = pd.Series([10, 20, 30, 40, 50])
# # print(type(s1))
# s2 = pd.Series([np.nan, 'b', 'c', 1, 2, 3])
# # print(s2.values)
# # print(s2.index)
# s5 = pd.Series({'kor': np.nan, 'eng': 95, 'mat':90})
# # print(s5.index)

pr1 = pd.Series([10, 20, 30, 40, 50])
# print(pr1.values)
pr2 = pd.Series([np.nan, 'b', 'c', 1, 2, 3])
# print(pr2)

# index_date = ['2025-11-11', '2025-11-11', '2025-11-11', '2025-11-11']
# pr3 = pd.Series([200, 195, np.nan, 205], index = index_date)
# print(pr3)

# pr4 = pd.Series({'kor': 100, 'eng': 70, 'math': 80)
# print(pr4)

# index_date = pd.date_range(start = '2025-03-01', periods = 5, freq = 'D')
# print(pd.Series([51, 54, 64, 75, 51], index = index_date))

# data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(f"data: {type(data)}")
# index_date = pd.date_range('2025-11-11', periods = 4)
# print(f"index_date: {type(index_date)}")
# columns_list = ['A', 'B', 'C']
# print(f"columns_list: {type(columns_list)}")
# temp = pd.DataFrame(data.values, index = index_date, columns = columns_list)
# print(temp)
# print(f"temp: {type(temp)}")

table_data = {
    'year': [2015, 2016, 2016, 2017, 2017],
    'location': ['kor', 'kor', 'usa', 'kor', 'usa'],
    'customer': [200, 250, 500, 300, 500]
}
print(f"table_data = {table_data}")

add_data = {'manger':['lee', 'kim', 'lee', 'park', 'lee']}
print(f"add_data: {add_data}")

# merged = {**table_data, **add_data}
# print(f"merged: {merged}")

# print(table_data)
temp = pd.DataFrame(table_data, columns=['year', 'customer', 'location' ])
temp['manger'] = add_data['manger']
print(temp)









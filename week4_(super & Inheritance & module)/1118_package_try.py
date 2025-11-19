# from imgread import pngread as png
# from imgread import jpgread as jpg
#
#
# png()
# jpg()
# try:
#     x = int(input("나눌 숫자를 입력하세요:"))
#     y = 10/x
#     print(y)
# except:
#     print("예외가 발생했습니다.")
# y = [10, 20, 30]
# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# except IndexError:
#     print('잘못된 인덱스입니다.')
# try:
#     print(5/0)
#     print(e)
# except NameError as e:
#     e = "name Error"
#     print(e)
# except ZeroDivisionError as e:
#     e = "division Error"
#     print(e)
# try:
#     age = int(input())
#     if  age < 0:
#         raise NameError
#     print(age)
# except NameError:
#     print("NameError")
import numpy as np
import pandas as pd
# data1 = [0, 1, 2, 3, 4, 5]
# a1 = np.array(data1)
# print(a1)
# print(a1.dtype)
# print(a1.min(), a1.max())
# data2 = [0.1, 5, 4, 12, 0.5]
# a2 = np.array(data2)
# print(a2)
# print(a2.min(), a2.max())

# print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(np.arange(12).reshape(4,3))

# b1 = np.arange(12).reshape(4, 3)
# print(b1.shape)

# b2 = np.arange(5)
# print(b2)
# print(b2.shape)

# print(np.linspace(1, 10, 10))
# zeroArray = np.zeros((4, 3))
# print(zeroArray)
# oneArray = np.ones((4, 3))
# print(oneArray)
# a = np.eye(4)
# print(a)
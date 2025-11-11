# with open("test.txt", "w") as f:
#     f.write("Hello World")
#     print(type(f))
#
# with open("test.txt", "r") as f:
#     data = f.read()
# print(data)

# with open('../two_times_table.txt', 'w') as f:
#     for num in range(1,6):
#         fstring = "2 X {0} = {1}\n".format(num, num*2)
#         f.write(fstring)

# f = open("two_times_table.txt", "r")
# lines = f.readlines()
# f.close()
# print(lines)

# with open("../two_times_table.txt", 'r') as f:
#     lines = f.readlines()
#
# for line in lines:
#     print(line, end="")

# with open("../two_times_table.txt", 'r') as f:
#     for line in f.readlines():
#         print(line, end="")

def my_func():
    print("My first function!")
    print("This is a function")

# my_func()
def my_friend(friendName):
    print(f"{friendName}는 나의 친구 입니다.")

# my_friend("철수")
# my_friend("영미")

def my_calc(x, y):
    z = x * y
    return z
# print(my_calc(3, 4))

# 백준 15596
def resolve(a):
    total = 0
    for i in a:
        total += i
    return total

# print(resolve([5]))

# 백준 1065
# N = input()
#
# def separate(N):
#     if(N == 1000):
#
#
#     elif(N >= 100):
#         hundreds = 1
#         tens = N / 10
#         ones = N /100
#     elif(N >= 10):
#
#     elif(N >= 1):
#
#     else:
#         return 1

# a = 5
# print(f"함수 밖의 전역 변수 {a}")
# def func1():
#     a = 1
#     print(f"지역 변수 {a}")
#
# def func2():
#     global a
#     a = 3
#     print(f"글로벌 키워드 변수 {a}")
#
# func1()
# func2()
# print(f"함수 밖의 전역 변수 {a}")
from functools import reduce
a = 10
if(a == 10):
    print("a = 10")

x = 95
if x >= 90:
    print("Pass")

x = 75
if x >= 90:
    print("Pass")
else:
    print("Fail")

# if ~ elif ~ else 조건문 예시
x = 85
if x >= 90:
    print("Very good")
elif (x >= 89) and (x < 90):
    print("Good")
else:
    print("Bad")

# 중첩 조건문 예시
x = 100
if x >= 90:
    if x == 100:
        print("Perfect")
    else:
        print("Very Good")
elif (x >= 80) and (x < 90):
    print("Good")
else:
    print("Bad")
# ======================================

# for 반복문 예시
for a in [0, 1, 2, 3, 4, 5]:
    print(a)

# for 반복문 list example
myFriends = ['James', 'Robert', 'Lisa', 'Mary']
for myFriend in myFriends:
    print(myFriends)

# for 반복문 range example
for i in range(0, 10, 1):
    print(i)

# nested for example
x_list = ['x1', 'x2']
y_list = ['y1', 'y2']
print('x y')
for x in x_list:
    for y in y_list:
        print(x, y)

# 구구단
for x in range(2,10):
    print()
    print(str(x)+"단 출력")

    for y in range(1, 10):
        print(str(x)+" X " + str(y) +" = " + str(x*y))

# 구구단 lambda 함수
multiply = lambda x, y: x * y
for x in range(2, 10):
    print()
    print(f"{x}단 출력")
    for y in range(1, 10):
        print(f"{x} x {y} = {multiply(x, y)}")


# 여러 개의 리스트 다루기
names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]
for k in range(len(names)):
    print(names[k], scores[k])

# zip func example
names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]
for names, scores in zip(names, scores):
    print(names, scores)

# 백준 2739 - 구구단
N = int(input());
for i in range(1, 10):
    print(str(N) + " * " + str(i) +" = " + str(N*i))

# 백준 10950 - A+B -3
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
T = int(input());
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)

# lambda func 람다 함수의 결과 값이 0이면 버려지고 1이상은 참 이니까 통과 즉, 결과 값에 담긴다.
result2 = list(map(lambda x: x * 2, range(5)))
print(f" {result2}")
result = reduce(lambda x, y: y + x,'abcde')
print(result)
result = filter(lambda x: x % 2, range(10))
print(list(result))

# while loop example
i = 0
sum = 0
print("i sum")
while(sum < 20):
    i += 1
    sum += i
    print(i, sum)

# break example
k = 0;
while True:
    k = k + 1
    if(k > 3):
        break
    print(k)
for k in range(10):
    if(k > 2):
        break
    print(k)

# continue example
for k in range(5):
    if(k == 2):
        continue
    print(k)

# k = 0
while True:
    k = k + 1

    if(k == 2):
        print("continue next")
        continue
    if(k > 4):
        break
    print(k)

# comprehension example
numbers = [1, 2, 3, 4, 5]
square = []
for i in numbers:
    square.append(i ** 2)
print(square)

numbers = [1, 2, 3, 4, 5]
square = [i**2 for i in numbers]
print(square)

# conditional comprehension
numbers = [1, 2, 3, 4, 5]
square = []
for i in numbers:
    if i >= 3:
        square.append(i**2)
print(square)

numbers = [1, 2, 3, 4, 5]
square = [i**2 for i in numbers if i >= 3]
print(square)


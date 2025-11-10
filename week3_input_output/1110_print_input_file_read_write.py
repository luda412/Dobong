print('best', 'python', 'book')
print('best', 'python', 'book', sep = '-:*:-')
print('best', 'python', 'book',end='')
print('hello')
print('abcd'+'efg')
print('best', 'python','book'+':', 'This book')
x = 10
print(x)
name = 'James'
ID_num = 789
print('Name:', name + ',', 'ID_num:', ID_num)
print(f"Name: {name}, ID_num: {ID_num}")
print("James is my friend.\nHe is Korean")
print("James is my friend.\n\nHe is Korean")
print('Welcome to ', end='')
print('python!')

백준 25314
N = int(input())
while(N>0):
    if(N > 4):
        print('long ', end='')
    else:
        print('long int')
    N-=4

백준 8393
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)

print('%type'%data)
name = '광재'
print('%s는 나의 친구입니다.' %name)

r = 3
PI = 3.141592653589793
print('반지름: %d, 원주율: %F' %(r,PI))
print(f'반지름: {r}, 원주율: {PI:.6f}')

animal_0 = 'cat'
animal_1 = 'dog'
animal_2 = 'fox'
print('Animal: {0}'.format(animal_0))
print('Animal: {0}, {1}, {2}'.format(animal_0, animal_1, animal_2))
print('Animal: {}, {}, {}'.format(animal_0, animal_1, animal_2))

name = 'Tomas'
age = 10
a = 0.1234567890123456789
fmt_string = 'String: {0}, Integer Number: {1}, Floating Number: {2}'
print(fmt_string.format(name, age, a))

a = 0.12345678901234567889
print('{0:.2f}, {0:.5f}'.format(a))

print("안녕하세요.\n만나서 \t\t 반갑습니다.")

naver;kakako;sk;samsung 을 print
print("naver;kakao;sk;samsung")
print("naver;"+"kakao;"+"sk;"+"samsung")
print("naver","kakao","sk","samsung", sep=";")
naver = 'naver'
kakao = 'kakao'
sk = 'sk'
samsung = 'samsung'
print("{0};{1};{2};{3}".format(naver, kakao, sk, samsung))
print(f"{naver};{kakao};{sk};{samsung}")

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def greet(self):
        print(f"Hello, my name is {self.name}, I'm from {self.country}" )

Person_1 = Person("Bob", "US")
print(Person_1.name)
Person_1.greet()
Person_2 = Person("John", "KOR")
Person_2.name = "kim"
def cal(n):
    return n+n
print(f"계산값: {cal(5) }")

yourName = input("당신의 이름은? ")
print("당신은 {}이군요.".format(yourName))
print(f"당신은 {yourName}이군요")

num = input("숫자를 입력하세요(숫자만 입력가능합니다.): ")
try:
    num_int = int(num)
    print(f"당신이 입력한 숫자는 {num}입니다.")
except ValueError:
    print("숫자만 입력 가능합니다.")

b = input("정사각형 한 변의 길이는?: ")
area = float(b) **2
print("정사각형의 넓이: {}".format(area))

class Scores:
    def __init__(self, name, korean, math, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.science = science

    def to_string(self):
        return f'이름: {self.name} 국어: {self.korean} 수학: {self.math} 과학: {self.science}'

    def save_to_file(self, filename="student.txt"):
        with open(filename, 'w') as f:
            f.write(self.to_string())
            f.write(self.cal_avr(self.korean, self.math, self.science))
    def cal_avr(self,korean,math,science):
        avr = str((korean + math + science)/3)
        return avr

def main():
    while True:
        user_input = input("성적 관리 시스템 시작.(q를 누르면 종료 됩니다.)")
        if user_input == "q":
            print("프로그램 종료")
            break

        name = input("이름을 입력하세요.:")
        try:
            korean = int(input("국어점수를 입력하세요.: "))
            math = int(input("수학점수를 입력하세요.: "))
            science = int(input("과학점수를 입력하세요.: "))
        except ValueError:
            print("점수는 숫자로 입력해주세요.")
            continue

        score = Scores(name, korean, math, science)
        score.save_to_file()
        print(f"{name}학생의 성적이 저장되었습니다.")
if __name__ == '__main__':
    main()

f = open('test.txt', 'w')
f.write('Hello World')
f.close()

f = open('test.txt', 'r')
file_txt = f.read()
f.close()
print(file_txt)

with open('two_times_table.txt', 'w') as f:
    for num in range(1, 6):
        format_string = "2 x {0} = {1} \n".format(num, 2*num)
        f.write(format_string)

with open('two_times_table.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
print(line1, end='')
print(line2, end='')

with open('two_times_table.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

with open("two_times_table.txt", "r") as f:
    lines = f.readlines()
print(lines)


print('Hello World');

x = 3;
y = 'hello';

print(x);
print(y);

print(3+2);

a = 1;
print(type(a));

# name = input('name: ')
# print(name)
x *= 2  # x = x * 2
print('ddd')
print(x)

def chat():
    print('basic python grammar')

def multiply(num):
    for i in range(1,10):
        print(num, 'X', i, '=', num*i)

# multiply(2)

def chat_demo(name1, name2):
    print("%s: hello, how are you doing?" %name1);
    print("%s: I'm good" %name2);

# chat_demo("lee", "kim")

def dsum(a, b):
    result = a+b;
    return result;
# print(dsum(1, 2));

class Person:
    name = "hong";

    def say_hello(self):
        print("hello! I'm " + self.name);

p = Person(); # Person 을 p라는 변수에 담는다.
p.say_hello(); # class Person의 function say_hello를 실행
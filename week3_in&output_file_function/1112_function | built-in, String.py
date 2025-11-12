mySquare = lambda x: x**2
print(mySquare(5))

mySimpleFunc = lambda x, y, z: 2*x + 3*y + z
print(mySimpleFunc(1, 2, 3))

print([int(0.123), int('3')])

print(float(0), float('10'))

print(str(123), str(12.12))
print(list({1, 2, 3}), tuple([1, 2, 3]), set([1, 2, 3]))

print(bool(0), bool(1), bool(-10), bool(4.12), bool(-10))

print(bool('a'), bool(' '), bool(''), bool(None))

def print_name(name):
    if bool(name):
        print(f"입력된 이름: {name}")
    else:
        print("입력된 이름이 없습니다.")
# print_name("James")

myNum = [10, 5, 12, 0, 3.5, 99.5]
print(f"최대: {max(myNum)}, 최소: {min(myNum)}")

str = "korean english math"
print(str.split(maxsplit=1))

phone_number = "+82-01-2345-6789"
split_num = phone_number.split("-",1)

print(split_num)
print(f"국내전화번호: {split_num[0]}")

str = "aaaaPythonbbaa"
print(str.strip('ba'))

ordered_coffee = "   espresso,  americano  , cafeLatte   "
splited_coffee = ordered_coffee.split(',') # 콤마를 기준으로 문자열을 자름 "   espresso"가 들어있음
print(splited_coffee)
result_list = []
for coffee in splited_coffee:
    striped_coffee = coffee.strip()
    result_list.append(striped_coffee)
print(result_list)


ordered_coffee = [["  americano  ,   latte ,   americano "], ["  latte  ,  latte "]]

str_coffee = ordered_coffee[0]

joined_coffee = "".join(str_coffee))


str_coffee1 = ordered_coffee[1]
print(str_coffee)
print(str_coffee1)



for coffee in ordered_coffee:


to_make_coffee = []

for coffee in splited_coffee:
    striped_coffee = coffee.strip()
    to_make_coffee.append(striped_coffee)
print(to_make_coffee)



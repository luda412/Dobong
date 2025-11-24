address_list = ["서울시", "도봉구", "창동"]
a = ", "
print(a.join(address_list))
str_f = "Python code"
print(f"찾는 문자열의 위치: {str_f.find('Python')}")
print(f"찾는 문자열의 위치: {str_f.find('code')}")
print(f"찾는 문자열의 위치: {str_f.find('n')}")
print(f"찾는 문자열의 위치: {str_f.find('easy')}")
str_f_se = "Python is powerful. Python is easy to learn"
print(str_f_se.find("Python", 10, 30))
print(str_f_se.find("Python", 35))
str_c = "Python is powerful. Python is easy to learn. Python is open"
print(f"Python의 개수는? {str_c.count('Python')}")
print(f"Python의 개수는? {str_c.count('powerful')}")
print(f"Python의 개수는? {str_c.count('IPython')}")
str_se = "Python is powerful. Python is easy to learn."
print(f"Python으로 시작?: {str_se.startswith('Python')}")
print(f"is로 시작?: {str_se.startswith('is')}")
print(f".로 끝?: {str_se.endswith('.')}")
print(f"learn으로 끝?: {str_se.startswith('learn')}")
str_a = "Python is fast. Python is friendly. Python is open."
print(f"{str_a.replace('Python', 'IPython')}")
print(f"{str_a.replace('Python', 'IPython', 2)}")
str_b = "[Python] [is] [fast]"
print(f"{str_b.replace('[','').replace(']','')}")
print(str_b)
print(str_b1)
print(str_b2)
print('Python'.isalpha())
print('Ver. 2.x'.isalpha())
print('1234'.isdigit())
print('1234adf'.isdigit())
print('abc123'.isalnum())
print('    abc123'.isalnum())
print('   '.isspace())
print(' 1  '.isspace())
print('PYTHON'.isupper())
print('python'.islower())

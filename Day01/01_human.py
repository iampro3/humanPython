# 주석
""" '주석입니다'  """
""" "주석입니다" """
""" 주석은 alt + enter """


""" a=7
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 나누기 : 실수형으로 결과가 나온다.
print(a//b)  # 몫
print(a**b) # 제곱
print(a%b) # 나머지 """


# 논리연산자 AND / OR

""" print(True and True)
print(True and False)
print(False and True)
print(False and False) """

# OR 연산자
""" print(True or True)
print(True or False)
print(False or True)
print(False or False) """

# 비교 연산자
""" print(4>3)
print(3>4)
print(3>=4)
print(3<=4) """

# input 입력
""" var = input("값을 입력해주세요!!")
print(var) """

# input 입력 - 데이터 type 확인
""" var = input("값을 입력해주세요!!")
print(var)
print(type(var)) """

# 형 변환하여 result 결과 출력
""" num1 = input("값을 입력하세요")
num2 = input("값을 입력하세요")
result = int(num1)+int(num2)
print(result) """

# 문자열 1
""" str1 ="Hello "
str2="World"
print(str1+str2) """

# 문자열 2
""" str1 ="55"
str2="1000"
print(str1+str2) """

# slicing
greeting = "Hello World"
print(greeting[0:5:4])
print(greeting[:])
print(greeting[6:])
print(greeting[3:9]) # 마지막 인덱스는 포함이 안 됨

# index error
greeting = "Hello World!"
greeting[13]    # IndexError: string index out of range

# documentation 활용하기
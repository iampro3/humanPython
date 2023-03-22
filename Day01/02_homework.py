greeting = 'Hello World!'
print(greeting)



food = "Python's favorate food is Perl"
food

say = '"Python is very easy" he says.'
say

'"Python is very easy" he says.'


food = 'Python\'s favorate is Perl' # 소유격을 의미하는 ['s] 를 붙이고 싶을 때, \를 '앞에 붙인다.
food

say = "\"Python is very easy.\" he says." # "쌍따옴표를 넣고 싶을 때, 쌍따옴표 앞에 \를 붙이면 출력된다."
say


# 중략 - Day01 수업과 중복내용

retn = "Life is too short\r"
print(retn)

say = "\"Life is too short\""
print(say)


say = '\'Life is too short\''

print(say)

head = "Python "
tail = "is fun"
head + tail

a = "Python"
a*2

print("="*50)
print("My program")
print("="*50)

a="Life is too short, You need a Python"
len(a)

a="Life is too short, You need a Python"
b=a[0]+a[1]+a[2]+a[3]
b

#슬라이싱으로 문자열 나누기
a="20010331Rainy"
date=a[:8] # 0부터 시작해서 7인 날짜까지 출력
weather=a[8:]
date

weather

a="20010331Rainy"
year=a[:4]
day=a[4:8]
weather=a[8:]
year

day

weather

a="pithon"
a[1] 
'i'
a[1]='y'

a="pithon"
a[:1]
a[2:]
a[:1]+'y'+a[2:]

"I eat a %s apples" %"five"

"I eat a %d apples" %3

number = 3
"I eat a %d apples" %number

number = 3
day ="three"
"I ate a %d apples. so I was sick for %s days." % (number, day)

"I have %s apples" %3

"Rate is %s" % 3.242

"Error is %d%" % 98
""" ---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-107-1e56ee03da63> in <module>
----> 1 "Error is %d%" % 98
ValueError: incomplete format """

"Erorr is %d%%" %98

"%10s" % "hi"

"%-10sjane." % "hi"

"%0.4f" % 3.241253

"%10.4f" % 3.241351

# format 함수를 사용한 포매팅
"I eat a {0} apples." .format(3)


"I eat a {0} apples" .format("five")


number = 3
"I eat a {} apples".format(number)

number = 3
day = "three"
"I ate a {0} apples. I sick for a {0} days" .format(number, day)

"I ate a {number} apples. I sick for a {day} days".format(number=3, day=5)

"I ate a {0} apples. I sick for a {day} days" .format(3, day=5)

"{0:<10}".format("hi")

"{0:>10}".format("hi")

"{0:^10}".format("hi")

name = "홍길동"
age = "30"
f"나의 이름은 {name}입니다. 나이는 {age}세 입니다."

age = 30
f"나는 내년에 {age+1}세가 된다."
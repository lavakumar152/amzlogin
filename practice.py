"""
char_name = 'lava'
char_age = '27'

print('there was a man named' + char_name + '.')
print('he is '+ char_age +'years old .' )
print('he really liked the name' + char_name +'.')
print('he like being' +char_age+'.')

name = 'lavakumar'
print(name.replace('lava', 'reddy'))

name = input('Enter the name : ')
age = input('enter the age : ')
print('hello ' + name + ' ! ' + 'you are '+age+' years old')


num1 = input('Enter a number')
num2 = input('Enter a number')

result = int(num1) + int(num2)

print(result)

name = input('enter your name')
place = input('enter your nativity')
profession = input('enter your profession')

print('my name is ' +name)
print(place + ' i am living in')
print('i am a ' + profession)

friends = ['lava', 'reddy', 'kumar', 'rani']
friends[1] = 'teddy'
print(friends)

coordinates = [(1,9), (5,6), (7.6), (5,8)]
coordinates[1] = (0,0)
print(coordinates)


def my_bio(name,age):
    print('hello ' +name+' you are '+ str(age) +'years old')
my_bio('lava', 27)


def cube(num):
    return num*num*num
print(cube(5))

is_male = True
is_tall = False
if is_male and is_tall:
    print('male or tall or both')
else:
    print('not male not tall')


def max_num(num1,num2,num3):
    if num1 > num2 and num1 >num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(max_num(1,9,22))


num1 = float(input('Enter the number'))
op = input('enter the operator')
num2 =float(input('enter the number'))

if op == '+' :
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1/ num2)
else:
    print('enter a valid num or bool')

month_con = {
    'jan' : 'january',
    'feb' : 'february',
    'mar' : 'march'
}

print(month_con.get('mar'))

i =  0
while i <= 10:
    print(i)
    i +=1
print('done with the  loop')

sec_word = 'lava'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != sec_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input('enter the guess_num :')
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print('Out of guess , You loose')
else:
    print('you win!')



print('you win')

def raise_to_power(b_n, p_n):
    result = 1
    for i in range (p_n):
        result = result * b_n
    return result

print(raise_to_power(5,6))
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9],
    [0]
]


print(number_grid[2][1])



def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter in 'aeiouAEIOU':
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input('enter a pharse')))

try:
    num = int(input('enter a number'))
    print(num)
except:
    print('invalid input')


employee_file = open('hello.py', 'r')
for i in employee_file.readlines():
    print(i)
employee_file.close()

from Student import Student
student1 = Student('lava', 27, 'developer', False)
print(student1.name)


# sorting values without the function sort
a = [4, 5, 6, 9, 8, 2, 0, 1, 3, 4]
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)

# print the vowels
a = 'enter a string'
for i in a:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        print(i)

# counting the vowles
sentence = input('enter a sentence')
string = sentence.lower()
count = 0
list1 = ['a', 'e', 'i', 'o', 'u']
for i in string:
    if i in list1:
        count = count+1
print(count)

a = [1, 2, 1, 5, 9, 6, 3, 5]

print(sort(a))

# reversing a num
n = 456
rev = 0
while n > 0:
    i = n % 10
    rev = rev * 10+i
    n = n // 10
print(rev)

def reverse(string):
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    print('reversed string', )

txt= "hello world" [::-1]
print(txt)

num = "123"  [:: -1]
print(num)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])




class Person:
    def __init__(self, name, age, partner_name):
        self.name = name
        self.age = age
        self.partner_name = partner_name


p1 = Person('lava', 27, 'reddyrani')

p2 = Person('reddyrani', 24, 'lavakumar')

print(p1.name)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(abc):
        print('hello my name is ' + abc.name)


p1 = Person('lava', 27)
p1.hello()

p1.age = 25

print(p1.age)



Create a class named Person,
with firstname and lastname properties
and a printname method:



class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


x = Student('reddy', 'rani')

x.printname()



def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


num = 6

print('factorial of num', num, 'is', factorial(num))



def simple_intrest(p, t, r):
    print('the principal is', p)
    print('the time is', t)
    print('the rate of intrest is', r)

    si = (p * t * r)/100

    print('the simple intrest is', si)
    return si
 simple_intrest(3000,7,1)



def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si


# Driver code
simple_interest(8, 6, 8)



def compound_interest(principle, rate, time):

    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)


# Driver Code
compound_interest(10000, 10.25, 5)

start = 1
end = 100

for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)


start = 2
end = 100
for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
    else:

        print(i)


start = 1
end = 100

for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
    else:
        print(i)

num = int(input('enter a number'))

if num > 1:
    for i in range(2, num):
        if(num % i == 0):
            print(num, ' is not a prime')
            break
        else:
            print(num, ' is a prime')
            break
else:
    print(num, ' is not a prime')



def fibonacci(n):
    if n < 0:
        print('incorrect input')
    elif(n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


print(fibonacci(int(input('enter a num : '))))




def is_palindrome(s):
    return s == s[:: -1]


s = input('enter a word : ')

ans = is_palindrome(s)

if ans:
    print('yes')
else:
    print('no')


import numpy

a = numpy.array([1, 2, 3, 4])

b = numpy.append(a, [5])
print(b)


a = int(input('Enter the first num : '))
op = input('Enter the operator : ')
b = int(input('Enter the second num : '))


def add(a, b):
    result = a + b
    print(result)


def sub(a, b):
    result = a-b
    print(result)


def mul(a, b):
    result = a*b
    print(result)


def div(a, b):
    result = a/b
    print(result)


if op == '+':
    add(a, b)
elif op == '-':
    sub(a, b)
elif op == '*':
    mul(a, b)
elif op == '/':
    div(a, b)
else:
    print('enter a valid num')

n = int(input('enter the number of rows'))
for i in range(n):
    print('*' * n)

a = input('enter a string')
count = 0
for i in a:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):

        count = count+1
print(count)


sentence = input('Enter a sentence : ')
a = sentence.lower()
count = 0
for i in a:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count = count + 1
        print(i)
print('there are ', count, ' vowels in', sentence)



year = int(input('Enter a year'))
if((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print(year, ' is a leap year')
else:
    print(year, ' not aleap year')


number = int(input('Enter any number : '))
rev_num = 0
while number > 0:
    n = number % 10
    rev_num = rev_num * 10 + n
    number = number // 10
print('the reversed num is ', rev_num)

width = float(input('enter width : '))
height = float(input('enter height: '))

area = width * height
perimeter = 2*(width + height)

print('area of a rectangle', area)
print('perimeter of a rectangle', perimeter)

my_list = [10, 5, 3, 9, 6, 1, 2]

print('my list before reverse', my_list)

my_list.reverse()

print('my list after reverse', my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('my list before reverse', my_list)

rev_list = my_list[:: -1]

print('reversed list is', rev_list)

a = 8
b = 9

a, b = b, a
print(a, b)

a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9, 10]

a, b = b, a

print(a, b)

string = input('enter a string : ')

if (string == string[:: -1]):
    print(string, ' is a palindrome')
else:
    print(string, ' is not a palindrome')

# fibonacci number


def fibonacci(n):
    if n == 0:
        print('Invalid input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(9))



def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))



def fibonacci(n):
    if n == 0:
        print('Invalid input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(9))



def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(6))

a = float(input('enter any num : '))
op = input('enter operator : ')
b = float(input('enter a number :'))


def add(a, b):
    result = a+b
    print(result)


def sub(a, b):
    result = a - b
    print(result)


def mul(a, b):
    result = a*b
    print(result)


def div(a, b):
    result = a/b
    print(result)


try:
    if op == '+':
        add(a, b)
    elif op == '-':
        sub(a, b)
    elif op == '*':
        mul(a, b)
    elif op == '/':
        div(a, b)
except:
    print('invalid input')

sentence = input('Enter any sentence : ')
string = sentence.lower()
count = 0

for i in string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count = count+1
        print(print('The vowels in ', sentence, ' is ', i))

year = int(input('enter any year : '))

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print(year, ' is a aleap year')
else:
    print(year, ' is not a leap year')

num = int(input('Enter a number : '))
rev = 0
while num > 0:
    a = num % 10
    rev = rev * 10 + a
    num = num // 10
print(rev)

string = input('enter a string')

reversed_string = string[:: -1]

print('string before reversed', string)

print('string after reversed ', reversed_string)

p = int(input('enter the principle : '))
t = int(input('enter the time : '))
r = int(input('enter the rate of intrest : '))

si = (p * t * r) / 100

print('the simple intrest is ', si)

p = float(input('enter principle amount'))
t = float(input('enter time span'))
r = float(input('enter rate of intrest'))

a = p * (pow((1+r/100), t))

ci = a - p

print('the compoundintrest is ', ci)

num = int(input('enter a num'))

if num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print(num, ' is not a not a prime')
            break
        else:
            print(num, ' is a prime')
else:
    print(num, ' is not a prime')




num = int(input('enter a num : '))
if num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print('not aprime')
            break
        else:
            print('prime')
            break
else:
    print('not aprime')

start = 1
end = 100
for num in range(start, end):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
    else:
        print(num)

list = [1, 2, 3, 4, 5, 6]
list2 = list[:: -1]
print(list2)
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))



def check_num(n):
    if n < 0:
        return('the number is nagative')
    elif n == 0:
        return('the num is zero')
    else:
        return('num is positive')


n = int(input('enter a number'))
print(check_num(n))

a = int(input('Enter first num : '))
op = input('Enter operator')
b = int(input('Enter second num : '))


def add(a, b):
    print(a+b)


def sub(a, b):
    print(a-b)


def mul(a, b):
    print(a*b)


def div(a, b):
    print(a/b)


if op == '+':
    add(a, b)
if op == '-':
    sub(a, b)
if op == '*':
    mul(a, b)
if op == '/':
    div(a, b)

b = float(input('enter the base of triangle : '))
h = float(input('enter the height of the triangle : '))

area = 1/2 * (b*h)

print('the area of triangle is ', area)

a = 2
b = 3
a, b = b, a
print(a, b)

import random
a = int(input('enter a num'))
b = int(input('enter b num'))

c = random.randint(a, b)
print(c)

km = int(input('enter kilometer'))

mile = km * 0.621371

print(mile)

celsius = float(input('enter celsius : '))

fahrenheit = (celsius * 9/5)+32
print(fahrenheit)

num = int(input('Enter a number : '))
if (num == 0 or num % 2 == 0):
    print(num, ' is even')
else:
    print(num, ' is odd')

year = int(input('Enter a year : '))
if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
    print(year, ' is aleap year')
else:
    print(year, 'is not aleap year')

num = int(input('Enter a number : '))

if num > 0:
    for i in range(2, num):
        if (num % i == 0):
            print('not prime')
            break
        else:
            print('prime')
            break
else:
    print('not prime')

start = int(input('Enter a num : '))
end = int(input('Enter a num : '))
for num in range(start, end):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
            else:
                print(num)


n = int(input('Enter a input: '))


def factorial(n):
    if n == 0:
        print('Invalid input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return factorial(n-1) + factorial(n-2)


print(factorial(n))

num = int(input('Enter a value : '))
for i in range(1, 21):
    print(num, 'x', i, '=', num*i)

n = int(input('Enter a num : '))


def fibonacci(n):
    if n == 0:
        print('Invalid input!!!')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(n))

n = int(input('Enter a num : '))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(n))

a = float(input('Enter a num : '))
op = input('Enter a operator : ')
b = float(input('Enter a num : '))


def add(a, b):
    result = a+b
    print(result)


def sub(a, b):
    result = a-b
    print(result)


def mul(a, b):
    result = a*b
    print(result)


def div(a, b):
    result = a/b
    print(result)


if op == '+':
    add(a, b)
elif op == '-':
    sub(a, b)
elif op == '*':
    mul(a, b)
elif op == '/':
    div(a, b)
else:
    print('Invalid input')

sentence = input('Enter a sentence : ')
string = sentence.lower()

for i in string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        print(i)
    else:
        print('There are no vowles in the sentence')
        break

sentence = input('Enter a sentence : ')
string = sentence.lower()
count = 0
for i in string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count = count+1
print(count)

year = int(input('Enter any year : '))
if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print(year, ' is a leap year')
else:
    print(year, ' is not a leap year')

num = 123456
rev = 0
while num > 0:
    a = num % 10
    rev = rev * 10 + a
    num = num // 10
print(rev)

string = input('Enter a string : ')
rev_string = string[:: -1]
print('The string before reversed ', string)
print('The string after reversed ', rev_string)

p = float(input('principle'))
t = float(input('time'))
r = float(input('rate of intrest'))
si = (p*t*r)/100

print('simple intrest is ', si)

num = int(input("Enter a num : "))
if num > 1:
    for i in range(2, num):
        if(num % i == 0):
            print('not a prime')
            break
        else:
            print('prime')
            break
else:
    print('not a prime')

start = 1
end = 100
for num in range(start, end):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
            else:
                print(num)
                break
dec = int(input('Enter a decimal num : '))

print(bin(dec), ' in binary')

print(oct(dec), ' is octal')

print(hex(dec), ' is hex')

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = arr1
print(arr2)

a = 10
b = 2
print(a**b)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Person('lava', 26)
print(a.name)

import numpy as np
a = np.array(24)
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[9, 8, 7], [6, 5, 4]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)

import numpy as np
arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr.ndim)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])

a = "Hello  world  "

print(a.upper())
print(a.lower())
print(a.strip())
print(a.split(','))

thislist = ["apple", "banana", "cherry"]
newlist = ["lava", "kumar", "reddy"]
thislist.extend(newlist)
print(thislist)
"""
i = 1
while i < 6:
    print(i)
    i = i + 1
    if i == 3:
        break

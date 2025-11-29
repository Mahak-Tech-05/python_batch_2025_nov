#main.py
from packages import add

print(add(10,5))

print('----------------------------------------')
#importing all functions togther
from packages import *

print(add(4,5))
print(sub(3,2))
print(reverse('Welcome'))

print('------------------------------------------')
#taking input form users
a = int(input('Enter first value:'))
b = int(input('Enter second value:'))
s = input("Enter text to inverse it")

print(sub(a,b))
print(add(a,b))
print(reverse(s))

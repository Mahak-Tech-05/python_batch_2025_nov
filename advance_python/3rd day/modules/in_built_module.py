#in built module
#math module
import math
num = 20
print('Square root:', math.sqrt(num))
print("Value of pi:", math.pi)
print("factorial of 5:",math.factorial(5))

print('----------------------------------------------------')

#calling many modules togther in one line
import math , random
num = random.randint(1,50)
print("Randome number:",num)
print("Square root:", math.sqrt(num))

# here we call all the function of module file togther
from cal_part_one import *
# here we call one by one all the functions
from cal_part_two import mul
from cal_part_two import div

f = int(input("Enter the value :"))
s = int(input("Enter the secoond value : "))


add(f,s)
result = sub(f,s)
print("The subtraction of both the number is:",result)
mul(f,s)
result = div(f,s)
print("The divsion of both the number is:" , result)

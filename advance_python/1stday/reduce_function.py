#lambda resuce function
from functools import reduce
num = [1,2,3,4]
total = reduce(lambda a,b : a+b , num)
print(total)

#nested lambda
mul = lambda a :lambda b: a*b
result=mul(4)(3)
print(result)

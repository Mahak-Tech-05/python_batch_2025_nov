#lambda function with map()
nums = [1,2,3,4]
square = list(map(lambda x : x*x, nums))
print(square)


#user input
n = list(map(int , input('Enter the values:').split()))
d = list(map(lambda x:x*2,n))
print('Orignal series:',n)
print('Double:',d)

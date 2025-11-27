#lambda function for filter()
nums = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x : x%2 == 0 , nums))
print(even)

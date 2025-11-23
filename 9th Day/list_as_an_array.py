#python list as an array (dynamic array )
#creating a list(act as a dynamic array)
number = [10,20,30,"Hii",50]
print("Original List:", number)

#Accessing elements
print("First element:", number[0])

#modifying elements
number[1] = 200
print("After Modification:", number)

# adding elements
number.append(60)
print("After append:", number)

# removing element
number.pop(2)
print("After poping the element:", number)

#loop thorught list
print("Loopinh through array")
for num in number:
    print (num)

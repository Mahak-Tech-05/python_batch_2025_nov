#array module(traditional fixed type array)
from array import array
#creating an integer array( 'i' means int)
arr = array('i',[1,2,3,4,5])
print("Original array:", arr)

#Accessing elements
print("Elements at index at 4:", arr[4])

#adding a element
arr.append(6)
print("After append:", arr)

arr.insert(4,13)
print("After insertion:" , arr)

arr.remove(3)
print("Afte removing:", arr)

print

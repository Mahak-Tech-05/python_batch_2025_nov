#try an except code
try:
    age = int(input("Enter the age:"))
    print(age)
except ValueError:
    print("Please enter only in digits")
    

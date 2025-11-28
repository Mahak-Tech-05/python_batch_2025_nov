#this is the programme in which we don't know the name of error
try:
    x = int(input("Enter something:"))
    y = 10/x
    print(y)
except Exception as e:
    print("Some error occured",e)

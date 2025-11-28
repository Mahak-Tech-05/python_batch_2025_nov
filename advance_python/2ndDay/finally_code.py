#finally block
try:
    x = 10/5
except ZeroDivisionError:
    print("You cannot divide by 0")
finally:
    print("This will always")

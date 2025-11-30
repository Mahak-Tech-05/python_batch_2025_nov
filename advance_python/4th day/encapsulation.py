#encapsulation code
class student:
    __marks=0 #private variable

    def set_marks(self ,m):
        if m>= 0 and m <=100:
            self.__marks = m
        else:
            print('Invalid marks!')

    def get_marks(self):
        return self.__marks

#using class
s = student()

s.set_marks(65) #setting value
print("Marks:",s.get_marks())#accessing value safety

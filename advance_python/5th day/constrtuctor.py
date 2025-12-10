#constrctor code
class student:
    #constructor
    def __init__(self , name , age):
        #setting first values
        self.name = name
        self.age = age

    def show(self):
        print('Name:',self.name)
        print('Age:',self.age)

#create object
name = input('enter youre name:')
age = int(input('Enter youre age:'))
s1 = student(name , age)
s1.show()

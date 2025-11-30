class Student:
    name = ""
    roll = 0
    def show(self):#method
        print("Name:", self.name)
        print("Roll:", self.roll)
#create object
s1 = Student()

#assign values
s1.name = "Ramlal"
s1.roll = 101

#call method
s1.show()

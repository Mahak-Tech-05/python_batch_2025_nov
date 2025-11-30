#inheritance code
#parent class
class animal:
    def sound(self):
        print("Animals make sound:")

#child class
class dog(animal):
    pass

#create object of child class
d=dog()
d.sound()#calling method from parent class

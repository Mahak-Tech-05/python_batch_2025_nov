#abstraction code
#importing abc module for abstraction
from abc import ABC , abstractmethod

#abstract class
class shape(ABC):

    @abstractmethod
    def area(self):
        pass # only the idea , no details

#child class
class circle(shape):
    #this is constructor used to store radius inside the object
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius* self.radius

#child class
class square(shape):
    def __init__ (self , side):
        self.side = side

    def area(self):
        return self.side * self.side

#using the classes
c = circle(5)
s = square(4)

print("Circle area :", c.area())
print("Square area :", s.area())

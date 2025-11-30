#polymorsphism inherutance(method overrirding)
#parent class
class shape:
    def area(self):
        return 0
#child class 
class square(shape):
    # when you create a square, so you can store its side length
    def __init__(self , side):
        self.side = side

    def area(self):
        return self.side * self.side
    #formula :- side * side
#child class of shape 
class circle(shape):
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

s = square(5)
c = circle(3)
print('Square area',s.area())
print('circle area',c.area())

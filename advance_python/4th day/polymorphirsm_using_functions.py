#1st type
#polymorphism using functions
class dog:
    def sound(self):
        return "Barks"
class cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

d = dog()
c = cat()

animal_sound(d)
animal_sound(c)

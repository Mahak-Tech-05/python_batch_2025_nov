#method code
class phone:
    def calls(self):
        print('Calling someone')

    def click_photo(self):
        print('clcicking a photo')

#creating object of phone
m = phone()

#using methods
m.calls()
m.click_photo()


#types of methods
#1st type instance method
class car :
    def __init__(self , brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand}Car is starting')

    def honk(self):
        print(f'{self.brand}Car is honking')

#creating object
car1 = car("honda")
car2 = car("lambo")

#calling instnce methods
car1.start()
car1.honk()

car2.start()
car2.honk()


#2nd type class method
class school:
    total_students = 100 #class attributes
    
    @classmethod
    def show_total_students(cls):
    	print(f'Total students in schoool: {cls.total_students}')
#calling class method
school.show_total_students()


#3rd static method
class caculator:
	@staticmethod
	def add(a , b):
		return a+b
	
	@staticmethod
	def mul(a , b):
		return a*b

#using static methods

print(caculator.add(5 , 4))
print(caculator.mul(5 , 6))
	
	

class person:
    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print('Hello , my name is:',self.name)

p = person('ramlal')
p.say_hello()

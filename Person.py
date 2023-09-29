class Persons:
    def __init__(self, name, age):
        self.n = name
        self.a = age
    
    def show(self):
        print(f'{self.n} is {self.a} years old.')
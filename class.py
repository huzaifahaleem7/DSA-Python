class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
        
    def age_inrement(self):
        self.age += 10
        print(f"After 10 years, I will be {self.age} years old")
        
p1 = Person("Ajmal", 30)
p2 = Person("Huzaifa", 24)
p3 = Person("Hamza", 22)


p1.greet()
p2.greet()
p3.greet()

p1.age_inrement()
p2.age_inrement()
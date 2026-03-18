class Animal:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name
    def voice(self):
        return "????????"
    
    def __str__(self):
        return f"{self.name} is a {self.gender} animal"
    
class Dog(Animal):

    def __init__(self, name, gender, age, breed):
        super().__init__(name, gender, age)
        self.breed = breed
    def voice(self):
        return "Woof!"
    
    def eat(self):
        return "Dog is eating."


class Cat(Animal):
    
    def __init__(self, name, gender, age, color):
        super().__init__(name, gender, age)
        self.color = color
    def voice(self):
        return "Meow!"
    def sleep(self):
        return "Cat is sleeping."
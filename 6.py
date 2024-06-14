class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Bark"

my_dog = Dog(name="Buddy", breed="Golden Retriever")
print(my_dog.name)
print(my_dog.species)
print(my_dog.make_sound())

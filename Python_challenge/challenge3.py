# Using the OOP features inheritance, create a class Animal with the method sound()
# and then create a cat and dog class that inherits from the animal class.
# the cat and dog class should override the sound class and print a different sound

class Animal:
    sound1 = "moo"
    sound2 = "baa"
    sound3 = "cluck"

    def print_animal_info(self):
        print("\nAnimal {", self.sound1, ",", self.sound2 + " }")


class Cat(Animal):
    sound = "meow"

    def __init__(self, sound1, sound2):
        self.sound1 = sound1
        self.sound2 = sound2


class Dog(Animal):
    sound = "woof"

    def __init__(self, sound1, sound2):
        self.sound1 = sound1
        self.sound2 = sound2


dog1 = Dog("woof", "yin")
dog1.print_animal_info()

cat1 = Cat("meow", "hmm")
cat1.print_animal_info()

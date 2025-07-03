# Function (Reusable logic)
def introduce_animal(animal):
    print(f"This is a {animal.__class__.__name__}. It says: {animal.speak()}")

# Base Class (Shows Encapsulation and Abstraction)
class Animal:
    def __init__(self, name):
        self.__name = name  # Encapsulated (private attribute)

    def get_name(self):
        return self.__name

    def speak(self):  # To be overridden (Polymorphism)
        return "Some generic animal sound"

# Derived Classes (Inheritance + Polymorphism)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed  # Encapsulation

    def get_breed(self):
        return self.__breed

    def speak(self):  # Polymorphism in action
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Polymorphism
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Main program logic
def main():
    # Creating objects (instances of classes)
    dog = Dog("Rex", "Labrador")
    cat = Cat("Whiskers")
    bird = Bird("Chirpy")

    # Using polymorphism with function
    for animal in [dog, cat, bird]:
        introduce_animal(animal)
        print(f"Name: {animal.get_name()}")
        print("---")

# Run the program
if __name__ == "__main__":
    main()

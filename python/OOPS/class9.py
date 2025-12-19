## Polymorphism

## Method Overriding - allows a child class to provide an implementation to a method already defined in Parent class

# Base Class

class Animal:
    def speak(self):
        return "Woof"
    

class Dog(Animal):
    def speak(self):
        return "Loud Woof"
    

dog=Dog()
print(dog.speak())
dog=Animal()
print(dog.speak())


def animal_speak(animal):
    print(animal.speak())


animal_speak(Animal())
animal_speak(Dog())


## Polymorphism with Function and Methods

class Shape:
    def area(self):
        return "The area of the figure"


class Rect(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
        return self.width*self.height


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius ** 2
    

## Function that demonstrates polymorphism

def print_area(shape):
    print(f'The area is {shape.area()}')


rect=Rect(4,5)
circ=Circle(3)

print_area(rect)
print_area(circ)


## Interfaces in python is abstract base class



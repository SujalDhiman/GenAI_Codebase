## OOPS

## Instance Variables and Methods

class Dog:
    ## constructor helps in initializing instance variables
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # instance method
    def bark(self):
        print(f'{self.name} says woof')

    ## self refers to current object


dog1 = Dog("Harry",3)

dog1.bark()

dog2 = Dog("Limcee",4)

dog2.bark()













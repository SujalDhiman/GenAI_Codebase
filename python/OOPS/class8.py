## Inheritance in Python

class Car:
    
    def __init__(self,windows,doors,engineType):
        self.windows=windows
        self.doors=doors
        self.engineType=engineType

    def drive(self):
        print(f"The person will drive the {self.engineType} car ")


# inheritance syntax
class Tesla(Car):
    def __init__(self,windows,doors,engineType,isSelfDriving):
        super().__init__(windows,doors,engineType)
        self.isSelfDriving=isSelfDriving

    
    def selfDriving(self):
        print(f'Tesla Supports {self.isSelfDriving} Mode')


car1=Tesla(4,5,"electric",True)

car1.selfDriving()



## Multiple Inheritance

class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Subclass must implement this method")


class Pet:
    def __init__(self,owner):
        self.owner=owner


# Multiple Inheritance
class Dog(Animal,Pet):
    
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)



    
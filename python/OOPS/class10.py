## Encapsulation with Getter and Setter Method

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age  # public variables


person=Person("Sujal",21)

print(person.age)

print(dir(person)) # important give other hidden methods names as well



class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age  # private variables


person=Person("Sujal",21)

print(person.__age) # can't access now
print(dir(person)) # here you will not see name and age now bcuz they are private now


class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age  # protected variables


# protected variables - cannot access outside the class but can access from derived class object


## getters and setters

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    # getter
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name
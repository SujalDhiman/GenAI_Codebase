## self argument in python

class Chaicup:
    size=150 #ml
    
    def describe(self):
        return f'A {self.size}ml chai cup'
    

cup = Chaicup()

print(cup.describe()) # the self has the context here of this object

print(Chaicup.describe(cup)) # when the class calls it, the context has to be provided externally

cup_two = Chaicup()
cup_two.size=100
print(cup_two.describe())
print(Chaicup.describe(cup_two))
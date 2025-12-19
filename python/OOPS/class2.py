## Class and Object Namespace

class Chai:
    origin="India"

print(Chai.origin)

Chai.is_hot=True

print(Chai.is_hot)

# creating objects from chai class

masala=Chai()

masala.is_hot=False

print(f'{masala.origin}')
print(f'{masala.is_hot}')

masala.country="India"
## Objects can have their own unique properties


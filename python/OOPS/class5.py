## Constructors and init in Python

class ChaiOrder:
    
    def __init__(self,type_,size):
        self.type = type_ # type_ because its a keyword
        self.size = size
    
    def summary(self):
        return f'{self.size}ml of {self.type} chai'
    
order = ChaiOrder("Masala",200)

print(order.summary())

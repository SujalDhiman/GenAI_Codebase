## Inheritance and Composition

class BaseChai:

    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f'Preparing {self.type} chai...')


class MasalaChai(BaseChai): # inheritance syntax
    def add_spices(self):
        print("Adding cardamom, ginger and cloves")



import copy

class Composition():
    def __init__(self, product, quantity):
        self.__product = copy.copy(product)
        self.__quantity = quantity

    @property
    def get_product(self):
        return self.__product

    
    def set_product(self, p):
        self.__product = p

    @property
    def get_quantity(self):
        return self.__quantity

    
    def set_quantity(self, q):
        self.__quantity = q

    def __str__(self):
        return f"\nComposition:{str(self.get_product)} \n- Quantity: {self.get_quantity}"

    def __eq__(self, other):
        return self.get_product == other.get_product and self.get_quantity == other.get_quantity

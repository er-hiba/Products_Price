from Product import Product

class Elementary(Product):
    def __init__(self, name, code, purchase_price):
        super().__init__(name, code)
        self.__purchase_price = purchase_price

    @property
    def get_price(self):
        return self.__purchase_price

    def __str__(self):
        return f"- {self.get_name}, Code: {self.get_code}, Purchase Price: {self.get_price}"

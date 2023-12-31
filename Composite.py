from Product import Product

class Composite(Product):
    def __init__(self, name, code, man_cost, constituents, vat_rate=0.18):
        super().__init__(name, code)
        self.__man_cost = man_cost
        self.vat_rate = vat_rate
        self.__constituents = constituents

    @property
    def get_man_cost(self):
        return self.__man_cost

    @property
    def get_constituents(self):
        return self.__constituents

    def get_price(self):
        total = sum(x.get_product.get_price for x in self.__constituents)
        total += self.get_man_cost 
        return total

    def __str__(self):
        constituents_info = " ".join(f"{elem}" for elem in self.get_constituents)
        return f"- {self.get_name}\n- Code: {self.get_code}\
\n- Manufacturing Cost: {self.get_man_cost}\n- Constituents:{constituents_info}- Purchase Price: {self.get_price()}"

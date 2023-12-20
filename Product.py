from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    @property
    def get_name(self):
        return self.__name

    
    def set_name(self, n):
        self.__name = n

    @property
    def get_code(self):
        return self.__code

    
    def set_code(self, c):
        self.__code = c

    @abstractmethod
    def get_price(self):
        pass

    def __str__(self):
        return f"Product: \n- Name: {self.__name} \n- Code: {self.__code}"

    def __eq__(self, other):
        return self.get_code == other.get_code

class Product:
    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount

    def get_product_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_amount(self):
        return self.__amount

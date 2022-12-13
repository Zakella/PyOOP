from src.data.Product import Product


class Beauty(Product):

    def __init__(self, name, price, amount, color):
        super().__init__(name, price, amount)
        self.__color = color

    @property
    def get_color(self):
        return self.__color

    def __str__(self):
        return f"Mist: {super().get_product_name()}, price: {super().get_price()}, amount: {super().get_amount()}, " \
               f"size: {self.get_color} "


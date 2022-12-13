from src.data.Product import Product


class Bras(Product):

    def __init__(self, name, price, amount, size):
        super().__init__(name, price, amount)
        self.size = size

    @property
    def get_size(self):
        return self.size

    def __str__(self):
        return f"Bras: {super().get_product_name()}, price: {super().get_price()}, amount: {super().get_amount()}, " \
               f"size: {self.get_size} "

from src.data.Busket import Busket


class BusketSerivice:
    def __init__(self):
        self.basket = Busket()

    def put_products_in_basket(self, product):
        basket_list = self.basket.get_busket_list()
        basket_list.append(product)
        a = 1

    def get_basket_products(self):
        return self.basket.get_busket_list()

    def calculate_products(self):
        bs_list = self.basket.get_busket_list()
        total = 0
        for item in bs_list:
            total += item.get_price() * item.get_amount()

        return total


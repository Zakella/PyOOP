from src.service.BusketSerivice import BusketSerivice as bs


class Console:

    def __init__(self):
        self.bs = bs()

    def show_products_in_basket(self):
        for item in self.bs.get_basket_products():
            print(item)

    def show_total_summ(self, value):
        print(f'Total in basket {value}')

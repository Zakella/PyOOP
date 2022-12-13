import src.service.ProductService as PS
from src.service.BusketSerivice import BusketSerivice
from src.view.Console import Console


class Controller:
    def __init__(self):
        self.busket_service = BusketSerivice()
        self.console = Console()

    def put_product(self, product):
        self.busket_service.put_products_in_basket(product)

    def show_products_in_basket(self):
        self.console.show_products_in_basket()

    def calculate_products(self):
        self.console.show_total_summ(self.busket_service.calculate_products())

    def delete_proudct(self):
        pass

    def update_product(self):
        pass


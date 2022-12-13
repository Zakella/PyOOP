from src.controller.Controller import Controller
from src.data.Bras import Bras
from src.data.Beauty import Beauty
from src.data.Busket import Busket

if __name__ == '__main__':
    controller = Controller()
    controller.put_product(Bras("Victoria Secret", 100, 1, "3S"))
    controller.put_product(Bras("Armani", 200, 2, "4S"))
    controller.put_product(Bras("Gucci", 500, 1, "2M"))
    controller.put_product(Beauty("Jovvani", 350, 1, "red"))
    controller.put_product(Beauty("Mirage", 50, 1, "blue"))
    controller.show_products_in_basket()
    controller.calculate_products()

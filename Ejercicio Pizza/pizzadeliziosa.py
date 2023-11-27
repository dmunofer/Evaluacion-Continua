from pizzabuilder import PizzaBuilder
from pizza import Pizza
from composite import MenuItem

class PizzaDeliziosoBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
        self.menu_item = MenuItem("Pizza Delizioso", 10.99)  # Precio base de la pizza

    # Métodos de construcción de pizza existentes

    def build_menu_item(self) -> MenuItem:
        return self.menu_item
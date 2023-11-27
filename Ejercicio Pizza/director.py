# Director
from pizzabuilder import PizzaBuilder
from composite import MenuComposite

class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder
        self.menu = MenuComposite("Menú Personalizado")

    def construir_pizza(self):
        pizza = self.builder.get_pizza()
        menu_item = self.builder.build_menu_item()
        self.menu.add_item(menu_item)

from abc import ABC, abstractmethod

class MenuComponent(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

class MenuComposite(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.menu_items = []

    def add_item(self, item: MenuComponent):
        self.menu_items.append(item)

    def remove_item(self, item: MenuComponent):
        self.menu_items.remove(item)

    def get_price(self) -> float:
        total_price = 0
        for item in self.menu_items:
            total_price += item.get_price()
        return total_price
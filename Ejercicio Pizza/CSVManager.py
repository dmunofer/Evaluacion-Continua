# CSV Manager
import csv
from pizza import Pizz
from composite import *

class CSVManager:
    @staticmethod
    def save_to_csv(menu_component: MenuComponent):
        with open('menus.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            details = [(item.name, item.get_price()) for item in menu_component.menu_items]
            csv_writer.writerows(details)

    @staticmethod
    def read_from_csv():
        menu_items = []
        with open('menus.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                menu_item = MenuItem(row[0], float(row[1]))
                menu_items.append(menu_item)
        return menu_items
from composite import MenuItem, MenuComposite
from pizzadeliziosa import PizzaDeliziosoBuilder
from director import PizzaDirector
from CSVManager import CSVManager

def mostrar_detalles_pizza(pizza):
    print("Detalles de la pizza personalizada:")
    print(f"Tipo de masa: {pizza.tipo_masa}")
    print(f"Salsa: {pizza.salsa}")
    print(f"Ingredientes principales: {', '.join(pizza.ingredientes_principales)}")
    print(f"Técnicas de cocción: {pizza.tecnicas_coccion}")
    print(f"Presentación: {pizza.presentacion}")
    print(f"Maridaje recomendado: {pizza.maridaje_recomendado}")

def main():
    # Uso del patrón Builder con validación de elecciones
    builder_delizioso = PizzaDeliziosoBuilder()
    director = PizzaDirector(builder_delizioso)
    director.construir_pizza()
    pizza_personalizada = builder_delizioso.get_pizza()

    # Crear elementos (pizzas, bebidas, etc.)
    pizza_margarita = MenuItem("Pizza Margarita", 10)
    pizza_hawaiana = MenuItem("Pizza Hawaiana", 12)
    cocacola = MenuItem("Coca Cola", 2)

    # Crear menús compuestos
    menu_pizza = MenuComposite("Menú Pizza")
    menu_pizza.add_component(pizza_margarita)
    menu_pizza.add_component(pizza_hawaiana)

    menu_completo = MenuComposite("Menú Completo")
    menu_completo.add_component(menu_pizza)
    menu_completo.add_component(cocacola)

    # Calcular precios
    price_pizza = pizza_personalizada.get_price()
    price_menu_pizza = menu_pizza.get_price()
    price_menu_completo = menu_completo.get_price()

    # Muestra los detalles de la pizza personalizada
    mostrar_detalles_pizza(pizza_personalizada)

    # Muestra los precios de los elementos y menús
    print(f"Precio Pizza Personalizada: ${price_pizza}")
    print(f"Precio Menú Pizza: ${price_menu_pizza}")
    print(f"Precio Menú Completo: ${price_menu_completo}")

    # Guarda la pizza personalizada en un archivo CSV
    CSVManager.save_to_csv(pizza_personalizada)

if __name__ == "__main__":
    main()
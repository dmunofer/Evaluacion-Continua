from pizzadeliziosa import PizzaDeliziosoBuilder
from director import PizzaDirector
from CSVManager import CSVManager

def mostrar_detalles_pizza(pizza)
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

    # Muestra los detalles de la pizza personalizada
    mostrar_detalles_pizza(pizza_personalizada)

    # Guarda la pizza personalizada en un archivo CSV
    csv_writer = PizzaDirector("pizzas_personalizadas.csv")
    csv_writer.write_pizza_to_csv(pizza_personalizada)

if __name__ == "__main__":
    main()

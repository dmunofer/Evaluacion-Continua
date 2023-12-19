from typing import List

# Clase para representar un producto en el menú
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Clase para representar un menú personalizado con maridajes y productos de socios
class MenuPersonalizado:
    def __init__(self):
        self.productos_delizioso: List[Producto] = []
        self.maridajes_recomendados: List[str] = []
        self.productos_socios: List[Producto] = []

    def agregar_producto_delizioso(self, producto: Producto):
        self.productos_delizioso.append(producto)

    def agregar_maridaje_recomendado(self, maridaje: str):
        self.maridajes_recomendados.append(maridaje)

    def agregar_producto_socio(self, producto: Producto):
        self.productos_socios.append(producto)

# Función para calcular el precio final del menú
def calcular_precio_final(menu: MenuPersonalizado):
    precio_total = sum(producto.precio for producto in menu.productos_delizioso + menu.productos_socios)
    return precio_total

# Ejemplo de uso para la pizzería Delizioso con Menús Personalizados
if __name__ == "__main__":
    # Crear un menú personalizado
    menu_cliente = MenuPersonalizado()

    # Agregar productos delizioso al menú
    pizza_margarita = Producto("Pizza Margarita", 12.0)
    ensalada_ceasar = Producto("Ensalada César", 8.0)
    menu_cliente.agregar_producto_delizioso(pizza_margarita)
    menu_cliente.agregar_producto_delizioso(ensalada_ceasar)

    # Agregar maridajes recomendados
    menu_cliente.agregar_maridaje_recomendado("Vino Blanco para la Pizza Margarita")

    # Agregar productos de socios al menú
    vino_tinto = Producto("Vino Tinto Reserva", 18.0)
    cerveza_artesanal = Producto("Cerveza Artesanal IPA", 5.0)
    postre_tiramisu = Producto("Tiramisú", 6.0)
    menu_cliente.agregar_producto_socio(vino_tinto)
    menu_cliente.agregar_producto_socio(cerveza_artesanal)
    menu_cliente.agregar_producto_socio(postre_tiramisu)

    # Calcular el precio final del menú
    precio_final = calcular_precio_final(menu_cliente)

    # Mostrar el menú al cliente
    print("=== Menú Personalizado ===")
    print("Productos de Delizioso:")
    for producto in menu_cliente.productos_delizioso:
        print(f"- {producto.nombre}: ${producto.precio:.2f}")

    print("\nMaridajes Recomendados:")
    for maridaje in menu_cliente.maridajes_recomendados:
        print(f"- {maridaje}")

    print("\nProductos de Socios:")
    for producto in menu_cliente.productos_socios:
        print(f"- {producto.nombre}: ${producto.precio:.2f}")

    print("\nPrecio Final: ${:.2f}".format(precio_final))

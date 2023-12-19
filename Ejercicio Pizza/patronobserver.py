from abc import ABC, abstractmethod
from typing import List

# Observador
class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass

# Sujeto (Notificador)
class Notificador:
    def __init__(self):
        self._observadores: List[Observador] = []

    def agregar_observador(self, observador: Observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def quitar_observador(self, observador: Observador):
        self._observadores.remove(observador)

    def notificar(self, mensaje: str):
        for observador in self._observadores:
            observador.actualizar(mensaje)

# Evento de Nuevos Sabores de Pizza
class EventoNuevosSabores(Observador):
    def actualizar(self, mensaje: str):
        print(f"Notificación de Nuevos Sabores: {mensaje}")

# Evento de Promociones en Pizzas
class EventoPromocionesPizzas(Observador):
    def actualizar(self, mensaje: str):
        print(f"Notificación de Promociones en Pizzas: {mensaje}")

# Evento de Nuevos Productos de Alianzas Estratégicas
class EventoNuevosProductosAlianzas(Observador):
    def actualizar(self, mensaje: str):
        print(f"Notificación de Nuevos Productos de Alianzas Estratégicas: {mensaje}")

# Interfaz para los Socios Estratégicos
class SocioEstrategico(ABC):
    @abstractmethod
    def actualizar_producto(self, nombre_producto: str, disponibilidad: bool, descripcion: str):
        pass

# Implementación de un Socio Estratégico de Vinos
class SocioVinos(SocioEstrategico):
    def actualizar_producto(self, nombre_producto: str, disponibilidad: bool, descripcion: str):
        print(f"Actualización de Vinos por el socio estratégico: {nombre_producto} - Disponibilidad: {disponibilidad}, Descripción: {descripcion}")

# Implementación de un Socio Estratégico de Cervezas
class SocioCervezas(SocioEstrategico):
    def actualizar_producto(self, nombre_producto: str, disponibilidad: bool, descripcion: str):
        print(f"Actualización de Cervezas por el socio estratégico: {nombre_producto} - Disponibilidad: {disponibilidad}, Descripción: {descripcion}")

# Implementación de un Socio Estratégico de Postres
class SocioPostres(SocioEstrategico):
    def actualizar_producto(self, nombre_producto: str, disponibilidad: bool, descripcion: str):
        print(f"Actualización de Postres por el socio estratégico: {nombre_producto} - Disponibilidad: {disponibilidad}, Descripción: {descripcion}")

# Ejemplo de uso para la pizzería Delizioso con Alianzas Estratégicas
if __name__ == "__main__":
    # Crear instancias de los eventos (observadores)
    evento_nuevos_sabores = EventoNuevosSabores()
    evento_promociones_pizzas = EventoPromocionesPizzas()
    evento_nuevos_productos_alianzas = EventoNuevosProductosAlianzas()

    # Crear el notificador (sujeto)
    notificador = Notificador()

    # Agregar observadores al notificador
    notificador.agregar_observador(evento_nuevos_sabores)
    notificador.agregar_observador(evento_promociones_pizzas)
    notificador.agregar_observador(evento_nuevos_productos_alianzas)

    # Introducir un nuevo sabor de pizza y notificar a los observadores
    nuevo_sabor = "Pizza de Pollo BBQ"
    notificador.notificar(f"Nuevo sabor de pizza disponible: {nuevo_sabor}")

    # Introducir una nueva promoción en pizzas y notificar a los observadores
    nueva_promocion_pizzas = "Descuento del 20% en todas las pizzas medianas"
    notificador.notificar(f"Nueva promoción en pizzas: {nueva_promocion_pizzas}")

    # Crear instancias de los socios estratégicos
    socio_vinos = SocioVinos()
    socio_cervezas = SocioCervezas()
    socio_postres = SocioPostres()

    # Agregar socios estratégicos como observadores para los productos de alianzas
    notificador.agregar_observador(socio_vinos)
    notificador.agregar_observador(socio_cervezas)
    notificador.agregar_observador(socio_postres)

    # Actualizar productos de los socios estratégicos
    socio_vinos.actualizar_producto("Vino Tinto Reserva", True, "Vino tinto de alta calidad.")
    socio_cervezas.actualizar_producto("Cerveza Artesanal IPA", False, "Cerveza con un amargor característico.")
    socio_postres.actualizar_producto("Tiramisú", True, "Postre italiano con capas de bizcocho y crema mascarpone.")

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

# Ejemplo de uso para la pizzería Delizioso
if __name__ == "__main__":
    # Crear instancias de los eventos (observadores)
    evento_nuevos_sabores = EventoNuevosSabores()
    evento_promociones_pizzas = EventoPromocionesPizzas()

    # Crear el notificador (sujeto)
    notificador = Notificador()

    # Agregar observadores al notificador
    notificador.agregar_observador(evento_nuevos_sabores)
    notificador.agregar_observador(evento_promociones_pizzas)

    # Introducir un nuevo sabor de pizza y notificar a los observadores
    nuevo_sabor = "Pizza de Pollo BBQ"
    notificador.notificar(f"Nuevo sabor de pizza disponible: {nuevo_sabor}")

    # Introducir una nueva promoción en pizzas y notificar a los observadores
    nueva_promocion_pizzas = "Descuento del 20% en todas las pizzas medianas"
    notificador.notificar(f"Nueva promoción en pizzas: {nueva_promocion_pizzas}")

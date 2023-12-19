# composite_pattern.py
from abc import ABC, abstractmethod
from typing import List

class Componente(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class Documento(Componente):
    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.tipo = tipo
        self.tamano = taman

    def mostrar(self):
        print(f"Documento: {self.nombre}, Tipo: {self.tipo}, Tamaño: {self.tamano} KB")

class Enlace(Componente):
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def mostrar(self):
        print(f"Enlace: {self.nombre}, Destino: {self.destino}")

class Carpeta(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenidos: List[Componente] = []

    def agregar(self, componente: Componente):
        self.contenidos.append(componente)

    def mostrar(self):
        print(f"Carpeta: {self.nombre}")
        for componente in self.contenidos:
            componente.mostrar()

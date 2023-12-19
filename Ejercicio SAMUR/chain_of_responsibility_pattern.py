# chain_of_responsibility_pattern.py
from abc import ABC, abstractmethod

class ManejadorAutorizacion(ABC):
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    @abstractmethod
    def autorizar(self, usuario, documento):
        pass

class Tecnico(ManejadorAutorizacion):
    def autorizar(self, usuario, documento):
        if usuario.rol == "Técnico":
            print(f"Técnico {usuario.nombre} autorizó el acceso a {documento.nombre}")
            return True
        elif self.siguiente:
            return self.siguiente.autorizar(usuario, documento)
        else:
            print(f"Acceso denegado para {usuario.nombre}")
            return False

class Supervisor(ManejadorAutorizacion):
    def autorizar(self, usuario, documento):
        if usuario.rol == "Supervisor":
            print(f"Supervisor {usuario.nombre} autorizó el acceso a {documento.nombre}")
            return True
        elif self.siguiente:
            return self.siguiente.autorizar(usuario, documento)
        else:
            print(f"Acceso denegado para {usuario.nombre}")
            return False

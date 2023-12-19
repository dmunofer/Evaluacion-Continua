# state_pattern.py
from abc import ABC, abstractmethod

class EstadoDocumento(ABC):
    @abstractmethod
    def realizar_accion(self, documento):
        pass

class EstadoPendienteAprobacion(EstadoDocumento):
    def realizar_accion(self, documento):
        print(f"Documento {documento.nombre} está pendiente de aprobación.")

class EstadoAprobado(EstadoDocumento):
    def realizar_accion(self, documento):
        print(f"Documento {documento.nombre} ha sido aprobado y ahora es accesible.")

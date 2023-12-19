# proxy_pattern.py
class ProxyAcceso:
    def __init__(self, usuario):
        self.usuario = usuario
        self.documentos_autorizados = set()

    def solicitar_acceso(self, documento):
        # Lógica de autorización aquí
        return True

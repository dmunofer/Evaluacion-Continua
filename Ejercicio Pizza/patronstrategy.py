from abc import ABC, abstractmethod
from sklearn.neural_network import MLPClassifier
import numpy as np

# Definición de la interfaz de la Estrategia de Precios
class EstrategiaPrecios(ABC):
    @abstractmethod
    def aplicar_estrategia(self, precio_base, *args, **kwargs):
        pass

# Estrategia de Hora Pico
class EstrategiaHoraPico(EstrategiaPrecios):
    def aplicar_estrategia(self, precio_base):
        return precio_base * 1.2  # Aumentar el precio durante las horas pico

# Estrategia de Demanda
class EstrategiaDemanda(EstrategiaPrecios):
    def aplicar_estrategia(self, precio_base, demanda):
        return precio_base * (1 + 0.1 * demanda)  # Ajustar el precio según la demanda

# Estrategia de Promociones
class EstrategiaPromociones(EstrategiaPrecios):
    def __init__(self, descuento):
        self.descuento = descuento

    def aplicar_estrategia(self, precio_base, es_promocion):
        if es_promocion:
            return precio_base * (1 - self.descuento)  # Aplicar descuento en caso de promoción
        else:
            return precio_base

# Estrategia de Red Neuronal
class EstrategiaRedNeuronal(EstrategiaPrecios):
    def __init__(self, modelo_red_neuronal):
        self.modelo_red_neuronal = modelo_red_neuronal

    def aplicar_estrategia(self, precio_base):
        # Lógica para obtener la predicción de la red neuronal y ajustar el precio
        prediccion = self.modelo_red_neuronal.predict(np.array([[precio_base]]))
        return precio_base * prediccion[0]

# Contexto que utiliza la Estrategia de Precios
class ContextoPrecio:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def cambiar_estrategia(self, estrategia):
        self.estrategia = estrategia

    def obtener_precio_final(self, precio_base, *args, **kwargs):
        return self.estrategia.aplicar_estrategia(precio_base, *args, **kwargs)

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    precio_base = 10.0
    demanda = 0.8
    es_promocion = True

    # Crear instancias de las estrategias
    estrategia_hora_pico = EstrategiaHoraPico()
    estrategia_demanda = EstrategiaDemanda()
    estrategia_promociones = EstrategiaPromociones(descuento=0.2)

    # Crear una red neuronal simple (MLP) para predecir la mejor estrategia
    datos_entrenamiento = np.array([[0.7, 0.8, 0.2], [0.3, 0.5, 0.8], [0.5, 0.6, 0.5]])  # Ejemplos de datos
    etiquetas_entrenamiento = np.array([1, 0, 1])  # Clases correspondientes a las estrategias

    red_neuronal = MLPClassifier(hidden_layer_sizes=(5, 2), max_iter=1000, random_state=42)
    red_neuronal.fit(datos_entrenamiento, etiquetas_entrenamiento)

    # Crear una estrategia basada en la red neuronal
    estrategia_red_neuronal = EstrategiaRedNeuronal(red_neuronal)

    # Crear un contexto con una estrategia inicial (puede ser cualquiera de las estrategias)
    contexto = ContextoPrecio(estrategia_hora_pico)

    # Obtener precios utilizando la estrategia actual
    precio_final = contexto.obtener_precio_final(precio_base)
    print(f"Precio final con estrategia de hora pico: {precio_final:.2f}")

    # Cambiar a otra estrategia (por ejemplo, estrategia de demanda)
    contexto.cambiar_estrategia(estrategia_demanda)

    # Obtener precios con la nueva estrategia
    precio_final = contexto.obtener_precio_final(precio_base, demanda=demanda)
    print(f"Precio final con estrategia de demanda: {precio_final:.2f}")

    # Cambiar a la estrategia de promociones
    contexto.cambiar_estrategia(estrategia_promociones)

    # Obtener precios con la estrategia de promociones
    precio_final = contexto.obtener_precio_final(precio_base, es_promocion=es_promocion)
    print(f"Precio final con estrategia de promociones: {precio_final:.2f}")

    # Cambiar a la estrategia basada en la red neuronal
    contexto.cambiar_estrategia(estrategia_red_neuronal)

    # Obtener precios con la estrategia de la red neuronal
    precio_final = contexto.obtener_precio_final(precio_base)
    print(f"Precio final con estrategia de red neuronal: {precio_final:.2f}")

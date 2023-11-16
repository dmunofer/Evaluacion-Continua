from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

class AnalysisFactory(ABC):
    @abstractmethod
    def create_mode(self) -> AbstractMode:
        pass

    @abstractmethod
    def create_mean(self) -> AbstractMean:
        pass

class ConcreteFactory_HourRequested(AnalysisFactory)
    def __init__(self, data):
        self.data = data

    def create_mode(self) -> AbstractMode:
        return ConcreteMode_HourRequested(self.data)

    def create_mean(self) -> AbstractMean:
        return ConcreteMean_HourRequested(self.data)

class ConcreteFactory_Month(AnalysisFactory):
    def __init__(self, data):
        self.data = data

    def create_mode(self) -> AbstractMode:
        return ConcreteMode_Month(self.data)

    def create_mean(self) -> AbstractMean:
        return ConcreteMean_Month(self.data)

class ConcreteFactory_HourIntervention(AnalysisFactory):
    def __init__(self, data):
        self.data = data

    def create_mean(self) -> AbstractMode:
        return ConcreteMode_HourIntervention(self.data)

    def create_mode(self) -> AbstractMean:
        return ConcreteMean_HourIntervention(self.data)

class AbstractMode(ABC):
    @abstractmethod
    def calculate(self):
        pass

class ConcreteMode_HourRequested(AbstractMode):
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return self.data['Hour Requested'].mode()

class ConcreteMode_Month(AbstractMode):
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return self.data['Month'].mode()

class ConcreteMode_HourIntervention(AbstractMode):
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return self.data['Hour Intervention'].mode()

class AbstractMean(ABC):
    @abstractmethod
    def calculate(self):
        pass

class ConcreteMean_HourRequested(AbstractMean):
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return self.data['Hour Requested'].mean()

class ConcreteMean_Month(AbstractMean):
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return self.data['Month'].mean()

class ConcreteMean_HourIntervention(AbstractMean):
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return self.data['Hour Intervention'].mean()

def client_code_mode(factory: AnalysisFactory) -> None:
    mode_calculator = factory.create_mode()
    print(f'Mode: {mode_calculator.calculate()}')

def client_code_mean(factory: AnalysisFactory) -> None:
    mean_calculator = factory.create_mean()
    print(f'Mean: {mean_calculator.calculate()}')

if __name__ == "__main__":
    data = pd.read_csv('Ejercicio1/activaciones_samur_2022.csv', delimiter=";")
    data = data.dropna()

    months_to_numbers = {
        'ENERO': 1,
        'FEBRERO': 2,
        'MARZO': 3,
        'ABRIL': 4,
        'MAYO': 5,
        'JUNIO': 6,
        'JULIO': 7,
        'AGOSTO': 8,
        'SEPTIEMBRE': 9,
        'OCTUBRE': 10,
        'NOVIEMBRE': 11,
        'DICIEMBRE': 12
    }

    data['Month'] = data['Month'].map(months_to_numbers)

    # Simplificación de la conversión de horas
    time_columns = ['Hour Requested', 'Hour Intervention']
    for col in time_columns:
        data[col] = pd.to_datetime(data[col], format='%H:%M:%S').dt.hour * 60 + pd.to_datetime(data[col], format='%H:%M:%S').dt.minute

    # Eliminar la columna 'Year'
    data.drop('Year', axis=1, inplace=True)

    factory_hour_requested = ConcreteFactory_HourRequested(data)
    factory_hour_intervention = ConcreteFactory_HourIntervention(data)
    factory_month = ConcreteFactory_Month(data)

    print("Hour Requested:")
    client_code_mode(factory_hour_requested)
    client_code_mean(factory_hour_requested)

    print("Month:")
    client_code_mode(factory_month)
    client_code_mean(factory_month)

    print("Hour Intervention:")
    client_code_mode(factory_hour_intervention)
    client_code_mean(factory_hour_intervention)

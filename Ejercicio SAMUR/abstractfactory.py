from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Union
import pandas as pd

#Componente base del Composite
class DocumentComponent(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self) -> None:
        pass

#Documento concreto del Composite
class Document(DocumentComponent):
    def __init__(self, name: str, doc_type: str, size: int):
        self.name = name
        self.doc_type = doc_type
        self.size = size

    def get_size(self) -> int:
        return self.size

    def display(self) -> None:
        print(f"Document: {self.name}.{self.doc_type}, Size: {self.size} KB")

#Enlace concreto del Composite
class Link(DocumentComponent):
    def __init__(self, name: str, target: Union[Document, Folder]):
        self.name = name
        self.target = target

    def get_size(self) -> int:
        # El tamaño del enlace es simbólico
        return 1

    def display(self) -> None:
        print(f"Link: {self.name} -> {self.target.name}")

#Carpeta concreta del Composite
class Folder(DocumentComponent):
    def __init__(self, name: str):
        self.name = name
        self.children: List[DocumentComponent] = []

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)

    def display(self) -> None:
        print(f"Folder: {self.name}, Size: {self.get_size()} KB")
        for child in self.children:
            child.display()

    def add(self, component: DocumentComponent) -> None:
        self.children.append(component)

    def remove(self, component: DocumentComponent) -> None:
        self.children.remove(component)

    def get_children(self) -> List[DocumentComponent]:
        return self.children

#Proxy concreto para el acceso a documentos
class DocumentProxy(DocumentComponent):
    def __init__(self, document: Document, access_log: List[str], user: str):
        self.document = document
        self.access_log = access_log
        self.user = user

    def get_size(self) -> int:
        return self.document.get_size()

    def display(self) -> None:
        print(f"Proxy Document: {self.document.name}.{self.document.doc_type}, Size: {self.get_size()} KB")

    def access_document(self) -> None:
        self.access_log.append(f"{self.user} accessed {self.document.name}.{self.document.doc_type}")

#Fábrica abstracta para análisis de datos
class AnalysisFactory(ABC):
    @abstractmethod
    def create_statistical_analysis(self, data) -> DocumentComponent:
        pass

    @abstractmethod
    def create_visualization(self, data) -> DocumentComponent:
        pass

# Fábrica concreta para análisis estadístico
class StatisticalAnalysisFactory(AnalysisFactory):
    def create_statistical_analysis(self, data) -> DocumentComponent:
        return Document(f"Statistical Analysis", "txt", 10)

    def create_visualization(self, data) -> DocumentComponent:
        return Link("Statistical Visualization", Folder("Visualizations"))

# Fábrica concreta para visualizaciones gráficas
class VisualizationFactory(AnalysisFactory):
    def create_statistical_analysis(self, data) -> DocumentComponent:
        return Link("Graphical Analysis", Folder("Analyses"))

    def create_visualization(self, data) -> DocumentComponent:
        return Document(f"Graphical Visualization", "png", 200)



from abstractfactory import *
from composite_pattern import Documento, Enlace, Carpeta
from proxy_pattern import ProxyAcceso
from chain_of_responsibility_pattern import Tecnico, Supervisor
from state_pattern import EstadoPendienteAprobacion, EstadoAprobado
from usuario import *
def main():
    try:
        # Acceder y leer el archivo CSV
        data = pd.read_csv('Ejercicio SAMUR/activaciones_samur_2022.csv', delimiter=";")

        # Crear una carpeta que contendrá los documentos generados
        root_folder = Folder("Analysis Results")

        # Crear una fábrica concreta de análisis estadístico
        statistical_analysis_factory = StatisticalAnalysisFactory()
        statistical_analysis = statistical_analysis_factory.create_statistical_analysis(data)
        root_folder.add(statistical_analysis)

        # Crear una fábrica concreta de visualizaciones
        visualization_factory = VisualizationFactory()
        visualization = visualization_factory.create_visualization(data)
        root_folder.add(visualization)

        # Mostrar la estructura generada
        root_folder.display()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

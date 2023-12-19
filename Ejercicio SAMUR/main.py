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

    # Crear documentos, enlaces y carpetas
    doc1 = Documento("Informe.pdf", "PDF", 120)
    doc2 = Documento("Especificaciones.docx", "Word", 80)
    enlace1 = Enlace("Enlace a Sitio Web", "https://www.ejemplo.com")
    carpeta1 = Carpeta("Documentos Importantes")
    carpeta1.agregar(doc1)
    carpeta1.agregar(doc2)
    carpeta1.agregar(enlace1)

    # Crear un proxy de acceso para un usuario
    usuario_proxy = ProxyAcceso(usuario=Usuario(nombre="Usuario1", rol="Técnico"))

    # Solicitar acceso a un documento
    if usuario_proxy.solicitar_acceso(doc1):
        doc1.mostrar()
    else:
        print("Acceso denegado.")

    # Configurar la cadena de autorización
    manejador_tecnico = Tecnico()
    manejador_supervisor = Supervisor(siguiente=manejador_tecnico)

    # Asignar roles a los usuarios
    usuario_tecnico = Usuario(nombre="Técnico1", rol="Técnico")
    usuario_supervisor = Usuario(nombre="Supervisor1", rol="Supervisor")

    # Autorizar acceso a un documento
    manejador_supervisor.autorizar(usuario_tecnico, doc1)
    manejador_supervisor.autorizar(usuario_supervisor, doc1)

    # Cambiar el estado del documento
    estado_pendiente = EstadoPendienteAprobacion()
    estado_aprobado = EstadoAprobado()

    doc1.estado = estado_pendiente
    doc1.estado.realizar_accion(doc1)

    doc1.estado = estado_aprobado
    doc1.estado.realizar_accion(doc1)

if __name__ == "__main__":
    main()

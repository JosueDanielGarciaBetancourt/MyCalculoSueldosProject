# TODO: Corregir bugs de agregar, modificar y  eliminar en su conjunto e individualmente
# TODO: Agregar nuevaUnidadBonificacion a tblBonificacion
# TODO: Implementar el funcionamiento de ventana FormInspeccionarTrabajador
# TODO: Implementar ordenamiento de tablas por ID y por Fechas
# TODO: Implementar justificaciones
# TODO: Después de cada CRUD se debe actualizar la tabla de trabajadores GUI

from logica.EjemploOperacionesDB import EjemploOperacionesDB
from modelo.Declarative_Base import reiniciarDB
from vista.GestorSueldos import GestorSueldos
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])  # Inicializando aplicación
    
    reiniciarDB()
    EjemploOperacionesDB()

    print("\nEjecutando app...")
    App = GestorSueldos(app)

# Importamos ABC para crear clases abstractas
from abc import ABC


# Clase abstracta base del sistema
class Entidad(ABC):

    # Constructor de la clase
    def __init__(self, id_entidad):

        # Validamos que el ID sea entero
        if not isinstance(id_entidad, int):
            raise ValueError("El ID debe ser un número entero")

        # Validamos que el ID sea mayor que cero
        if id_entidad <= 0:
            raise ValueError("El ID debe ser mayor que cero")

        # Encapsulamos el atributo
        self._id_entidad = id_entidad

    # Método getter para obtener el ID
    @property
    def id_entidad(self):
        return self._id_entidad
# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod

# Importamos la clase Entidad
from modelos.entidad import Entidad


# Clase abstracta Servicio
class Servicio(Entidad, ABC):

    # Constructor de la clase Servicio
    def __init__(self, id_entidad, nombre, costo_base):

        # Llamamos al constructor padre
        super().__init__(id_entidad)

        # Validamos que el nombre no este vacío
        if not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío")

        # Validamos que el costo sea positivo
        if costo_base <= 0:
            raise ValueError("El costo base debe ser mayor que cero")

        # Encapsulación de atributos
        self._nombre = nombre
        self._costo_base = costo_base

    # Getter del nombree
    @property
    def nombre(self):
        return self._nombre

    # Getter del costo base
    @property
    def costo_base(self):
        return self._costo_base

    # Método abstracto para calcular costo
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto para describir servicio
    @abstractmethod
    def describir_servicio(self):
        pass
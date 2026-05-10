from modelos.entidad import Entidad
import re


class Cliente(Entidad):

    def __init__(self, id_entidad, nombre, documento, correo):

        super().__init__(id_entidad)

        # VALIDACIÓN NOMBRE
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        # VALIDACIÓN DOCUMENTO
        if not documento.isdigit():
            raise ValueError("El documento debe contener solo números")

        # VALIDACIÓN CORREO
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, correo):
            raise ValueError("Correo electrónico inválido")

        self._nombre = nombre
        self._documento = documento
        self._correo = correo

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    @property
    def correo(self):
        return self._correo

    def mostrar_info(self):

        return (
            f"Cliente: {self._nombre}\n"
            f"Documento: {self._documento}\n"
            f"Correo: {self._correo}"
        )
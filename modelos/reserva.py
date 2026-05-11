# IMPORTAMOS DATETIME
from datetime import datetime

# IMPORTAMOS CLASES
from modelos.cliente import Cliente
from modelos.servicio import Servicio


# ==================================================
# EXCEPCIONES PERSONALIZADAS
# ==================================================

class ReservaError(Exception):
    """Clase base para excepciones de Reserva"""
    pass


class ReservaYaConfirmadaError(ReservaError):
    """Excepción lanzada cuando la reserva ya está confirmada"""
    pass


class ReservaYaCanceladaError(ReservaError):
    """Excepción lanzada cuando la reserva ya está cancelada"""
    pass


class ReservaConfirmadaError(ReservaError):
    """Excepción lanzada cuando se intenta cancelar una reserva confirmada"""
    pass


class ReservaCanceladaError(ReservaError):
    """Excepción lanzada cuando se intenta procesar una reserva cancelada"""
    pass


# ==================================================
# CLASE RESERVA
# ==================================================

class Reserva:

    # CONSTRUCTOR
    def __init__(self, cliente, servicio, duracion):

        # VALIDACIÓN CLIENTE
        if not isinstance(cliente, Cliente):

            raise ValueError(
                "El cliente es inválido"
            )

        # VALIDACIÓN SERVICIO
        if not isinstance(servicio, Servicio):

            raise ValueError(
                "El servicio es inválido"
            )

        # VALIDACIÓN DURACIÓN
        if duracion <= 0:

            raise ValueError(
                "La duración debe ser mayor a 0"
            )

        # ATRIBUTOS
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion

        # ESTADO INICIAL
        self._estado = "pendiente"

        # FECHA CREACIÓN
        self._fecha = datetime.now()

    # ==================================================
    # GETTERS
    # ==================================================

    @property
    def cliente(self):

        return self._cliente

    @property
    def servicio(self):

        return self._servicio

    @property
    def duracion(self):

        return self._duracion

    @property
    def estado(self):

        return self._estado

    @property
    def fecha(self):

        return self._fecha

    # ==================================================
    # CONFIRMAR RESERVA
    # ==================================================

    def confirmar(self):

        # VALIDAR SI YA ESTÁ CONFIRMADA
        if self._estado == "confirmada":

            raise ReservaYaConfirmadaError(
                "La reserva ya está confirmada"
            )

        # VALIDAR SI ESTÁ CANCELADA
        if self._estado == "cancelada":

            raise ReservaCanceladaError(
                "No se puede confirmar una reserva cancelada"
            )

        # CAMBIAR ESTADO
        self._estado = "confirmada"

        print("Reserva confirmada correctamente")

    # ==================================================
    # CANCELAR RESERVA
    # ==================================================

    def cancelar(self):

        # VALIDAR SI YA ESTÁ CANCELADA
        if self._estado == "cancelada":

            raise ReservaYaCanceladaError(
                "La reserva ya fue cancelada"
            )

        # VALIDAR SI YA ESTÁ CONFIRMADA
        if self._estado == "confirmada":

            raise ReservaConfirmadaError(
                "No se puede cancelar una reserva confirmada"
            )

        # CAMBIAR ESTADO
        self._estado = "cancelada"

        print("Reserva cancelada correctamente")

    # ==================================================
    # PROCESAR RESERVA
    # ==================================================

    def procesar(self):

        try:

            # VALIDAR ESTADO
            if self._estado == "cancelada":

                raise ReservaCanceladaError(
                    "No se puede procesar una reserva cancelada"
                )

            print("Procesando reserva...")

            # CALCULAR COSTO
            costo = self._servicio.calcular_costo(
                self._duracion
            )

            print(
                f"Costo total de la reserva: ${costo}"
            )

            return costo

        except ReservaError as error:

            print(
                "Error al procesar la reserva:",
                error
            )

            return None

    # ==================================================
    # MOSTRAR INFORMACIÓN
    # ==================================================

    def mostrar_reserva(self):

        return (

            "\n----- INFORMACIÓN DE LA RESERVA -----\n"

            f"Cliente: {self._cliente.nombre}\n"

            f"Servicio: {self._servicio.nombre}\n"

            f"Duración: {self._duracion}\n"

            f"Estado: {self._estado}\n"

            f"Fecha: {self._fecha}"
        )
from datetime import datetime

# Excepciones personalizadas para la Reserva
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

# Clase Reserva
class Reserva:

    # Constructor
    def __init__(self, cliente, servicio, duracion):

        # Validaciones básicas
        if cliente is None:
            raise ValueError("El cliente no puede estar vacío")

        if servicio is None:
            raise ValueError("El servicio no puede estar vacío")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0")

        # Integración de objetos
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

        # Estados de la reserva
        self.estado = "pendiente"

        # Fecha de creación
        self.fecha = datetime.now()

    # Método para confirmar reserva
    def confirmar(self):

        if self.estado == "confirmada":
            raise ReservaYaConfirmadaError("La reserva ya está confirmada")

        if self.estado == "cancelada":
            raise ReservaCanceladaError("No se puede confirmar una reserva cancelada")

        self.estado = "confirmada"

        print("Reserva confirmada correctamente")

    # Método para cancelar reserva
    def cancelar(self):

        if self.estado == "cancelada":
            raise ReservaYaCanceladaError("La reserva ya fue cancelada")

        if self.estado == "confirmada":
            raise ReservaConfirmadaError("No se puede cancelar una reserva confirmada")

        self.estado = "cancelada"

        print("Reserva cancelada correctamente")

    # Método para procesar reserva
    def procesar(self):

        try:

            # Validar estado
            if self.estado == "cancelada":
                raise ReservaCanceladaError("No se puede procesar una reserva cancelada")

            print("Procesando reserva...")

            # Calcular costo del servicio
            costo = self.servicio.calcular_costo(self.duracion)

            print(f"Costo total de la reserva: ${costo}")

            return costo

        except ReservaError as e:

            print("Error al procesar la reserva:", e)
            return None

    # Mostrar información de la reserva
    def mostrar_reserva(self):

        print("\n----- INFORMACIÓN DE LA RESERVA -----")

        print("Cliente:", self.cliente.nombre)

        print("Servicio:", self.servicio.nombre)

        print("Duración:", self.duracion)

        print("Estado:", self.estado)

        print("Fecha:", self.fecha)

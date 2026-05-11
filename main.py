# SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ

# IMPORTACIONES
from modelos.cliente import Cliente
from modelos.reserva import Reserva

# SERVICIOS DERIVADOS
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import AsesoriaEspecializada

# LOGGER
from excepciones.logger import (
    configurar_logger,
    registrar_info,
    registrar_error
)

# CONFIGURAR LOGGER
configurar_logger()

print("===== SOFTWARE FJ =====")


# SIMULACIÓN 1 - RESERVA DE SALA

try:

    cliente1 = Cliente(
        1,
        "Andrés Sánchez",
        "123456789",
        "andres@gmail.com"
    )

    servicio1 = ReservaSala(
        1,
        "Sala Ejecutiva",
        50000
    )

    reserva1 = Reserva(
        cliente1,
        servicio1,
        3
    )

    reserva1.confirmar()

    print("\n[SIMULACIÓN 1]")

    print(
        reserva1.mostrar_reserva()
    )

    reserva1.procesar()

    registrar_info(
        "Reserva de sala realizada correctamente"
    )

except Exception as error:

    print(
        f"Error en simulación 1: {error}"
    )

    registrar_error(
        f"Error en simulación 1: {error}"
    )


# SIMULACIÓN 2 - ALQUILER DE EQUIPO

try:

    cliente2 = Cliente(
        2,
        "María López",
        "987654321",
        "maria@gmail.com"
    )

    servicio2 = AlquilerEquipo(
        2,
        "Computador Gamer",
        80000
    )

    reserva2 = Reserva(
        cliente2,
        servicio2,
        2
    )

    reserva2.confirmar()

    print("\n[SIMULACIÓN 2]")

    print(
        reserva2.mostrar_reserva()
    )

    reserva2.procesar()

    registrar_info(
        "Alquiler de equipo realizado correctamente"
    )

except Exception as error:

    print(
        f"Error en simulación 2: {error}"
    )

    registrar_error(
        f"Error en simulación 2: {error}"
    )


# SIMULACIÓN 3 - ASESORÍA ESPECIALIZADA

try:

    cliente3 = Cliente(
        3,
        "Carlos Pérez",
        "456789123",
        "carlos@gmail.com"
    )

    servicio3 = AsesoriaEspecializada(
        3,
        "Asesoría de Software",
        100000
    )

    reserva3 = Reserva(
        cliente3,
        servicio3,
        4
    )

    reserva3.confirmar()

    print("\n[SIMULACIÓN 3]")

    print(
        reserva3.mostrar_reserva()
    )

    reserva3.procesar()

    registrar_info(
        "Asesoría registrada correctamente"
    )

except Exception as error:

    print(
        f"Error en simulación 3: {error}"
    )

    registrar_error(
        f"Error en simulación 3: {error}"
    )


# SIMULACIÓN 4 - CORREO INVÁLIDO

try:

    cliente4 = Cliente(
        4,
        "Laura",
        "741258963",
        "correo_malo"
    )

except Exception as error:

    print("\n[SIMULACIÓN 4]")

    print(
        f"Error detectado: {error}"
    )

    registrar_error(
        f"Error en simulación 4: {error}"
    )


# SIMULACIÓN 5 - COSTO NEGATIVO

try:

    servicio5 = ReservaSala(
        5,
        "Sala VIP",
        -50000
    )

except Exception as error:

    print("\n[SIMULACIÓN 5]")

    print(
        f"Error detectado: {error}"
    )

    registrar_error(
        f"Error en simulación 5: {error}"
    )


# SIMULACIÓN 6 - CANCELACIÓN DE RESERVA

try:

    cliente6 = Cliente(
        6,
        "Valentina",
        "159753486",
        "valentina@gmail.com"
    )

    servicio6 = AlquilerEquipo(
        6,
        "Proyector",
        30000
    )

    reserva6 = Reserva(
        cliente6,
        servicio6,
        5
    )

    reserva6.cancelar()

    print("\n[SIMULACIÓN 6]")

    print(
        reserva6.mostrar_reserva()
    )

    reserva6.procesar()

    registrar_info(
        "Reserva cancelada correctamente"
    )

except Exception as error:

    print(
        f"Error en simulación 6: {error}"
    )

    registrar_error(
        f"Error en simulación 6: {error}"
    )


# SIMULACIÓN 7 - DOCUMENTO INVÁLIDO

try:

    cliente7 = Cliente(
        7,
        "Pedro",
        "ABC123",
        "pedro@gmail.com"
    )

except Exception as error:

    print("\n[SIMULACIÓN 7]")

    print(
        f"Error detectado: {error}"
    )

    registrar_error(
        f"Error en simulación 7: {error}"
    )


# SIMULACIÓN 8 - NOMBRE VACÍO

try:

    cliente8 = Cliente(
        8,
        "",
        "123456789",
        "cliente@gmail.com"
    )

except Exception as error:

    print("\n[SIMULACIÓN 8]")

    print(
        f"Error detectado: {error}"
    )

    registrar_error(
        f"Error en simulación 8: {error}"
    )


# SIMULACIÓN 9 - DURACIÓN INVÁLIDA

try:

    cliente9 = Cliente(
        9,
        "Camilo",
        "951753852",
        "camilo@gmail.com"
    )

    servicio9 = ReservaSala(
        9,
        "Sala Empresarial",
        60000
    )

    reserva9 = Reserva(
        cliente9,
        servicio9,
        -2
    )

except Exception as error:

    print("\n[SIMULACIÓN 9]")

    print(
        f"Error detectado: {error}"
    )

    registrar_error(
        f"Error en simulación 9: {error}"
    )


# SIMULACIÓN 10 - DOBLE CONFIRMACIÓN

try:

    cliente10 = Cliente(
        10,
        "Sofía",
        "852456123",
        "sofia@gmail.com"
    )

    servicio10 = AsesoriaEspecializada(
        10,
        "Consultoría Premium",
        150000
    )

    reserva10 = Reserva(
        cliente10,
        servicio10,
        2
    )

    reserva10.confirmar()

    # ERROR INTENCIONAL
    reserva10.confirmar()

except Exception as error:

    print("\n[SIMULACIÓN 10]")

    print(
        f"Error detectado: {error}"
    )

    registrar_error(
        f"Error en simulación 10: {error}"
    )

# FINAL DEL PROGRAMA

print("\n===== FIN DEL PROGRAMA =====")

registrar_info(
    "Finalización correcta del programa"
)
# ==================================================
# SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ
# ==================================================

# IMPORTACIONES
from modelos.cliente import Cliente

# IMPORTAMOS LOGGER
from excepciones.logger import (
    configurar_logger,
    registrar_info,
    registrar_error
)

# CONFIGURAMOS EL LOGGER
configurar_logger()

print("===== SOFTWARE FJ =====")



# SIMULACIÓN 1 - CLIENTE VÁLIDO


try:

    cliente1 = Cliente(
        1,
        "Andrés Sánchez",
        "123456789",
        "andres@gmail.com"
    )

    print("\n[SIMULACIÓN 1]")
    print(cliente1.mostrar_info())

    registrar_info("Cliente 1 registrado correctamente")

except ValueError as error:

    print(f"Error: {error}")

    registrar_error(f"Error en simulación 1: {error}")



# SIMULACIÓN 2 - NOMBRE VACÍO

try:

    cliente2 = Cliente(
        2,
        "",
        "987654321",
        "cliente@gmail.com"
    )

    print(cliente2.mostrar_info())

    registrar_info("Cliente 2 registrado correctamente")

except ValueError as error:

    print("\n[SIMULACIÓN 2]")
    print(f"Error detectado: {error}")

    registrar_error(f"Error en simulación 2: {error}")


# SIMULACIÓN 3 - DOCUMENTO INVÁLIDO

try:

    cliente3 = Cliente(
        3,
        "Carlos",
        "ABC123",
        "carlos@gmail.com"
    )

    print(cliente3.mostrar_info())

    registrar_info("Cliente 3 registrado correctamente")

except ValueError as error:

    print("\n[SIMULACIÓN 3]")
    print(f"Error detectado: {error}")

    registrar_error(f"Error en simulación 3: {error}")


# SIMULACIÓN 4 - CORREO INVÁLIDO

try:

    cliente4 = Cliente(
        4,
        "Laura",
        "456789123",
        "correo_malo"
    )

    print(cliente4.mostrar_info())

    registrar_info("Cliente 4 registrado correctamente")

except ValueError as error:

    print("\n[SIMULACIÓN 4]")
    print(f"Error detectado: {error}")

    registrar_error(f"Error en simulación 4: {error}")


# SIMULACIÓN 5 - ID NEGATIVO

try:

    cliente5 = Cliente(
        -1,
        "Pedro",
        "741258963",
        "pedro@gmail.com"
    )

    print(cliente5.mostrar_info())

    registrar_info("Cliente 5 registrado correctamente")

except ValueError as error:

    print("\n[SIMULACIÓN 5]")
    print(f"Error detectado: {error}")

    registrar_error(f"Error en simulación 5: {error}")


# SIMULACIÓN 6 - CLIENTE VÁLIDO

try:

    cliente6 = Cliente(
        6,
        "María",
        "852369741",
        "maria@gmail.com"
    )

    print("\n[SIMULACIÓN 6]")
    print(cliente6.mostrar_info())

    registrar_info("Cliente 6 registrado correctamente")

except ValueError as error:

    print(f"Error: {error}")

    registrar_error(f"Error en simulación 6: {error}")


# SIMULACIÓN 7 - CORREO VACÍO

try:

    cliente7 = Cliente(
        7,
        "Camilo",
        "123123123",
        ""
    )

    print(cliente7.mostrar_info())

    registrar_info("Cliente 7 registrado correctamente")

except ValueError as error:

    print("\n[SIMULACIÓN 7]")
    print(f"Error detectado: {error}")

    registrar_error(f"Error en simulación 7: {error}")


# SIMULACIÓN 8 - DOCUMENTO VACÍO

try:

    cliente8 = Cliente(
        8,
        "Sofía",
        "",
        "sofia@gmail.com"
    )

    print(cliente8.mostrar_info())

    registrar_info("Cliente 8 registrado correctamente")

except ValueError as error:

    print("\n[SIMULACIÓN 8]")
    print(f"Error detectado: {error}")

    registrar_error(f"Error en simulación 8: {error}")


# SIMULACIÓN 9 - NOMBRE CON ESPACIOS

try:

    cliente9 = Cliente(
        9,
        "     ",
        "963258741",
        "espacios@gmail.com"
    )

    print(cliente9.mostrar_info())

    registrar_info("Cliente 9 registrado correctamente")

except ValueError as error:

    print("\n[SIMULACIÓN 9]")
    print(f"Error detectado: {error}")

    registrar_error(f"Error en simulación 9: {error}")

# SIMULACIÓN 10 - CLIENTE FINAL VÁLIDO

try:

    cliente10 = Cliente(
        10,
        "Valentina",
        "159753486",
        "valentina@gmail.com"
    )

    print("\n[SIMULACIÓN 10]")
    print(cliente10.mostrar_info())

    registrar_info("Cliente 10 registrado correctamente")

except ValueError as error:

    print(f"Error: {error}")

    registrar_error(f"Error en simulación 10: {error}")


# FIN DEL PROGRAMA

print("\n===== FIN DE SIMULACIONES =====")

registrar_info("Finalización correcta del programa")
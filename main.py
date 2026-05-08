# Importamos la clase Cliente
from modelos.cliente import Cliente


# Bloque try para controlar posibles errores
try:

    # Creamos un cliente válido
    cliente1 = Cliente(
        1,
        "Andrés Sánchez",
        "123456789",
        "andres@gmail.com"
    )

    # Mostramos información del cliente
    print(cliente1.mostrar_info())

# Capturamos errores de validación
except ValueError as error:

    # Mostramos mensaje de error
    print(f"Error: {error}")
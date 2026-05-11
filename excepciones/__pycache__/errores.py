from excepciones import logger  # Importamos nuestro módulo de logs

# 1. DEFINICIÓN DE EXCEPCIONES PERSONALIZADAS (Jerarquía Orientada a Objetos)

class SoftwareFJError(Exception):
    """Clase base para cualquier error de lógica o negocio dentro del sistema."""
    pass

class DatoInvalidoError(SoftwareFJError):
    """Se lanza cuando un dato de entrada (correo, identificación) no cumple el formato."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando la lógica de una reserva no se cumple (ej. valores negativos)."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza si se intenta acceder o reservar un servicio inactivo o inexistente."""
    pass


# 2. PROCESAMIENTO ROBUSTO CON TODAS LAS ESTRUCTURAS EXIGIDAS

def procesar_reserva_segura(cliente_id, servicio_nombre, duracion_horas, costo_base):
    """
    Simula el procesamiento de una reserva aplicando manejo avanzado de excepciones.
    Cubre: try/except/else, try/except/finally y encadenamiento de excepciones.
    """
    
    # --- ESTRUCTURA: try/except (Para validación de tipo de datos iniciales) ---
    try:
        # Registrar el inicio del evento
        logger.registrar_evento(f"Iniciando intento de reserva para el Cliente ID: {cliente_id}")
        
        # Validación de tipo de datos (Dato inválido)
        if not str(cliente_id).isdigit():
            raise DatoInvalidoError(f"El identificador de cliente '{cliente_id}' debe ser únicamente numérico.")
            
    except DatoInvalidoError as error_dato:
        # Se captura el error, se registra en logs.txt y se muestra al usuario sin colapsar
        logger.registrar_dato_invalido(str(error_dato))
        print(f" Error de datos: {error_dato}")
        return False


    # --- ESTRUCTURA: try/except/else/finally (Cálculos y lógica de negocio con encadenamiento) ---
    try:
        # Validación de parámetros lógicos
        if duracion_horas <= 0:
            # Simulamos un error interno de cálculo matemático (ValueError)
            error_origen = ValueError("La duración no puede ser de cero o de valor negativo.")
            
            # ENCADENAMIENTO DE EXCEPCIONES (raise ... from ...)
            # Explicación: Transformamos un error común de Python en nuestra excepción de negocio
            raise ReservaInvalidaError("No se pudo calcular la reserva debido a parámetros de tiempo inválidos.") from error_origen

        # Cálculo simulado del costo final
        costo_total = duracion_horas * costo_base

    except ReservaInvalidaError as error_reserva:
        # Capturamos la reserva fallida debido a la lógica inconsistente
        logger.registrar_reserva_fallida(f"Servicio: '{servicio_nombre}' | Motivo: {error_reserva}")
        
        # Mostramos tanto nuestro error como la causa original (gracias al encadenamiento)
        print(f" Error en Reserva: {error_reserva}")
        if error_reserva.__cause__:
            print(f"   Causa raíz del sistema: {error_reserva.__cause__}")
        return False

    except Exception as error_inesperado:
        # Captura de cualquier otro error general para no detener el sistema
        logger.registrar_error_critico(f"Fallo no controlado: {str(error_inesperado)}")
        print(f" Ocurrió un error inesperado, pero el sistema sigue en pie.")
        return False

    else:
        # Bloque ELSE: Se ejecuta únicamente si NO hubo ninguna excepción dentro del try
        logger.registrar_evento(f"Reserva exitosa para Cliente {cliente_id}. Servicio: {servicio_nombre}. Total: ${costo_total}")
        print(f" ¡Reserva Exitosa! El total del servicio '{servicio_nombre}' es: ${costo_total}")
        return True

    finally:
        # Bloque FINALLY: Se ejecuta SIEMPRE, sin importar si hubo error o éxito
        print(" Finalizando ciclo de procesamiento de la transacción de reserva.")
        print("-" * 60)

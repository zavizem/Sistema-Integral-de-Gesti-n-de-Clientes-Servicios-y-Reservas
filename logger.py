import logging

def configurar_logger():
    """
    Configura el manejador de registros (logging) del sistema.
    Redirecciona la salida a un archivo físico llamado 'logs.txt' en codificación UTF-8.
    """
    # Se configura el nivel INFO para poder capturar tanto eventos informativos como errores.
    logging.basicConfig(
        filename='logs.txt',
        filemode='a', # El modo 'a' (append) asegura que los logs se acumulen sin borrarse.
        format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )

def registrar_evento(mensaje):
    """Registra eventos generales del flujo del sistema (Operaciones exitosas)."""
    logging.info(f"EVENTO: {mensaje}")

def registrar_dato_invalido(mensaje):
    """Registra específicamente las fallas de ingreso de datos o formatos erróneos."""
    logging.warning(f"DATOS INVÁLIDOS: {mensaje}")

def registrar_reserva_fallida(mensaje):
    """Registra de manera dedicada los intentos de reserva que no se completaron."""
    logging.error(f"RESERVA FALLIDA: {mensaje}")

def registrar_error_critico(mensaje):
    """Registra errores imprevistos o críticos en el sistema."""
    logging.critical(f"ERROR CRÍTICO: {mensaje}")

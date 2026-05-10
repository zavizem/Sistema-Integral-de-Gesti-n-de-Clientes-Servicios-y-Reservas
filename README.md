# Software FJ - Sistema Integral de Gestión

## Descripción del Proyecto

Este proyecto corresponde al desarrollo de un sistema integral orientado a objetos para la empresa ficticia “Software FJ”, realizado como actividad colaborativa del curso Programación - Código 213023_62 de la Universidad Nacional Abierta y a Distancia (UNAD).

El sistema fue desarrollado utilizando el lenguaje Python y tiene como finalidad gestionar clientes, servicios y reservas sin utilizar bases de datos, aplicando principios de Programación Orientada a Objetos (POO) y manejo avanzado de excepciones.

# Funcionalidades

    Gestión de Clientes
- Registro de clientes.
- Validación de datos personales.
- Validación de correos electrónicos.

    Gestión de Servicios
- Reserva de salas.
- Alquiler de equipos.
- Asesorías especializadas.

    Gestión de Reservas
- Confirmación de reservas.
- Cancelación de reservas.
- Validación de operaciones.

    Manejo de Excepciones
- Excepciones personalizadas.
- Uso de try/except.
- Registro de errores en logs.

# Tecnologías Utilizadas

- Python 3
- GitHub
- Programación Orientada a Objetos

# Estructura del Proyecto

Software_FJ/
│
├── modelos/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── reserva.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   └── asesoria.py
│
├── excepciones/
│   ├── errores.py
│   └── logger.py
│
├── logs/
│   └── logs.txt
│
├── main.py
│
└── README.md

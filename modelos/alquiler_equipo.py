from modelos.servicio import Servicio


class AlquilerEquipo(Servicio):

    # CONSTRUCTOR
    def __init__(self, id_entidad, nombre, costo_base):

        super().__init__(
            id_entidad,
            nombre,
            costo_base
        )

    # CALCULAR COSTO
    def calcular_costo(self, duracion):

        return self._costo_base * duracion

    # DESCRIBIR SERVICIO
    def describir_servicio(self):

        return (
            "Servicio de alquiler de equipos"
        )
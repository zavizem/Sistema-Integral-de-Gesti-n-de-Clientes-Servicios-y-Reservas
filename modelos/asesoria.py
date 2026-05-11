from modelos.servicio import Servicio


class AsesoriaEspecializada(Servicio):

    def __init__(self, id_entidad, nombre, costo_base):

        super().__init__(
            id_entidad,
            nombre,
            costo_base
        )

    def calcular_costo(self, duracion):

        return self._costo_base * duracion

    def describir_servicio(self):

        return (
            "Servicio de asesoría especializada"
        )
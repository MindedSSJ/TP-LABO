# Si hereda de Persona:
from persona import Persona

class Cirujano:

    def __init__(self, nombre, especialidades, disponible=True):
        """
        especialidades: lista de órganos o tipos en los que el cirujano es experto.
        disponible: indica si puede operar actualmente.
        """
        self.nombre = nombre
        self.especialidades = especialidades  # lista de strings
        self.disponible = disponible

    def disponible_para_operar(self):
        return self.disponible

    def tiene_especialidad_para(self, organo):
        return organo in self.especialidades

    def es_general(self):
        # Asumimos que ser general significa tener la especialidad 'general'
        return 'general' in self.especialidades

    def marcar_ocupado(self):
        self.disponible = False

    def marcar_disponible(self):
        self.disponible = True

    def __str__(self):
        est = "disponible" if self.disponible else "ocupado"
        return f"Cirujano {self.nombre} ({est}), especialidades: {', '.join(self.especialidades)}"

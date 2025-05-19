#clase paciente
from persona import Persona

class Paciente(Persona):
    def __init__(self, nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud):
        super().__init__(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud)

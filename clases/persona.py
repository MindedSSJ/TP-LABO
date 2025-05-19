#clase persona
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud):
        self.nombre = nombre
        self.dni = dni
        self.nacimiento = nacimiento  # datetime.date
        self.sexo = sexo
        self.telefono = telefono
        self.tipo_sangre = tipo_sangre
        self.centro_salud = centro_salud

    def info(self):
        return (
            f"Nombre: {self.nombre}, DNI: {self.dni}, Sexo: {self.sexo}, "
            f"Telefono: {self.telefono}, Tipo de Sangre: {self.tipo_sangre}, "
            f"Centro de Salud: {self.centro_salud}"
        )

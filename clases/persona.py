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

        """
        nombre: nombre que representa de la persona
        dni: numero de dni de la persona
        nacimiento: fecha de nacimiento de la persona
        sexo: Masculino o Femenino
        telefono: numero personal de telefono de la persona
        tipo_sangre: Tipo de sangre de la persona 'A+, A-, B+, B-, AB+, AB-, O+, O-'
        centro_salud: centro de salud en el que esta registrado la persona
        """

    def info(self):
        return (
            f"Nombre: {self.nombre}, DNI: {self.dni}, Sexo: {self.sexo}, "
            f"Telefono: {self.telefono}, Tipo de Sangre: {self.tipo_sangre}, "
            f"Centro de Salud: {self.centro_salud}"
        )

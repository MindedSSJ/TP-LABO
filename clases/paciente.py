from persona import Persona
from abc import ABC, abstractmethod

class paciente(Persona):
    
    def __init__(self, donante_receptor, nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud):
        super().__init__(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud)
        self.donante_receptor = donante_receptor
        self.lista_receptores = []
        self.lista_donantes = []
   
    def paciente(self):
        super().info()
    
        return self.donante_receptor
        
    
    def donante_receptor(self):

        if self.donante_receptor == "receptor":
            self.lista_receptores.append(self)
        else:
            self.lista_donantes.append(self)

        return self.donante_receptor
    

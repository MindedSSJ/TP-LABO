from clases.persona import Persona
from abc import ABC, abstractmethod

class paciente(Persona):
    
    def __init__(self, donante_receptor):
        self.donante_receptor = donante_receptor


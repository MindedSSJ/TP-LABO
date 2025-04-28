from abc import ABC, abstractmethod

class vehiculo(ABC):
    
    def __init__(self, velocidad, registro_viajes):
        self.velocidad = velocidad
        self.registro_viajes = registro_viajes

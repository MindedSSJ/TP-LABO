from vehiculo import vehiculo

class helicoptero(vehiculo):
    
    def __init__(self, tiempo_viaje):

        self.tiempo_viaje = tiempo_viaje
    
    def tiempor_viaje(self, distancia):
        return vehiculo.velocidad / distancia
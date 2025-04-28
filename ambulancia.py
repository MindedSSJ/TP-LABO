from vehiculo import vehiculo

class ambulancia(vehiculo):

    def __init__(self, tiempo_viaje, trafico):

        self.tiempo_viaje = tiempo_viaje
        self.trafico = trafico
        
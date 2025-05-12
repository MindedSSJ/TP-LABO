class vehiculo:
    def _init_(self, tipo, velocidad):
        self.tipo = tipo  # "ambulancia", "helicoptero", "avion"
        self.velocidad = velocidad  # km/h
        self.registro_viajes = []  # lista con info de viajes

    def calcular_tiempo_viaje(self, distancia, trafico=0):
        """
        Calcula tiempo de viaje en horas.
        Los vehículos aéreos ignoran el tráfico.
        """
        if self.tipo in ["helicoptero", "avion"]:
            tiempo = distancia / self.velocidad
        else:
            tiempo = (distancia / self.velocidad) + trafico
        return round(tiempo, 2)

    def registrar_viaje(self, origen, destino, distancia, trafico):
        tiempo = self.calcular_tiempo_viaje(distancia, trafico)
        viaje = {
            "origen": origen.nombre,
            "destino": destino.nombre,
            "distancia": distancia,
            "trafico": trafico,
            "tiempo_estimado": tiempo
        }
        self.registro_viajes.append(viaje)
        return tiempo
import random

class Vehiculo:
    def __init__(self, tipo, velocidad):
        tipos_validos = ['ambulancia', 'helicoptero', 'avion']
        if tipo not in tipos_validos:
            raise ValueError(f"Tipo de vehículo debe ser uno de {tipos_validos}")
        
        self.tipo = tipo
        self.velocidad = velocidad  # km/h
        self.viajes_realizados = []  # lista de tuplas: (distancia, trafico, tiempo_estimado)

    def calcular_tiempo(self, distancia, trafico):
        """
        Calcula el tiempo que tarda el vehículo en llegar.
        Si es aéreo, ignora el tráfico.
        """
        if self.tipo in ['helicoptero', 'avion']:
            tiempo = distancia / self.velocidad
        else:
            tiempo = (distancia + trafico) / self.velocidad
        
        # Guardar registro del viaje
        self.viajes_realizados.append((distancia, trafico, round(tiempo, 2)))
        return round(tiempo, 2)

    def __str__(self):
        return f"Vehículo tipo {self.tipo} con velocidad {self.velocidad} km/h"

    def mostrar_viajes(self):
        print(f"\n🛣️ Viajes realizados por {self.tipo}:")
        for i, (distancia, trafico, tiempo) in enumerate(self.viajes_realizados, 1):
            info = f"{i}. Distancia: {distancia} km, "
            if self.tipo == "ambulancia":
                info += f"Tráfico: {trafico}, "
            info += f"Tiempo estimado: {tiempo} horas"
            print(info)

class Vehiculo():

    def __init__(self, tipo, velocidad):
        """
        tipo: 'ambulancia', 'helicoptero' o 'avion'
        velocidad: número que representa la velocidad relativa para seleccionar el mejor vehículo
        """
        tipos_validos = ['ambulancia', 'helicoptero', 'avion']
        if tipo not in tipos_validos:
            raise ValueError(f"Tipo de vehículo debe ser uno de {tipos_validos}")
        self.tipo = tipo
        self.velocidad = velocidad

    def __str__(self):
        return f"Vehículo tipo {self.tipo} con velocidad {self.velocidad}"

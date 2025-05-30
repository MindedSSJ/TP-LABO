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
        if self.tipo == "ambulancia":
            self.velocidad = 100
        elif self.tipo == "elicoptero" or self.tipo == "avion":
            self.velocidad = 200
            
        return f"Vehículo tipo {self.tipo} con velocidad {self.velocidad}"
    
class Organo():
    def __init__(self, tipo_organos, fecha_ablacion, hora_ablacion):
        """
        tipo_organos: diferentes tipos de organos "corazón, hígado, páncreas, huesos, riñón, pulmones,
        intestino, piel y córneas"
        fecha_ablacion: fecha en la que se realiza la extracción quirurgica de un organo
        hora_ablacion: Hora en la que se realiza la extraccion quirurgica de un organo
        """


        self.tipo_organos = tipo_organos.lower()
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.disponible = True  # por defecto está disponible

    def marcar_donado(self):
        """
        funcion que marca como donado un organo
        """
        self.disponible = False

    def esta_disponible(self):
        """
        funcion que marca si un organo esta disponible
        """
        return self.disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Asignado"
        return f"{self.tipo_organos.capitalize()} ({self.fecha_ablacion} {self.hora_ablacion}) - {estado}"

    def __eq__(self, other):
        return self.tipo_organos == other.tipo_organos and self.fecha_ablacion == other.fecha_ablacion

class Organo():
    def __init__(self, tipo_organos, fecha_ablacion, hora_ablacion):
        self.tipo_organos = tipo_organos.lower()
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.disponible = True  # por defecto está disponible

    def marcar_donado(self):
        self.disponible = False

    def esta_disponible(self):
        return self.disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Asignado"
        return f"{self.tipo_organos.capitalize()} ({self.fecha_ablacion} {self.hora_ablacion}) - {estado}"

    def __eq__(self, other):
        return self.tipo_organos == other.tipo_organos and self.fecha_ablacion == other.fecha_ablacion

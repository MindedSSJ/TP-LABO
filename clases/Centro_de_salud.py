from vehiculo import Vehiculo
from cirujano import Cirujano

class CentroDeSalud:
    def __init__(self, nombre, direccion, partido, provincia, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono
        self.cirujanos = []
        self.vehiculos = []

    def agregar_cirujano(self, cirujano):
        """Agrega un cirujano a la lista de cirujanos del centro."""
        self.cirujanos.append(cirujano)

    def agregar_vehiculo(self, vehiculo):
        """Agrega un vehículo a la lista de vehículos del centro."""
        self.vehiculos.append(vehiculo)

    def asignar_cirujano(self, tipo_organo):
        """
        Busca un cirujano especializado en el tipo de órgano.
        Si no hay, intenta encontrar uno general.
        """
        for cirujano in self.cirujanos:
            if cirujano.disponible_para_operar() and cirujano.tiene_especialidad_para(tipo_organo):
                cirujano.marcar_ocupado()
                return cirujano

        for cirujano in self.cirujanos:
            if cirujano.disponible_para_operar() and cirujano.es_general():
                cirujano.marcar_ocupado()
                return cirujano

        return None  # No hay cirujanos disponibles

    def asignar_vehiculo(self, destino):
        """
        Asigna el tipo de vehículo adecuado según la distancia:
        - Misma provincia y mismo partido: ambulancia
        - Misma provincia, distinto partido: helicóptero
        - Distinta provincia: avión
        """
        if self.provincia != destino.provincia:
            tipo_necesario = "avion"
        elif self.partido != destino.partido:
            tipo_necesario = "helicoptero"
        else:
            tipo_necesario = "ambulancia"

        # Filtrar vehículos por tipo y ordenarlos por velocidad (mayor primero)
        vehiculos_filtrados = [v for v in self.vehiculos if v.tipo == tipo_necesario]
        if not vehiculos_filtrados:
            return None

        vehiculos_filtrados.sort(key=lambda v: v.velocidad, reverse=True)
        return vehiculos_filtrados[0]

    def __str__(self):
        return f"{self.nombre} - {self.direccion}, {self.partido}, {self.provincia} (Tel: {self.telefono})"

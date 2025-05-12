class CentroDeSalud:
    def _init_(self, nombre, direccion, partido, provincia, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono
        self.cirujanos = []
        self.vehiculos = []

    def agregar_cirujano(self, cirujano):
        self.cirujanos.append(cirujano)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def asignar_cirujano(self, organo):
        for cirujano in self.cirujanos:
            if cirujano.disponible_para_operar() and cirujano.tiene_especialidad_para(organo):
                cirujano.marcar_ocupado()
                return cirujano
        # Si no hay especializado, buscar general
        for cirujano in self.cirujanos:
            if cirujano.disponible_para_operar() and cirujano.es_general():
                cirujano.marcar_ocupado()
                return cirujano
        return None  # No hay cirujanos disponibles

    def asignar_vehiculo(self, destino):
        if self.provincia != destino.provincia:
            tipo = "avion"
        elif self.partido != destino.partido:
            tipo = "helicoptero"
        else:
            tipo = "ambulancia"

        vehiculos_filtrados = [v for v in self.vehiculos if v.tipo == tipo]
        if not vehiculos_filtrados:
            return None

        # Elegir el de mayor velocidad
        vehiculos_filtrados.sort(key=lambda v: v.velocidad, reverse=True)
        return vehiculos_filtrados[0]
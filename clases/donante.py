#clase donante
from paciente import Paciente

class Donante(Paciente):
    def __init__(self, nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud,
                 fecha_muerte, hora_muerte, fecha_ablacion, hora_ablacion, lista_organos):
        super().__init__(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud)
        self.fecha_muerte = fecha_muerte
        self.hora_muerte = hora_muerte
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.lista_organos = lista_organos  # Lista de objetos Organo

    def tiene_organos(self):
        if not self.lista_organos:
            print("El donante no tiene órganos viables para donar")
        else:
            print(f"{[organo.tipo for organo in self.lista_organos]} son los órganos viables para donar del paciente")

    def organo_donado(self, tipo_organo):
        for organo in self.lista_organos:
            if organo.tipo == tipo_organo:
                self.lista_organos.remove(organo)
                print(f"Órgano '{tipo_organo}' donado.")
                return organo
        print(f"No se encontró el órgano '{tipo_organo}' en la lista del donante.")
        return None

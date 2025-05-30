#clase donante
from .paciente import Paciente
from .organos import Organo  # asegurate que el archivo se llame organo.py

class Donante(Paciente):
    def __init__(self, nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud,
                 fecha_muerte, hora_muerte, fecha_ablacion, hora_ablacion, lista_organos):
        """
        nombre: nombre que representa al donante
        dni: numero de dni del donante
        nacimiento: fecha de nacimiento del donante
        sexo: Masculino o Femenino
        telefono: numero personal de telefono del donante
        tipo_sangre: Tipo de sangre del donante 'A+, A-, B+, B-, AB+, AB-, O+, O-'
        centro_salud: centro de salud en el que esta registrado el donante
        fecha_muerte: fecha en la que el donante fallecio
        hora_muerte: hora exacta en la que el donante fallecio
        fecha_ablacion: fecha en la que se realiza la extracción quirurgica de un organo
        hora_ablacion: Hora en la que se realiza la extraccion quirurgica de un organo
        lista_organos: lista de los organos donados por el fallecido 
        """
        
        super().__init__(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud)
        self.fecha_muerte = fecha_muerte
        self.hora_muerte = hora_muerte
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.lista_organos = lista_organos  # lista de objetos Organo

    def tiene_organos(self):
        disponibles = [organo for organo in self.lista_organos if organo.esta_disponible()]
        if not disponibles:
            print("El donante no tiene órganos viables para donar.")
            return False
        print("Órganos viables para donar:")
        for organo in disponibles:
            print(f" - {organo}")
            return True
    
    def organo_donado(self, tipo_organo):
        """
        Busca un órgano disponible del tipo indicado, lo elimina de la lista y lo devuelve.
        Si no lo encuentra, devuelve None.
        """
        for organo in self.lista_organos:
            if organo.tipo_organos == tipo_organo.lower() and organo.esta_disponible():
                self.lista_organos.remove(organo)
                print(f"Órgano '{tipo_organo}' extraído de la lista del donante.")
                return organo
        print(f"No se encontró un órgano disponible de tipo '{tipo_organo}'.")
        return None


    def __str__(self):
        return f"Donante: {self.nombre} (DNI: {self.dni}) - Centro: {self.centro_salud.nombre}"

from .donante import Donante
from .receptor import Receptor
from .Centro_de_salud import CentroDeSalud


class Incucai:
    def __init__(self):
        self.lista_donantes = []
        self.lista_receptores = []
        self.lista_centros_salud = []

    def agregar_donante(self, donante):
        self.lista_donantes.append(donante)

    def agregar_receptor(self, receptor):
        self.lista_receptores.append(receptor)

    def agregar_centro_salud(self, centro):
        self.lista_centros_salud.append(centro)

    def buscar_match(self, receptor):
        """
        Busca un donante compatible con el receptor (por tipo de sangre y órgano).
        Devuelve el primer match que encuentre.
        """
        for donante in self.lista_donantes:
            if receptor.tipo_sangre == donante.tipo_sangre:
                for organo in donante.lista_organos:
                    if organo.tipo_organos == receptor.organo_necesitado:
                        return donante, organo
        return None, None

    def coordinar_trasplante(self, donante, receptor):
        """
        Coordina la asignación de cirujano y vehículo, si hay match.
        """
        centro_donante = donante.centro_salud
        centro_receptor = receptor.centro_salud

        # Asignar cirujano
        cirujano = centro_donante.asignar_cirujano(receptor.organo_necesitado)
        if not cirujano:
            print("No hay cirujano disponible para este órgano.")
            return False

        # Asignar vehículo
        vehiculo = centro_donante.asignar_vehiculo(centro_receptor)
        if not vehiculo:
            print("No hay vehículo disponible para trasladar el órgano.")
            return False

        # Sacar el órgano del donante
        organo_donado = donante.organo_donado(receptor.organo_necesitado)
        if not organo_donado:
            print("El órgano ya fue asignado o no está disponible.")
            return False

        print(f"Match y coordinación exitosa:")
        print(f"   - Donante: {donante.nombre}")
        print(f"   - Receptor: {receptor.nombre}")
        print(f"   - Cirujano asignado: {cirujano.nombre}")
        print(f"   - Vehículo asignado: {vehiculo.tipo} a {vehiculo.velocidad} km/h")
        return True

    def __str__(self):
        return (f"INCUCAI - Donantes: {len(self.lista_donantes)}, "
                f"Receptores: {len(self.lista_receptores)}, "
                f"Centros de Salud: {len(self.lista_centros_salud)}")

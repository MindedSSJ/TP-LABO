#clase receptor
from .paciente import Paciente
from  .organos import Organo

class Receptor(Paciente):
    def __init__(self, nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud,
                 organo_necesitado, fecha_listado, prioridad, patologia, estado):
        """
        nombre: nombre que representa al receptor
        dni: numero de dni del receptor
        nacimiento: fecha de nacimiento del receptor
        sexo: Masculino o Femenino
        telefono: numero personal de telefono del receptor
        tipo_sangre: Tipo de sangre del receptor 'A+, A-, B+, B-, AB+, AB-, O+, O-'
        centro_salud: centro de salud en el que esta registrado el receptor
        organo_necesitado: organo que necesita para transplante el receptor
        fecha_listado: fecha en la que fue ingresado y admitido en la lista de receptores
        prioridad: prioridad que tiene el receptor, 'alta, media, baja'
        patologia: patologia que contiene el receptor
        estado: estado del receptor, 'estable o inestable'
        """

        super().__init__(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud)

        self.organo_necesitado = organo_necesitado  # string: "corazón", "hígado", etc.
        self.fecha_listado = fecha_listado  # datetime.date
        self.prioridad = prioridad  # número entero
        self.patologia = patologia
        self.estado = estado  # "Estable" o "Inestable"

    def match(self, donante):
        """
        Verifica si el donante tiene un órgano compatible con el receptor.
        Coincide por tipo de órgano y tipo de sangre.
        """
        for organo in donante.lista_organos:
            if organo.tipo_organos == self.organo_necesitado and donante.tipo_sangre == self.tipo_sangre:
                print(f"Match encontrado para el paciente {self.nombre}, órgano otorgado por {donante.nombre}")
                return True
        print(f"No hay match para el receptor {self.nombre}")
        return False

    def cambio_prioridad(self):
        """
        Si el trasplante falla, se eleva la prioridad y se cambia el estado a 'Inestable'.
        """
        self.prioridad = 1  # Asumiendo que 1 es la máxima prioridad
        self.estado = "Inestable"
        print(f"La prioridad de {self.nombre} fue actualizada a {self.prioridad} y su estado a {self.estado}.")
        return self.prioridad, self.estado

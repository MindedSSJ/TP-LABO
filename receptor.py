from paciente import paciente

class receptor(paciente):
    
    def __init__(self, organo_necesitado, fecha_listado, prioridad, patologia, estado):

        self.organo_necesitado = organo_necesitado
        self.fecha_listado = fecha_listado
        self.prioridad = prioridad
        self.patologia = patologia
        self.estado = estado
        
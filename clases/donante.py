from paciente import paciente

class donante(paciente):
    
    def __init__(self, fecha_muerte, hora_muerte, fecha_ablacion, hora_ablacion, lista_organos):

        self.fecha_muerte = fecha_muerte
        self.hora_muerte = hora_muerte
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.lista_organos = []
        
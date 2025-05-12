from paciente import paciente

class receptor(paciente):
    
    def __init__(self, nombre, dni, tipo_sangre, organo_necesitado, nacimiento, sexo, telefono, centro_salud, fecha_listado,
                  prioridad, patologia, estado):
        
        super().__init__(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud)

        self.organo_necesitado = organo_necesitado
        self.fecha_listado = fecha_listado
        self.prioridad = prioridad
        self.patologia = patologia
        self.estado = estado
        

        def match(self, donante):
            #preguntar a agus si no deberiamos hacer tambien que el tipo de sangre coincida para hacer el match
            
            if self.organo_necesitado in donante.lista_organo and self.tipo_sangre == donante.tipo_sangre:
                print("Match encontrado para el paciente {receptor.nombre}, organo otorgano por {donante.nombre}")
                return True
            else:
                print("no hay match para el receptor {receptor.nombre}")
                return False
            
        def cambio_prioridad(self):
            #preguntar agus jeje
            return
            
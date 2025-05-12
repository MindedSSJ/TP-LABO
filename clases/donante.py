from paciente import paciente

class donante(paciente):
    
    def __init__(self, nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud, fecha_muerte, hora_muerte, fecha_ablacion,
                  hora_ablacion, lista_organos):
        super().__init__(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud)
        
        self.fecha_muerte = fecha_muerte
        self.hora_muerte = hora_muerte
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.lista_organos = lista_organos

        super().__init__(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud)
        
        def tiene_organos(self):

            if self.lista_organos == None:
                print("El donante no tiene organos viables para donar")
            else:
                print("{self.lista_organos} son los organos viables para donar del paciente")
                
        
        def organo_donado(self, tipo_organo):
          """
            Marca un órgano como donado y lo remueve de la lista de órganos.
            Si el órgano no está disponible, devuelve un mensaje de error.
          """
          for organo in self.lista_organos:
              if organo.tipo == tipo_organo:
                  self.lista_organos.remove(organo)
                  print("Organo '{tipo_organo}'")
                  return organo
              else:
                  print("no se encontro el organo '{tipo_organo}' en la lista del donante")
                  return None
                  
              






                
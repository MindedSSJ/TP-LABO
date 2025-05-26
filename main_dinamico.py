from clases.organos import Organo
from clases.Centro_de_salud import *
from clases.incuncai import *

def crear_centro_salud():
    try:
        nombre = input("Nombre del centro de salud: ")
        direccion = input("Dirección: ")
        partido = input("Partido: ")
        provincia = input("Provincia: ")
        telefono = int(input("Teléfono: "))
        return CentroDeSalud(nombre, direccion, partido, provincia, telefono)
    except Exception as e:
        print(f"[ERROR] al crear centro de salud: {e}")
        return None

def crear_donante(centro_salud):
    try:
        nombre = input("Nombre del donante: ")
        dni = int(input("DNI: "))
        nacimiento = int(input("Fecha de nacimiento (YYYY-MM-DD): "))
        sexo = input("Sexo (M/F): ")
        telefono = int(input("Teléfono: "))
        tipo_sangre = input("Tipo de sangre: ")
        fecha_muerte = int(input("Fecha de muerte (YYYY-MM-DD): "))
        hora_muerte = int(input("Hora de muerte (HH:MM): "))
        fecha_ablacion = int(input("Fecha de ablación (YYYY-MM-DD): "))
        hora_ablacion = int(input("Hora de ablación (HH:MM): "))

        organos = []
        while True:
            tipo = input("Órgano a agregar (o 'fin' para terminar): ")
            if tipo.lower() == 'fin':
                break
            organos.append(Organo(tipo, fecha_ablacion, hora_ablacion))

        return Donante(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro_salud,
                       fecha_muerte, hora_muerte, fecha_ablacion, hora_ablacion, organos)
    except Exception as e:
        print(f"[ERROR] al crear donante: {e}")
        return None

def crear_receptor(centro_salud):
    try:
        nombre = input("Nombre del receptor: ")
        dni = int(input("DNI: "))
        nacimiento = int(input("Fecha de nacimiento (YYYY-MM-DD): "))
        sexo = input("Sexo (M/F): ")
        telefono = int(input("Teléfono: "))
        tipo_sangre = input("Tipo de sangre: ")
        organo_necesitado = input("Órgano necesario: ")
        fecha_listado = int(input("Fecha de ingreso al listado (YYYY-MM-DD): "))
        prioridad = int(input("Prioridad (1=alta, 2=media, 3=baja): "))
        patologia = input("Patología: ")
        estado = input("Estado: ")

        return Receptor(nombre, dni, tipo_sangre, organo_necesitado, nacimiento, sexo,
                        telefono, centro_salud, fecha_listado, prioridad, patologia, estado)
    except Exception as e:
        print(f"[ERROR] al crear receptor: {e}")
        return None

def main():
    try:
        print("=== INICIO DEL SISTEMA INCUCAI ===")

        print("Por favor, ingrese los datos del centro de salud, donante y receptor.")
        print("Si no desea ingresar alguno, deje el campo vacío.")
        centro = crear_centro_salud()
        if not centro:
            return

        incucai = Incucai()
        incucai.agregar_centro_salud(centro)

        print("Ingrese los datos del donante y receptor.")
        donante = crear_donante(centro)
        if donante:
            incucai.agregar_donante(donante)

        receptor = crear_receptor(centro)
        if receptor:
            incucai.agregar_receptor(receptor)
        

        if receptor and donante:
            print("\n== Buscando MATCH entre donante y receptor ==")
            if receptor.match(donante):
                organo_donado = donante.organo_donado(receptor.organo_necesitado)
                if organo_donado:
                    print(f"Órgano {organo_donado.tipo} asignado a {receptor.nombre}")
                else:
                    print("No se pudo donar el órgano")
            else:
                print("No se encontró match")

    except Exception as e:
        print(f"[ERROR] General: {e}")

if __name__ == "__main__":
    main()

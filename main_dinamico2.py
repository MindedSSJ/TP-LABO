from clases.organos import Organo
from clases.Centro_de_salud import *
from clases.incuncai import *


def input_sexo(mensaje):
    valor_valido = {"M", "F"}
    while True:
        valor = input(mensaje).upper()
        if valor in valor_valido:
            return valor
        else:
            print("Genero no aceptado. Intente con M = Masculino, F = femenino")
def input_sangre(mensaje):
    valor_valido = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
    while True:
        valor = input(mensaje).upper()
        if valor  in valor_valido:
            return valor
        else:
            print("Tipo de sangre no válido. Intente con A+, A-, B+, B-, AB+, AB-, O+ u O-.") 

def input_numerico(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("❌ Por favor, ingrese solo números.")
def input_texto(mensaje):
    while True:
        valor = input(mensaje)
        if valor.replace(" ", "").isalpha():
            return valor
        else:
            print("❌ Por favor, ingrese solo letras.")

def crear_centro_salud():
    try:
        nombre = input("Nombre del centro de salud: ")
        direccion = input("Dirección: ")
        partido = input_texto("Partido: ")
        provincia = input_texto("Provincia: ")
        telefono = input_numerico("Teléfono: ")
        return CentroDeSalud(nombre, direccion, partido, provincia, telefono)
    except Exception as e:
        print(f"[ERROR] al crear centro de salud: {e}")
        return None

def crear_donante(centro_salud):
    try:
        nombre = input_texto("Nombre del donante: ")
        dni = input_numerico("DNI: ")
        nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
        sexo = input_sexo("Sexo (M/F): ")
        telefono = input_numerico("Teléfono: ")
        tipo_sangre = input_sangre("Tipo de sangre: ")
        fecha_muerte = input_numerico("Fecha de muerte (YYYY-MM-DD): ")
        hora_muerte = input_numerico("Hora de muerte (HH:MM): ")
        fecha_ablacion = input_numerico("Fecha de ablación (YYYY-MM-DD): ")
        hora_ablacion = input_numerico("Hora de ablación (HH:MM): ")

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
        nombre = input_texto("Nombre del receptor: ")
        dni = input_numerico("DNI: ")
        nacimiento = input_numerico("Fecha de nacimiento (YYYY-MM-DD): ")
        sexo = input_sexo("Sexo (M/F): ")
        telefono = input_numerico("Teléfono: ")
        tipo_sangre = input_sangre("Tipo de sangre: ")
        organo_necesitado = input("Órgano necesario: ")
        fecha_listado = input("Fecha de ingreso al listado (YYYY-MM-DD): ")
        prioridad = input_numerico("Prioridad (1=alta, 2=media, 3=baja): ")
        patologia = input("Patología: ")
        estado = input_texto("Estado: ")

        return Receptor(nombre, dni, tipo_sangre, organo_necesitado, nacimiento, sexo,
                        telefono, centro_salud, fecha_listado, prioridad, patologia, estado)
    except Exception as e:
        print(f"[ERROR] al crear receptor: {e}")
        return None

def main():
    try:
        print("\n=== SISTEMA INCUCAI - CARGA Y MATCH DE PACIENTES ===\n")

        centro = crear_centro_salud()
        if not centro:
            return

        incucai = Incucai()
        incucai.agregar_centro_salud(centro)

        donante = crear_donante(centro)
        if donante:
            incucai.agregar_donante(donante)

        receptor = crear_receptor(centro)
        if receptor:
            incucai.agregar_receptor(receptor)

        if receptor and donante:
            print("\n🔍 Buscando MATCH entre donante y receptor...\n")
            if receptor.match(donante):
                organo_donado = donante.organo_donado(receptor.organo_necesitado)
                if organo_donado:
                    print(f"✅ Órgano '{organo_donado.tipo}' asignado a {receptor.nombre}")
                else:
                    print("❌ El órgano no está disponible para donar.")
            else:
                print("❌ No se encontró compatibilidad entre donante y receptor.")

    except Exception as e:
        print(f"[ERROR GENERAL]: {e}")

if __name__ == "__main__":
    main()


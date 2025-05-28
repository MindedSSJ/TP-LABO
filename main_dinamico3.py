from clases.organos import Organo
from clases.Centro_de_salud import *
from clases.incuncai import *
from datetime import datetime

donantes = []
receptores = []
centros_salud = []

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


def seleccionar_centro():
    if not centros_salud:
        print("⚠️ No hay centros registrados.")
        return None
    print("\nCentros de Salud disponibles:")
    for i, c in enumerate(centros_salud):
        print(f"{i+1}. {c.nombre} ({c.provincia} - {c.partido})")
    while True:
        try:
            opcion = int(input("Seleccione un centro por número: "))
            if 1 <= opcion <= len(centros_salud):
                return centros_salud[opcion - 1]
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Ingrese un número válido.")

def cargar_centro_salud():
    print("\n🏥 Cargando nuevo Centro de Salud:")
    nombre = input_texto("Nombre: ")
    direccion = input("Dirección: ")
    partido = input("Partido: ")
    provincia = input("Provincia: ")
    telefono = input_numerico("Teléfono: ")
    
    centro = CentroDeSalud(nombre, direccion, partido, provincia, telefono)
    centros_salud.append(centro)
    print("✅ Centro de Salud registrado.\n")

def cargar_donante():
    print("\n🫀 Cargando nuevo Donante:")
    centro = seleccionar_centro()
    if not centro:
        return

    nombre = input_texto("Nombre: ")
    dni = input_numerico("DNI: ")
    nacimiento = input_numerico("Fecha de nacimiento (YYYY-MM-DD): ")
    sexo = input_texto("Sexo (M/F): ")
    telefono = input_numerico("Teléfono: ")
    tipo_sangre = input_sangre("Tipo de sangre: ")
    fecha_muerte = input_numerico("Fecha de muerte (YYYY-MM-DD): ")
    hora_muerte = input_numerico("Hora de muerte (HH:MM): ")
    fecha_ablacion = input_numerico("Fecha de ablación (YYYY-MM-DD): ")
    hora_ablacion = input_numerico("Hora de ablación (HH:MM): ")

    lista_organos = []
    while True:
        tipo_organos = input("Agregar órgano a donar (escriba 'fin' para terminar): ").lower()
        if tipo_organos == "fin":
            break
        lista_organos.append(Organo(tipo_organos, fecha_ablacion, hora_ablacion))

    donante = Donante(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro,
                      fecha_muerte, hora_muerte, fecha_ablacion, hora_ablacion, lista_organos)
    donantes.append(donante)
    print("✅ Donante registrado.\n")

def cargar_receptor():
    print("\n💉 Cargando nuevo Receptor:")
    centro = seleccionar_centro()
    if not centro:
        return

    nombre = input_texto("Nombre: ")
    dni = input_numerico("DNI: ")
    nacimiento = input_numerico("Fecha de nacimiento (YYYY-MM-DD): ")
    sexo = input_sexo("Sexo (M/F): ")
    telefono = input_numerico("Teléfono: ")
    tipo_sangre = input_sangre("Tipo de sangre: ")
    organo_necesitado = input_texto("Órgano que necesita: ")
    fecha_listado = input_numerico("Fecha de ingreso al listado (YYYY-MM-DD): ")
    prioridad = input_numerico("Prioridad (1-5): ")
    patologia = input("Patología: ")
    estado = input("Estado actual: ")

    receptor = Receptor(nombre, dni, tipo_sangre, organo_necesitado, nacimiento, sexo,
                        telefono, centro, fecha_listado, prioridad, patologia, estado)
    receptores.append(receptor)
    print("✅ Receptor registrado.\n")

def ver_listas():
    print("\n🏥 Centros de Salud registrados:")
    for c in centros_salud:
        print(f"- {c.nombre} ({c.provincia} - {c.partido})")

    print("\n📋 Donantes registrados:")
    for d in donantes:
        print(f"🧑 {d.nombre} - Órganos: {[o.tipo_organos for o in d.lista_organos]}")

    print("\n📋 Receptores registrados:")
    for r in receptores:
        print(f"🧑 {r.nombre} - Necesita: {r.organo_necesitado}")


def main():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Centro de Salud")
        print("2. Registrar Donante")
        print("3. Registrar Receptor")
        print("4. Ver Listados")
        print("5. Ejecutar el sistema")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_centro_salud()
        elif opcion == "2":
            cargar_donante()
        elif opcion == "3":
            cargar_receptor()
        elif opcion == "4":
            ver_listas()
        elif opcion == "5":
            print("\n🔄 Ejecutando el sistema...")
            if not donantes or not receptores:
                print("⚠️ No hay donantes o receptores registrados.")
                continue
            
            for receptor in receptores:
                for donante in donantes:
                    if receptor.match(donante):
                        organo_donado = donante.organo_donado(receptor.organo_necesitado)
                        if organo_donado:
                            print(f"✅ Órgano {organo_donado.tipo_organos} asignado a {receptor.nombre}")
                        else:
                            print(f"❌ No se pudo donar el órgano a {receptor.nombre}")
            print("🔄 Sistema ejecutado con éxito.\n")
        elif opcion == "6":
            print("👋 Cerrando sistema...")
            break
        else:
            print("❌ Opción inválida, intentá nuevamente.")

if __name__ == "__main__":
    main()

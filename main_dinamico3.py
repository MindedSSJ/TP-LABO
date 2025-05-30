from clases.organos import Organo
from clases.Centro_de_salud import *
from clases.incuncai import *
from datetime import datetime

"""
Este sistema permite gestionar un banco de órganos, registrando donantes y receptores, sus organos disponibles y/o necesarios, 
así como los centros de salud y cirujanos disponibles para realizar las ablaciones y trasplantes. Tambien lleva a cabo la 
asignación de órganos a receptores según su compatibilidad y prioridad.
"""


donantes = []
receptores = []
centros_salud = []

def input_fecha(mensaje):
    """ 
    Solicita una fecha valida al usuario en el formato de YYYY-MM-DD.
    Si el formato es incorrecto, solicita nuevamente la fecha.
    """
    while True:
        valor = input(mensaje)
        try:
            return datetime.strptime(valor, "%Y-%m-%d").date()
        except ValueError:
            print("Formato incorrecto. Use YYYY-MM-DD (incluya el guión).")
def input_hora(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return datetime.strptime(valor, "%H:%M").time()
        except ValueError:
            print("Formato de hora incorrecto. Use HH:MM (incluya los dos puntos).")
def input_sexo(mensaje):
    """
    Solicita el sexo del donante o receptor en el formato pedido.
    Si el valor ingresado no es válido, solicita nuevamente.
    """
    valor_valido = {"M", "F"}
    while True:
        valor = input(mensaje).upper()
        if valor in valor_valido:
            return valor
        else:
            print("Genero no aceptado. Intente con M = Masculino, F = femenino")

def input_sangre(mensaje):
    """
    Solicita el tipo de sangre del donante o receptor.
    Si el valor ingresado no es válido, solicita nuevamente.
    """
    valor_valido = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
    while True:
        valor = input(mensaje).upper()
        if valor  in valor_valido:
            return valor
        else:
            print("Tipo de sangre no válido. Intente con A+, A-, B+, B-, AB+, AB-, O+ u O-.") 

def input_numerico(mensaje):
    """ 
    Solicita un valor numérico valido al usuario.
    Si el valor ingresado no es un número, solicita nuevamente.
    """
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("Por favor, ingrese solo números.")
def input_texto(mensaje):
    """
    Solicita un texto en el formato pedido al usuario.
    Si el valor ingresado no es válido (contiene números o caracteres especiales), solicita nuevamente.
    """
    while True:
        valor = input(mensaje)
        if valor.replace(" ", "").isalpha():
            return valor
        else:
            print("Por favor, ingrese solo letras.")


def seleccionar_centro():
    """ 
    Muestra una lista de centros de salud registrados y permite al usuario seleccionar uno.
    Si no hay centros registrados, informa al usuario y retorna None.
    """
    if not centros_salud:
        print("No hay centros registrados.")
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
    """
    Solicita al usuario los datos necesarios para crear un nuevo centro de salud y lo agrega a la lista de centros.
    Si los datos ingresados son incorrectos, informa al usuario y no agrega el centro.
    """
    print("\nCargando nuevo Centro de Salud:")
    nombre = input_texto("Nombre: ")
    direccion = input("Dirección: ")
    partido = input("Partido: ")
    provincia = input("Provincia: ")
    telefono = input_numerico("Teléfono: ")
    
    centro = CentroDeSalud(nombre, direccion, partido, provincia, telefono)
    centros_salud.append(centro)
    print("✅ Centro de Salud registrado.\n")

def cargar_donante():
    """ 
    Solicita al usuario los datos necesarios para crear un nuevo donante y lo agrega a la lista de donantes.
    Si los datos ingresados son incorrectos, informa al usuario y no agrega el donante.
    """
    print("\n🫀 Cargando nuevo Donante:")
    centro = seleccionar_centro()
    if not centro:
        return

    nombre = input_texto("Nombre: ")
    dni = input_numerico("DNI: ")
    nacimiento = input_fecha("Fecha de nacimiento (YYYY-MM-DD): ")
    sexo = input_sexo("Sexo (M/F): ")
    telefono = input_numerico("Teléfono: ")
    tipo_sangre = input_sangre("Tipo de sangre: ")
    fecha_muerte = input_fecha("Fecha de muerte (YYYY-MM-DD): ")
    hora_muerte = input_hora("Hora de muerte (HH:MM): ")
    fecha_ablacion = input_fecha("Fecha de ablación (YYYY-MM-DD): ")
    hora_ablacion = input_hora("Hora de ablación (HH:MM): ")

    lista_organos = []
    while True:
        tipo_organos = input("Agregar órgano a donar (escriba 'fin' para terminar): ").lower()
        if tipo_organos == "fin":
            break
        lista_organos.append(Organo(tipo_organos, fecha_ablacion, hora_ablacion))

    donante = Donante(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro,
                      fecha_muerte, hora_muerte, fecha_ablacion, hora_ablacion, lista_organos)
    donantes.append(donante)
    Incucai.agregar_donante(donante) # Agregar el donante a la lista de Incucai
    # Agregar el donante a la lista de Incucai

    print("✅ Donante registrado.\n")

def cargar_receptor():
    """
    Solicita al usuario los datos necesarios para crear un nuevo receptor y lo agrega a la lista de receptores.
    Si los datos ingresados son incorrectos, informa al usuario y no agrega el receptor.
    """
    print("\nCargando nuevo Receptor:")
    centro = seleccionar_centro()
    if not centro:
        return

    nombre = input_texto("Nombre: ")
    dni = input_numerico("DNI: ")
    nacimiento = input_fecha("Fecha de nacimiento (YYYY-MM-DD): ")
    sexo = input_sexo("Sexo (M/F): ")
    telefono = input_numerico("Teléfono: ")
    tipo_sangre = input_sangre("Tipo de sangre: ")
    organo_necesitado = input_texto("Órgano que necesita: ").lower()
    fecha_listado = input_fecha("Fecha de ingreso al listado (YYYY-MM-DD): ")
    prioridad = input_numerico("Prioridad (1-5): ")
    patologia = input("Patología: ")
    estado = input("Estado actual: ")

    receptor = Receptor(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro,
                 organo_necesitado, fecha_listado, prioridad, patologia, estado)
    
    receptores.append(receptor)
    # Agregar el receptor a la lista de Incucai
    Incucai.agregar_receptor(receptor)
    print("Receptor registrado.\n")

def ver_listas():
    """ 
    Muestra los listados de centros de salud, donantes y receptores registrados.
    """
    print("\n🏥 Centros de Salud registrados:")
    for c in centros_salud:
        print(f"- {c.nombre} ({c.provincia} - {c.partido})")

    print("\nDonantes registrados:") #error
    for d in Incucai.lista_donantes:
        print(f"{d.nombre} - DNI: {d.dni}, Tipo de Sangre: {d.tipo_sangre}, Fecha de Ablación: {d.fecha_ablacion}, Hora de Ablación: {d.hora_ablacion}")
        print(f"{d.nombre} - Órganos: {[o.tipo_organos for o in d.lista_organos]}")

    print("\n📋 Receptores registrados:")
    for r in receptores:
        print(f"{r.nombre} - Necesita: {r.organo_necesitado}")

def registrar_cirujano():
    """
    Solicita al usuario los datos necesarios para registrar un cirujano en un centro de salud.
    Si no hay centros de salud registrados, informa al usuario y no registra el cirujano.
    """
    print("\n Registrar Cirujano en Centro de Salud")
    centro = seleccionar_centro()
    if not centro:
        return

    nombre = input_texto("Nombre del cirujano: ")
    especialidades = input("Especialidades (separadas por coma): ").lower().split(",")
    especialidades = [e.strip() for e in especialidades]

    cirujano = Cirujano(nombre, especialidades)
    centro.agregar_cirujano(cirujano)
    print(f"Cirujano {nombre} registrado con especialidades: {', '.join(especialidades)}")


def main():
    """
    Función principal que muestra el menú y permite al usuario interactuar con el sistema.
    Permite registrar centros de salud, donantes, receptores, ver listados y ejecutar el sistema.
    """
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Centro de Salud")
        print("2. Registrar Donante")
        print("3. Registrar Receptor")
        print("4. Ver Listados")
        print("5. Registrar cirujano")
        print("6. Ejecutar el sistema")
        print("7. Salir")
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
            registrar_cirujano()
        elif opcion == "6":
            print("\nEjecutando el sistema...")
            if not donantes or not receptores:
                print("No hay donantes o receptores registrados.")
                continue
            
            for receptor in receptores:
                for donante in donantes:
                    if receptor.match(donante):
                        organo_donado = donante.organo_donado(receptor.organo_necesitado)
                        if organo_donado:
                            print(f"Órgano {organo_donado.tipo_organos} asignado a {receptor.nombre}")
                        else:
                            print(f"No se pudo donar el órgano a {receptor.nombre}")
                            cirujano = donante.centro_salud.asignar_cirujano(organo_donado.tipo_organos)
                            if cirujano:
                                print(f" Cirujano asignado: {cirujano.nombre}")
                            else:
                                print("No hay cirujano disponible o especializado en ese órgano.")
                    else:
                        print(f"No se pudo donar el órgano a {receptor.nombre}")            
            print("🔄 Sistema ejecutado con éxito.\n")
        elif opcion == "7":
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida, intentá nuevamente.")

if __name__ == "__main__":
    main()

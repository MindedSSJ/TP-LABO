from clases.organos import Organo
from clases.Centro_de_salud import *
from clases.incucai import *
from datetime import datetime, timedelta
import random
"""
Este sistema permite gestionar un banco de órganos, registrando donantes y receptores, sus organos disponibles y/o necesarios, 
así como los centros de salud y cirujanos disponibles para realizar las ablaciones y trasplantes. Tambien lleva a cabo la 
asignación de órganos a receptores según su compatibilidad y prioridad.
"""


donantes = []
receptores = []
centros_salud = []
vehiculos = [Vehiculo("ambulancia", 80),
             Vehiculo("helicoptero", 150),
             Vehiculo("avion", 600)]

# Mapa de distancias ficticias entre provincias (en km)
distancias = {
    ("Buenos Aires", "Cordoba"): 700,
    ("Buenos Aires", "Santa Fe"): 500,
    ("Cordoba", "Santa Fe"): 350,
    ("Buenos Aires", "Buenos Aires"): 50,
    ("Cordoba", "Cordoba"): 50,
    ("Santa Fe", "Santa Fe"): 50,
    ("Caba", "Caba"): 50,
}


def calcular_distancia(prov_origen, prov_destino):
    if prov_origen.lower() == prov_destino.lower():
        return 50  # misma provincia, distancia local
    return distancias.get((prov_origen, prov_destino)) or distancias.get((prov_destino, prov_origen), 800)

def elegir_vehiculo(prov_origen, prov_destino):
    distancia = calcular_distancia(prov_origen, prov_destino)
    trafico = random.randint(10, 50) if prov_origen.lower() == prov_destino.lower() else 0  # solo si es terrestre
    tipo_preferido = "avion" if distancia > 600 else "helicoptero" if distancia > 200 else "ambulancia"

    for v in vehiculos:
        if v.tipo == tipo_preferido:
            tiempo = v.calcular_tiempo(distancia, trafico)
            print(f"\n🛻 Vehículo asignado: {v.tipo} (Velocidad: {v.velocidad} km/h)")
            print(f"📏 Distancia: {distancia} km - ⏱️ Tiempo estimado de viaje: {tiempo:.2f} horas\n")
            return v, tiempo

    # Si no encontró del tipo preferido, usar el primero disponible
    v = vehiculos[0]
    tiempo = v.calcular_tiempo(distancia, trafico)
    print(f"\n🚨 Vehículo por defecto asignado: {v.tipo}")
    print(f"📏 Distancia: {distancia} km - ⏱️ Tiempo estimado de viaje: {tiempo:.2f} horas\n")
    return v, tiempo

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
            print("Formato incorrecto. Use YYYY-MM-DD.")
def input_hora(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return datetime.strptime(valor, "%H:%M").time()
        except ValueError:
            print("Formato de hora incorrecto. Use HH:MM.")
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

    valid_organos = {"corazon", "pulmon", "higado", "riñon", "pancreas", "intestino"}
    print("Órganos válidos:", ", ".join(valid_organos))
    organos = input("Ingrese los órganos a donar, separados por coma: ").lower().split(",")

    lista_organos = []
    for tipo in organos:
        tipo = tipo.strip()
        if tipo in valid_organos:
            if tipo not in [o.tipo_organos for o in lista_organos]:
                lista_organos.append(Organo(tipo, fecha_ablacion, hora_ablacion))
            else:
                print(f"⚠️ El órgano '{tipo}' ya fue ingresado. Ignorado.")
        else:
            print(f"❌ Órgano inválido: '{tipo}'. No será registrado.")

        if not lista_organos:
            print("⚠️ No se registró ningún órgano válido. Cancelando registro de donante.")

    donante = Donante(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro,
                      fecha_muerte, hora_muerte, fecha_ablacion, hora_ablacion, lista_organos)
    donantes.append(donante)

    
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
    # Validación de prioridad
    while True:
        prioridad = input_numerico("Prioridad del 1 al 5 (1: baja - 5: alta): ")
        if 1 <= prioridad <= 5:
            break
    print("La prioridad debe estar entre 1 y 5.")

    patologia = input("Patología: ")
    estado = input("Estado actual: ")

    receptor = Receptor(nombre, dni, nacimiento, sexo, telefono, tipo_sangre, centro,
                 organo_necesitado, fecha_listado, prioridad, patologia, estado)
    receptores.append(receptor)

    
    print("Receptor registrado.\n")

def ver_vehiculos():
    if not vehiculos:
        print("No hay vehículos registrados.")
        return
    else:
        for v in vehiculos:
            print(f"🚐 {v.tipo} - Velocidad: {v.velocidad} km/h")


def ver_listas():
    """ 
    Muestra los listados de centros de salud, donantes y receptores registrados.
    """
    print("\n🏥 Centros de Salud registrados:")
    for c in centros_salud:
        print(f"- {c.nombre} ({c.provincia} - {c.partido})")

    print("\nDonantes registrados:")
    for d in donantes:
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
        print("7. Ver vehículos")
        print("8. Salir")
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
            def protocolo_trasplante(donante, receptor, organo_donado):
                print(f"\n✅ Órgano {organo_donado.tipo_organos} asignado a {receptor.nombre}")

        # 1. Asignar vehículo
                vehiculo, distancia = elegir_vehiculo(donante.centro_salud.provincia, receptor.centro_salud.provincia)
                if not vehiculo:
                    print("❌ No hay vehículo disponible para transporte.")
                    return False

        # 2. Asignar cirujano para ablación
                cirujano_donante = donante.centro_salud.asignar_cirujano(organo_donado.tipo_organos)
                if not cirujano_donante:
                    print("❌ No hay cirujano disponible para ablación.")
                    return False

        # 3. Realizar ablación
                tiempo_actual = datetime.now()
                organo_donado.fecha_ablacion = tiempo_actual.date()
                organo_donado.hora_ablacion = tiempo_actual.time()
                try:
                    donante.lista_organos.remove(organo_donado)
                except ValueError:
                    print("organo ya removido")
                print(f"🩺 Ablación realizada por {cirujano_donante.nombre} a las {organo_donado.hora_ablacion} del {organo_donado.fecha_ablacion}")

        # 4. Transporte
                tiempo_traslado_horas = vehiculo.calcular_tiempo(distancia, 0)
                tiempo_llegada = tiempo_actual + timedelta(hours=tiempo_traslado_horas)
                print(f"🚗 Vehículo asignado: {vehiculo.tipo} ({vehiculo.velocidad} km/h)")
                print(f"⏱️ Tiempo estimado de traslado: {tiempo_traslado_horas:.2f} horas")

        # 5. Trasplante
                cirujano_receptor = receptor.centro_salud.asignar_cirujano(organo_donado.tipo_organos)
                if not cirujano_receptor:
                    print("❌ No hay cirujano disponible para trasplante en el centro receptor.")
                    return False

                tiempo_transcurrido = tiempo_llegada - tiempo_actual
                if tiempo_transcurrido > timedelta(hours=20):
                    print("⛔ El órgano no llegó a tiempo. Tiempo excedido para trasplante.")
                    return False

        # Trasplante exitoso
                print(f"✅ Trasplante realizado con éxito por cirujano: {cirujano_receptor.nombre} en paciente:{receptor.nombre}")
                receptores.remove(receptor)
                return True

    # Proceso de match y ejecución
            for receptor in receptores[:]:  # Copia para evitar modificación durante la iteración
                for donante in donantes:
                    if receptor.match(donante):
                        organo_donado = donante.organo_donado(receptor.organo_necesitado)
                        if organo_donado:
                            exito = protocolo_trasplante(donante, receptor, organo_donado)
                            break  # Receptor ya fue atendido
        elif opcion == "7":
            ver_vehiculos()
        elif opcion == "8":
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida, intentá nuevamente.")

if __name__ == "__main__":
    main()


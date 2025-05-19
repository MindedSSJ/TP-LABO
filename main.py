from clases.donante import Donante
from clases.receptor import Receptor
from organos import Organo
from Centro_de_salud import CentroDeSalud
from incuncai import Incucai

# Crear centros de salud
centro1 = CentroDeSalud("Hospital Central", "Calle Falsa 123", "San Martín", "Buenos Aires", "1122334455")
centro2 = CentroDeSalud("Clínica Norte", "Av. Salud 456", "Vicente López", "Buenos Aires", "1199887766")

# Crear órganos
org1 = Organo("riñón", "2025-05-18", "10:00")
org2 = Organo("hígado", "2025-05-18", "10:00")

# Crear donante
donante1 = Donante(
    nombre="Juan Pérez",
    dni="12345678",
    nacimiento="1980-01-01",
    sexo="M",
    telefono="1111222233",
    tipo_sangre="A+",
    centro_salud=centro1,
    fecha_muerte="2025-05-18",
    hora_muerte="08:00",
    fecha_ablacion="2025-05-18",
    hora_ablacion="10:00",
    lista_organos=[org1, org2]
)

# Crear receptor
receptor1 = Receptor(
    nombre="María Gómez",
    dni="87654321",
    nacimiento="1990-05-20",
    sexo="F",
    telefono="1144556677",
    tipo_sangre="A+",
    centro_salud=centro2,
    organo_necesitado="riñón",
    fecha_listado="2025-05-15",
    prioridad="alta",
    patologia="Insuficiencia renal",
    estado="espera"
)

# Crear sistema INCUCAI
sistema_incucai = Incucai()
sistema_incucai.agregar_centro(centro1)
sistema_incucai.agregar_centro(centro2)
sistema_incucai.agregar_donante(donante1)
sistema_incucai.agregar_receptor(receptor1)

# Mostrar órganos disponibles del donante
donante1.tiene_organos()

# Intentar hacer un match y donar un órgano
print("\n⛓ Intentando match con el receptor...")

if receptor1.match(donante1):
    organo_donado = donante1.organo_donado(receptor1.organo_necesitado)
    if organo_donado:
        print(f"\n🫀 Órgano {organo_donado.tipo_organos} fue asignado a {receptor1.nombre}")
else:
    print("❌ No se pudo realizar el trasplante.")

# Mostrar órganos restantes
print("\n📦 Órganos restantes del donante:")
donante1.tiene_organos()

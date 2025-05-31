proyecto de sistema de gestion de donantes y receptor de organos
es un proyecto que hace una simulacion sobre un sistema de coordinacion de transplantes de organos, todo mediante una organizacion INCUNCAI
el proyecto permite registrar donantes y receptores, realizar procesos de matching entre organos donados y receptor, observa la disponibilidad de cirujanos en los centros de salud agregados
el proyecto esta realizado en python con programacion orientada a objetos
esta distribuido en distintas clases, siendo la clase padre la clase Paciente, dentro de ella tiene clases hijas como puede ser donante y receptor

sus funcionalidades principales como ya mencionadas anteriormente a brevedad son
registrar donantes con su informacion y organos dispnibles
registrar receptores con su organo requerido, prioridad y estado del receptor
realizar matching entre donante y receptor (por organo y tipo de sangre)
asignar cirujanos a centros de salud con su especialidad y verificar disponibilidad despues de un match exitoso
Observar listados de centros de salud, donantes, receptores, cirujanos

instructivo de uso

primero y principal antes de agregar un donante, un organo o un receptor, debemos crear e incluir un centro de salud
luego de crear centro de salud, podemos crear donantes, receptores e incluir cirujanos con su respectiva especializacion
al tener todos los datos necesarios de cada uno de las variables pedidas el menu te otorga una opcion para ejecutar el sistema y encontrar match 

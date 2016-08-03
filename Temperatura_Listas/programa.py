#Registro medición

import random
import menu
import Registro
import Alerta

sectores = ['norte', 'sur', 'este', 'oeste']
# Listado de alertas por sector
alertas_norte = []
alertas_sur = []
alertas_este = []
alertas_oeste = []

# Límites de temperatura
lim_sup = 40
lim_inf = 5

# Listado de mediciones
mediciones = []

def inicio():
    op = menu.mostrar_menu()

    while (op != 6):
        if op == 1:
            generar_mediciones(100)
        elif op == 2:
            mostrar_cantidades()
        elif op == 3:
            mostrar_mayor_temperatura()
        elif op == 4:
            mostrar_menor_temperatura()
        elif op == 5:
            hora = menu.leer_entero_valido("Ingrese la hora: ", 0, 24)
            mostrar_alertas_por_hora("Sur", hora)
        elif op == 6:
            print("Finalizó el programa")
            exit(0)
        op = menu.mostrar_menu()

# Generar registro de mediciones en forma aleatoria
def generar_mediciones(cantidad):
    for i in range(0, cantidad):
        hora = random.randint(0,24)
        lugar = random.choice(sectores)
        hum = random.randint(-10, 40)
        registro = Registro.Registro()
        Registro.init(registro, lugar, hora, hum)
        mediciones.append(registro)

# Procesar mediciones y generar alertas
def procesar_mediciones():
    for medicion in mediciones:
        if (medicion.temperatura > lim_sup):
            alerta = Alerta.crearAlerta(1)
            agregar_a_lista(medicion.lugar, alerta)
        elif (medicion.temperatura < lim_inf):
            alerta = Alerta.crearAlerta(2)
            agregar_a_lista(medicion.lugar, alerta)

# Agrega el alerta a la lista correspondiente
def agregar_a_lista(lugar, alerta):
    if (lugar == "norte"):
        alertas_norte.append(alerta)
    elif (lugar == "sur"):
        alertas_sur.append(alerta)
    elif (lugar == "este"):
        alertas_este.append(alerta)
    elif (lugar == "oeste"):
        alertas_oeste.append(alerta)

def mostrar_cantidades():
    "A desarrollar"
    pass

def mostrar_mayor_temperatura():
    "A desarrollar"
    pass

def mostrar_menor_temperatura():
    "A desarrollar"
    pass

def mostrar_alertas_por_hora(lugar, hora):
    "Ordenar los alertas por hora y mostrarlos en pantalla"
    pass

inicio()
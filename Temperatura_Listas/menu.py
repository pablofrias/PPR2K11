
def mostrar_menu():
    print('SENSORES DE TEMPERATURAS' \
          '\n\t 1- Generar aleatoriamente mediciones' \
          '\n\t 2- Mostrar cantidad de alertas por región' \
          '\n\t 3- Mostrar registro de mayor humedad' \
          '\n\t 4- Mostrar registro de menor humedad' \
          '\n\t 5- Mostrar alertas por hora en zona Sur' \
          "\n\t 6- Salir")
    return leer_entero_valido("Ingrese opción: ", 1, 6)

def leer_entero_valido(msg, li, ls):
    x = int(input(msg))
    while x < li or x > ls:
        print('Valor incorrecto')
        x = int(input(msg))
    return x
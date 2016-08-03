# Registro de temperatura

class Registro:
    pass

# Inicializador de registro
def init(registro, lugar, hora, temperatura):
    registro.lugar = lugar
    registro.hora = hora
    registro.temperatura = temperatura

# Imprimir en pantalla
def write(registro):
    print("Registro - Lugar: ", registro.lugar, \
           " temperatura: ", registro.temperatura, \
           " hora: ", registro.hora)
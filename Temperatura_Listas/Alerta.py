
class Alerta:
    pass

def init(alerta, tipo):
    alerta.tipo = tipo

def crearAlerta(tipo):
    alerta = Alerta()
    init(alerta, 1)
    return alerta

def write(alerta):
    if alerta.tipo == 1:
        print('Alerta! Temperatura mayor al límite superior')
    else:
        print('Alerta! Temperatura menor al límite inferior')

contador = 0

def consumir():
    global contador
    contador =+ 1
    print("Executando Consumir: ", contador)
    consumir()

consumir()

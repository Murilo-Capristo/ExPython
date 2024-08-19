contador = 1

class No:
    lista = [x for x in range(1000000)]
    proximo = None


if __name__ == "__main__":
    raiz = No()
    temp = raiz
    while True:
        print("Contador: ", contador)
        contador += 1
        outro = No()
        temp.proximo = outro
        temp = outro
vendas = [120, 80, 150, 90, 200]


def valor_minimo(numero):
    if numero > 100:
        return True
    else:
        return False
    
def dez_porcento(lista_numeros):
    lista_temp = []
    for numero in lista_numeros:
        lista_temp.append(numero * 0.90)
    return lista_temp    
    
nova_lista = list(filter(valor_minimo, vendas))

saida_esperada = dez_porcento(nova_lista)
print(vendas)
print((nova_lista))

print(saida_esperada)


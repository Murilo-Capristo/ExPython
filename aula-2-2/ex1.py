lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def numeros_3_4(numero):
    if numero % 3 == 0 or numero % 4 == 0:
        return True
    else:
        return False
    
nova_lista = filter(numeros_3_4, lista)
print("lista: ")
print(lista)
print("Numeros Divisiveis por 3 ou por 4: ")
print(list(nova_lista))
num_casos = int(input()) #numero de casos de teste
for caso in range(num_casos):
    alunos = int(input()) #Numero de alunos na fila
    notas = input()
    lista_notas = notas.split(" ")
    lista_notas_float = [float(nota) for nota in lista_notas]
    lista_notas_ordenada = sorted(lista_notas_float, reverse=True)
    print("Notas lista:" , lista_notas)
    print("Notas Float:" , lista_notas_float)
    print("Notas Ordenadas:" , lista_notas_ordenada)
    contador = 0
    for i in range(len(lista_notas_float)):
        if lista_notas_float[1] == lista_notas_ordenada[1]:
            contador += 1
    print("Quantos mudaram:",contador)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Numeros impares
for i in lista:
    if i % 2 != 0:
        print(i)


#Numeros pares
for i in lista:
    if i % 2 == 0:
        print(i)     


#Impar²
for i in lista:
    if i % 2 != 0:
        quadrado = i * i
        print(quadrado)

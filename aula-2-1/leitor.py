import json

arquivo = open("./dados.json", "r", encoding="latin1")
conteudo = arquivo.read()
print("Conteudo: ")
print(conteudo)


lista = json.loads(conteudo)
print("Lista: ", end = "")
print(lista)

for sacanagem in lista:
    print(sacanagem["nome"])
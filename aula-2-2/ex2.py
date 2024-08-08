clientes = [
    {"nome": "Joao Silva", "idade": 24, "genero": "M"},
    {"nome": "Maria Silva", "idade": 25, "genero": "F"},
    {"nome": "Alberto Roberto", "idade": 30, "genero": "M"},
    {"nome": "Iracema Souza", "idade": 23, "genero": "F"}
]



filtro_nome = lambda dicionario : dicionario['genero'] != ""
nomes = filter(filtro_nome, clientes)
print("Apenas os nomes: ")
for i in clientes:
    print()

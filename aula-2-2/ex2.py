clientes = [
    {"nome": "Joao Silva", "idade": 24, "genero": "M"},
    {"nome": "Maria Silva", "idade": 25, "genero": "F"},
    {"nome": "Alberto Roberto", "idade": 30, "genero": "M"},
    {"nome": "Iracema Souza", "idade": 23, "genero": "F"}
]



filtro_nome = lambda dicionario : dicionario['nome']
nomes = map(filtro_nome, clientes)
print("Apenas os nomes: ")
print(list(nomes))

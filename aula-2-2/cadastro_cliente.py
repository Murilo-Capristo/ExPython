clientes= [
    {"nome": "Joao Silva", "idade": 24, "genero": "M"},
    {"nome": "Maria Madanela", "idade": 75, "genero": "F"},
    {"nome": "Pedro Paia", "idade": 14, "genero": "M"},
    {"nome": "Mirela Salvao", "idade": 22, "genero": "F"}
]

filtro_homens = lambda dicionario : dicionario['genero'] == "M"
filtro_mulheres = lambda dicionario : dicionario['genero'] == "F"
homens = filter(filtro_homens, clientes)
mulheres = filter(filtro_mulheres, clientes)
print("toDO MUNDO: ")
print(clientes)
print("Apenas os homens")
print(list(homens))
print("Apenas as Mulheres: ")
print(list(mulheres))
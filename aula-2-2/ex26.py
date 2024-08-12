produtos = [ {"nome": "Camisa", "preço": 50, "em_estoque": True}, {"nome": "Calça", "preço": 80, "em_estoque": False}, {"nome": "Chapéu", "preço": 30, "em_estoque": True}, ] 

produtos_estoque = lambda dicionario : dicionario['em_estoque']
filtragem = filter(produtos_estoque, produtos)
print("Produtos em estoque: ")
print(list(filtragem))
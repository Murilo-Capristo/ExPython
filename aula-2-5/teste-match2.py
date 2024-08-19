lista = ["Bom","Dia" ,"joao", "maria", "jose", "sara"]
match lista:
    case [cumprimento, periodo, *nomes]:
        for i,nome in enumerate(nomes):
            print(i, cumprimento, periodo, nome)


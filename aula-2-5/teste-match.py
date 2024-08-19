from time import sleep


menu = """ 
        (C) Cadastrar
        (M) Mostrar
        (R) Remover
        (A) Atualizar
        (S) Sair
        
        >"""

while True:
    print(menu, end="")
    bruto = input().lower()
    escolha = bruto[0]
    match escolha:
        case "c":
            print("Cadastrar")
            sleep(1)
        case "m":
            print("Mostrar")
            sleep(1)
        case "r":
            print("Remover")
            sleep(1)
        case "a":
            print("Atualizar")
            sleep(1)
        case "s":
            print("Saindo...")
        
            sleep(0.1)
            break
        case _:
            print("Opção inválida!")
            sleep(1)

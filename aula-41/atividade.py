import os

def menu_principal(): 
    os.system("cls")
    print("""Programa Agenda de Contatos
          
          Menu de opções:
          
        (1) Cadastrar
        (2) Ler registros
        (0) Sair 
""")

def ler_registros():
    print("""Sub menu (2) Ler registros, escolha uma opção:
                (1) Atualizar o registro
                (2) Remover o Registro
                (0) Voltar
          
          """)

while True:
    print(menu)

    escolha = int(input())
    if(escolha == 1):
        print("Escolha 1")
    elif(escolha == 2):
        print("Escolha 2")
    elif(escolha == 0):
        break

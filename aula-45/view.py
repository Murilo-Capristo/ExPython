from datetime import datetime
import os

from controller import Controller
from model import Contato

class View:
    rodando = True
    

    def __init__(self):
        self.control = Controller()


    def ler_dados_contato(self):

        print("Digite os dados do contato")
        contato = Contato()
        contato.nome = input("Nome>")
        contato.telefone = input("Telefone>")
        contato.email = input("Email> ")
        str_nascimento = input("Nascimento>")
        contato.nascimento = datetime.strptime(str_nascimento, "%d/%m/%Y")
        return contato
    
    
    def menu_principal(self):
        os.system("CLS")
        print("Agenda de Contato no FireBase")
        print("""
    (1) Cadastrar novo contato
    (2) Procurar contatos existentes
    (3) Remover um contato específico
    (4) Atualizar um contato específico
              (0) Sair
    
    Por favor escolha uma opção e tecle <Enter> >""" ,  end="")
        opcao = int(input())
        if opcao != "":
            match opcao:
                case 1:
                    contato = self.ler_dados_contato()
                    self.control.cadastrar(contato)
                case 2:
                    self.control.pesquisar()
                    contatos = self.control.pesquisar()
                    for contato in contatos:
                        print(contato)
                case 3:
                    self.control.remover()
                case 4:
                    self.control.atualizar()
                case 0:
                    print("Obrigado por usar nosso sistema. Até breve!")
                    self.rodando = False
                case _:
                    print("Opção inválida")
        else:
            print("Você precisa selecionar uma opção")

    def executar(self):
         while self.rodando:
            self.menu_principal()
            input("Tecle <Enter> para continuar.")

if __name__ == "__main__":
    view = View()
    view.executar()
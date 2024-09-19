import os

from controle import Controle
from modelo import Contato


class Visualizacao:
    def __init__(self) -> None:
        self.controle = Controle()
        pass

    def menu_principal(self):
        # os.system("cls")
        print(
            """
                    A G E N D A   D E   C O N T A T O S

(1) Cadastrar um contato
(2) Pesquisar um contato
(3) Remover um contato
(4) Atualizar um contato
(5) Gerar tabela
(0) Sair

Por favor escolha uma opção >"""
)
        entrada = input()
        if(len(entrada)> 0):
            opcao = entrada
            match(opcao):
                case "1" : 
                    c1 = self.criar_contato()
                    self.controle.salvar(c1)

                case "2" :
                    nome = input("Digite um nome para pesquisar: ").lower()
                    lista_contatos = self.controle.pesquisar(nome)
                    self.mostrar_contatos(lista_contatos)
                case "3" : 
                    contato_id = self.ler_id_contato()
                    if contato_id is not None:
                        self.controle.apagar(contato_id)
                        print("Contato Deletado")
                case "4" : 
                    contato_id= self.ler_id_contato()
                    if contato_id is not None:
                        print("Agora digite os novos valores para o Contato")
                        c1 = self.criar_contato()
                        self.controle.atualizar(contato_id, c1)
                case "5":
                    self.controle.gerar_tabela()

                case "0" :
                    print("Até logo!")
                    exit()
                case _:
                    print("Entrada Inválida!")
    
    def criar_contato(self) -> Contato:
        c = Contato()
        print("")
        c.nome = input("Informe o nome do contato: ").lower()
        c.telefone = input("Telefone >")
        c.email = input("Email >").lower()

        return c
    
    def mostrar_contatos(self, lista_contatos : list) -> None:
        for contato in lista_contatos:
            print("-"*40)
            print(contato)

    def ler_id_contato(self) -> int:
        while True:
            str_contato_id = input("Digite o ID para pesquisar > ").lower()
            if str_contato_id == "sair":
                return None
                
            if len(str_contato_id) > 0 and str_contato_id.isnumeric():
                contato_id = int(str_contato_id)
                print(f"Verificando ID: {contato_id}")
                if self.controle.check_contato(contato_id):
                    return contato_id
                else:
                    print("Contato não existente. Tente novamente, ou digite 'sair' para parar de pesquisar.")
            else:
                input("Número digitado não é um ID válido! Tecle <Enter> para continuar")

        r

if __name__ == "__main__":
    vis = Visualizacao()
    while True:
        vis.menu_principal()
        input("Tecle <Enter> para continuar")
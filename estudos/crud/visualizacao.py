from controle import Controle
import os
from modelo import Carro

class Visualizacao:
    def __init__(self) -> None:
        self.controle = Controle()
    
    def menuPrincipal(self):
        os.system("cls")
        print("""
                A G E N D A  D E  C O N T A T O S

              
(1) Gerar Tabela
(2) Adicionar Carro            
(3) Listar Carros
(4) Atualizar Carro
(5) Excluir carro
(0) Sair                

""")    
        escolha = input()
        if(len(escolha) > 0):
            opcao = escolha
            match(opcao):
                case "1":
                    self.controle.gerarTabela()
                case "2":
                    c1 = self.criarCarro
                    self.controle.adicionar(c1)
                case "3":
                    modelo = input("Digite um modelo para pesquisar: ").lower()
                    lista_carros = self.controle.pesquisar()
                    self.mostrarCarros(lista_carros)
                case "4":
                    id_carro = self.lerIdCarro
                    print("Agora digite as novas informações>")
                    c1 = self.criarCarro
                    self.controle.atualizar(id_carro, c1)
                case "5":
                    id_carro = self.lerIdCarro
                    self.controle.excluir(id_carro)
                    print("Carro excluido!")
                case "0":
                    print("Até logo!")
                    exit()
                case _:
                    print("Entrada inválida!")

    def criarCarro(self)-> Carro:
        c = Carro()
        print("")
        c.marca = input("Marca:").lower()
        c.modelo = input("Modelo: ").lower()
        c.ano = input("Ano: ").lower()
        c.tipoDeCombustivel = input("Tipo de combustivel").lower()
        return c
    
    def mostrarCarros(self, lista_carros = list):
        for carro in lista_carros:
            print("-" * 40)
            print(carro)

    def lerIdCarro(self)-> int:
        while True:
            carroId = input("Digite o Id do carro")
            if len(carroId) > 0 and carroId.isnumeric:
                return carroId
            else:
                print("Numero digitado não é um ID válido! Tecle <Enter> para continuar")
if __name__ == "__main__":
    vis = Visualizacao()
    while True:
        vis.menu()
        input("Tecle <Enter> para continuar!")                
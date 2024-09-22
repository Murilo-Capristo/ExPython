from controle import Controle
import os
from modelo import Carro

class Visualizacao:
    def __init__(self) -> None:
        self.controle = Controle()
    
    def criarCarro(self)-> Carro:
        c = Carro()
        print("")
        c.marca = input("Marca:")
        c.modelo = input("Modelo: ")
        c.ano = input("Ano: ")
        c.tipoDeCombustivel = input("Tipo de combustivel")
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
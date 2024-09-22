from repositorio import Repositorio
from modelo import Carro
class Controle:
    def __init__(self):
        self.lista_carros = []
        self.repositorio = Repositorio()
        
    def pesquisar(self, nome_pesquisa : str):
        self.lista_carros.clear()
        temp_lista = self.repositorio.procurarCarro()
        self.lista_carros.extend(temp_lista)
        return temp_lista
    def adicionar(self, carro : Carro):
        self.repositorio.adicionarCarro(carro)
    def excluir(self, carro_id : int):
        self.repositorio.excluirCarro(carro_id)
    def atualizar(self, carro_id : int, carro : Carro):
        self.repositorio.alterarCarro(carro_id, carro)
    def gerarTabela(self):
        self.repositorio.gerarTabela()
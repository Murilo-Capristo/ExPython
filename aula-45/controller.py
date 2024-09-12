from model import Contato
from servico import Servico
class Controller:
    def __init__(self):
        self.servico = Servico()
    def cadastrar(self, contato):
        print("Cadastrando o contato")
        response = self.servico.cadastrar_firebase(contato)
        print(contato)
        print(f"Reposta = {response}")
        
        
        
    def pesquisar(self):
        print("Pesquisar Contatos")
        contatos = self.servico.pesquisar_firebase()
        return contatos
        
        pass
    def remover(self):
        print("Remover contatos")
        pass
    def atualizar(self):
        print("Atualizar contatos")
        pass
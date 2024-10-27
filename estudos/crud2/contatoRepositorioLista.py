from contato import Contato
class ContatoRepositorioLista:
    lista = []
    counter = 0 

    def __init__(self):
        pass

    def cadastrar(self, contato : Contato):
        self.counter += 1
        contato.contato_id = self.counter
        self.lista.append(contato)

    def pesquisar_por_id(self, contato_id : int) -> list:
        lista_temp = []
        for contato in self.lista:
            if contato.contato_id == contato_id:
                lista_temp.append(contato)
        return lista_temp
    
    def pesquisar_por_nome(self, nome : str) -> list:
        lista_temp = []
        for contato in self.lista:
            if contato.nome.find(nome) != -1:
                lista_temp.append(contato)
        return lista_temp
    
    def atualizar(self, contato_id : int, contato : Contato):
        lista_encontrado = self.pesquisar_por_id( contato_id)
        for c in lista_encontrado:
            c.nome = contato.nome
            c.telefone = contato.telefone
            c.email = contato.email

    def remover(self, contato_id : int):
        lista_encontrado = self.pesquisar_por_id( contato_id)
        for c in lista_temp:
            self.lista.remove(c)
            
            

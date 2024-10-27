class Contato:
    contato_id = int
    nome = str
    telefone = str
    email = str

    def __init__(self, contato_id : int = 0, nome : str = "", telefone : str = "", email : str = ""):
        self.contato_id = contato_id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
         return f"ID: {self.contato_id}\tNome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}"
    
    def from_dict(self, dicionario):
        #novo_contato = from_dict(param_dict)
        self.contato_id = dicionario.get("id", "")
        self.nome = dicionario.get("nome", "")
        self.telefone = dicionario.get("telefone", "")
        self.email = dicionario.get("email", "")

    
    def to_dict(self) -> dict:
        dicionario = {}
        dicionario["id"]= self.contato_id
        dicionario["nome"]=self.nome
        dicionario["email"]=self.email
        dicionario["telefone"]=self.telefone
        return dicionario
        
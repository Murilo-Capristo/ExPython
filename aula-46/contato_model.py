
class Contato:
    contato_id : int
    nome : str
    telefone : str
    email : str

    def __init__(self, contato_id = 0, nome = "", telefone = "", email = ""):
        self.contato_id = contato_id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self) -> str:
        return f"{self.contato_id}\n{self.nome}\n{self.telefone}\n{self.email}"

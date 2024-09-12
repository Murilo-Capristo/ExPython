from datetime import datetime

class Contato:
    """
    Classe que descreve os objetos do tipo Contato.
    """
    def __init__(self, id=0, nome="", telefone="", email="", nascimento=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.nascimento = nascimento or datetime.now()

    def __str__(self):
        width = 34
        line_format = f"| {{:<{width - 2}}} |\n"
        sb = []
        sb.append("+" + "-" * width + "+\n")
        sb.append(line_format.format(f"ID CONTATO : {self.id}"))
        sb.append(line_format.format(f"Nome: {self.nome}"))
        sb.append(line_format.format(f"Telefone: {self.telefone}"))
        sb.append(line_format.format(f"Email: {self.email}"))
        sb.append(line_format.format(f"Nascimento: {self.nascimento.strftime('%d/%m/%Y')}"))
        sb.append("+" + "-" * width + "+\n")

        return ''.join(sb)

if __name__ == "__main__":
    date_time_str = "01/04/2003"
    nascimento = datetime.strptime(date_time_str, "%d/%m/%Y")
    c1 = Contato(1, "João Silva", "(11) 111-111", "joao@teste.com", nascimento)
    print("Contato:\n", c1)

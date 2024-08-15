class Pessoa:
    nome = ""
    sobrenome = ""

    def imprimir(self):
        print(f"Nome:{self.nome}\t\tSobrenome:{self.sobrenome}")

p1 = Pessoa()
p1.nome = "Joao"
p1.sobrenome = "1"    
p1.imprimir()

p2 = Pessoa()
p2.nome = "Silva"
p2.sobrenome = "2"   
p2.imprimir()

# print(f"Nome: {p1.nome}\t\tSobrenome: {p1.sobrenome}")
# print(f"Nome: {p2.nome}\t\tSobrenome: {p2.sobrenome}")
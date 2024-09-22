class Carro:
    def __init__(self, 
                carro_id : int = 0, 
                marca : str = "",
                modelo : str = "",
                ano : int =  0,
                tipoDeCombustivel : str =  ""):
        self.id = carro_id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tipoDeCombustivel = tipoDeCombustivel
    
    def __str__(self):
        return f"""{self.marca}\n{self.modelo}"""
if __name__ == "__main__":
    c1 = Carro(1,"Hyundai","Tucson",2015,"Diesel")
    print(c1)
        
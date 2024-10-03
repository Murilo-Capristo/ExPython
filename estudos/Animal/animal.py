def animais():
    vertebra = input("""    
    (1) Vertebrado
    (2) Invertebrado   
    >""").lower()

    # VERTEBRADO
    if vertebra == "1" or vertebra == "vertebrado":
        tipoVer = input("""
        (1) Ave
        (2) Mamífero
        >""").lower()
        
        # AVE
        if tipoVer == "1" or tipoVer == "ave":
            print("Ave")
            alimentacaoAve = input("""
            (1) Carnivoro
            (2) Onívoro                    
            >""").lower()
            
            # CARNIVORO
            if alimentacaoAve == "1" or alimentacaoAve == "carnivoro":
                return "Águia"
                
            # ONIVORO
            elif alimentacaoAve == "2" or alimentacaoAve == "onivoro" or alimentacaoAve == "onívoro":
                return "Pomba"
            else:
                return "Valor inválido"
        
        # MAMIFERO  
        elif tipoVer == "2" or tipoVer == "mamifero" or tipoVer == "mamífero":
            print("Mamifero")
            alimentacaoMam = input("""
            (1) Onivoro
            (2) Herbivoro                    
            >""").lower()
            
            # ONIVORO
            if alimentacaoMam == "1" or alimentacaoMam == "onivoro":
                return "Homem"
            
            # HERBIVORO
            elif alimentacaoMam == "2" or alimentacaoMam == "herbivoro":
                return "Vaca"
            else:
                return "Valor inválido"

    elif vertebra == "2" or vertebra == "invertebrado":
        tipoInv = input("""
        (1) Inseto
        (2) Anelideo
        >""").lower()
        
        if tipoInv == "1" or tipoInv == "inseto":
            print("Inseto")
            alimentacaoIns = input("""
            (1) Hematofago
            (2) Herbivoro
            >""").lower()
            
            if alimentacaoIns == "1" or alimentacaoIns == "hematofago":
                return "Pulga"
            elif alimentacaoIns == "2" or alimentacaoIns == "herbivoro":
                return "Lagarta"
            else:
                return "Valor inválido"
        
        elif tipoInv == "2" or tipoInv == "anelideo":
            print("Anelideo")
            alimentacaoAne = input("""
            (1) Hematofago
            (2) Onivoro
            >""").lower()
            
            if alimentacaoAne == "1" or alimentacaoAne == "hematofago":
                return "Sanguessuga"
            elif alimentacaoAne == "2" or alimentacaoAne == "onivoro":
                return "Minhoca"
            else:
                return "Valor inválido"
    
    
    else:
        return "Valor inválido"

while True:
    print(animais())
    sn = input("Deseja continuar?(S/N)").lower()
    if sn == "n":
        exit()

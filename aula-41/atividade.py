import os
import oracledb
from datetime import datetime

class Contato:
    """
    Classe de contato para servir como padrão para os objetos do tipo contato
    """
    def __init__(self, nome="", telefone="", email="", nascimento=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.nascimento = nascimento

def gerar_conexao_db():
    usuario = os.environ.get("FIAP_ORACLE_USER")
    senha = os.environ.get("FIAP_ORACLE_PASS")
    db_path = "oracle.fiap.com.br:1521/orcl"
    con = oracledb.connect(
        user=usuario, 
        password=senha, 
        dsn=db_path)
    return con


nome_tabela = "EX_CONTATOS"
def gravar_db(contato: Contato) -> bool:
    conexao = gerar_conexao_db()
    cursor = conexao.cursor()
    sql_insert = f"""
         INSERT INTO {nome_tabela} (nome, telefone, email, nascimento) VALUES (:1, :2, :3, :4)"""
    
    try:
        cursor.execute(sql_insert, (contato.nome, contato.telefone, contato.email, contato.nascimento))
        conexao.commit()  # Corrigido para chamar com parênteses
        return True
    except Exception as err:
        print("Erro: ", err)
        conexao.rollback()
        return False
    finally:
        cursor.close()
        conexao.close()  # Move o fechamento da conexão para o finally para garantir que sempre seja fechado

def gerar_tabela() -> bool:
    conexao = gerar_conexao_db()
    cursor = conexao.cursor()

    sql_create = f"""
CREATE TABLE {nome_tabela}(
nome VARCHAR2(100),
telefone VARCHAR2(20),
email VARCHAR2(50),
nascimento DATE,
CONSTRAINT Contato_pk PRIMARY KEY (nome)
)"""
    try:
        cursor.execute(sql_create)
        conexao.commit()
        return True
    except Exception as err:
        print(err)
        conexao.rollback()
        return False
    finally:
        cursor.close()
        conexao.close()

def menu_principal(): 
    os.system("cls")
    print("""Programa Agenda de Contatos
          
          Menu de opções:
        
        (1) Gerar Tabela
        (2) Cadastrar
        (3) Ler registros
        (0) Sair 
>""" , end="")



def mostrar_registros() -> bool:
    print("Todos os registros:\n")
    conexao = gerar_conexao_db()
    cursor = conexao.cursor()
    sql_mostrar = f"SELECT * FROM {nome_tabela}"
    try:
        cursor.execute(sql_mostrar)
        conexao.commit()
        dados = cursor.fetchall()
        for d in dados:
            print(d)
        return True
    except Exception as err:
        print(f"Erro-> {err}")
        conexao.rollback()
        return False
    finally:
        cursor.close()
        conexao.close()

def procurar_registro() -> Contato:
    conexao = gerar_conexao_db()
    cursor = conexao.cursor()
    exec = True
    while exec:
        nome = input("Digite o nome do contato \n>")
        sql_procurar = f"SELECT * FROM {nome_tabela} WHERE NOME LIKE :nome"

        try:
            cursor.execute(sql_procurar, NOME=f"%{nome}%")
            dados = cursor.fetchall()
            if dados:
                for d in dados:
                    contato = Contato(nome=d[0], telefone=d[1], email=d[2], nascimento=d[3])
                    print(f"Nome: {contato.nome} \n Telefone: {contato.telefone}\n Email: {contato.email}\n Nascimento: {contato.nascimento}\n")
                    return contato
                    
            else:
                print("Nenhum resultado encontrado!")
        except Exception as err:
            print(f"Erro-> {err}")
        

def remover():
    cliente = procurar_registro()
    if cliente is None:
        print("Nenhum cliente encontrado com esses parâmetros")
        return
    conexao = gerar_conexao_db()
    cursor = conexao.cursor()
    sql_remove = f"""DELETE FROM {nome_tabela} WHERE NOME = :nome"""
    try:
        cursor.execute(sql_remove, nome=cliente.nome)
        conexao.commit()
        print(f"Contato {cliente.nome} Removido com sucesso!")
    except Exception as err:
        print(f"Erro-> {err}")
        print("Contato não Removido")


# def atualizar_registro() -> None:
#     cliente = procurar_registro()
#     if cliente is None:
#         print("Nenhum Cliente encontrado com esses parâmetros")
#         return
#     conexao = gerar_conexao_db()
#     cursor = conexao.cursor()
    
#     nome = input("Digite o nome completo Atualizado ( <Enter> para não mudar )") or cliente.nome
#     telefone = input("Digite o telefone Atualizado ( <Enter> para não mudar) ") or cliente.telefone
#     email = input("Digite o email Atualizado ( <Enter> para não mudar) ") or cliente.email
#     data = input("Digite a data (dd/mm/aaaa) Atualizada ( <Enter> para não mudar) ") or cliente.nascimento
    
#     try:
#         sql_atualizar = f"""
# UPDATE {nome_tabela}
# SET NOME = :1, TELEFONE = :2, EMAIL = :3, DATA = :3
# WHERE NOME = :5
#         """
#         set_collum = []
#         conditions = {}
#         if nome != cliente.nome:
#             set_collum.append("NOME = :nome")
#             conditions['nome'] = nome

#         if telefone != cliente.telefone:
#             set_collum.append("TELEFONE = :telefone")
#             conditions['telefone'] = telefone 

#         if email != cliente.email:
#             set_collum.append("EMAIL = :email")
#             conditions['email'] = email

        

        
#         cursor.execute(sql_atualizar,nome,telefone,email,data,cliente )
#         conexao.commit
#         print(f"Dados do cliente {cliente}")

    

    





def ler_registros():

    print("""Sub menu (3) Ler registros, escolha uma opção:
                (1) Atualizar o registro
                (2) Remover o Registro
                (0) Voltar
>""", end="")
    escolha = input()
    if escolha == "1":
        procurar_registro()
    elif escolha == "2":
        remover()


def opcao_invalida():
    print("Opção inválida, tecle [Enter] para prosseguir")
    input(">", end="")

def cadastrar() -> Contato:
    """
        Função para pedir os dados de contato, e retorna um objeto do tipo Contato
    """
    print("\nCadastro de Contato:")
    nome = input("Nome Completo> ")
    telefone = input("Telefone (11) 01111-1111> ")
    email = input("Email XXXXXXXX@XXXX.COM> ")
    nascimento = input("Nascimento DD/MM/AAAA> ")
    
    if len(nome) > 5 and len(telefone) > 5 and len(email) > 5 and len(nascimento) == 10:
        try:
            date_format = '%d/%m/%Y'
            nascimento_date = datetime.strptime(nascimento, date_format)
            if nascimento_date < datetime.now():
                return Contato(nome, telefone, email, nascimento_date)
            else:
                print("Data de nascimento inválida!")
        except ValueError:
            print("Data de nascimento no formato inválido")
    else:
        print("Os valores precisam ser preenchidos com mais de 5 caracteres em cada campo!")
    return None

if __name__ == "__main__":
    exec = True
    while exec:
        menu_principal()
        escolha = input()

        if escolha == "1":
            if gerar_tabela():
                print("Tabela gerada com sucesso!")
            else:
                print("Falha ao gerar tabela")

        elif escolha == "2":
            contato = cadastrar()
            if contato is not None:
                if gravar_db(contato):
                    print("Contato cadastrado com sucesso!")
                else:
                    print("Falha ao cadastrar o contato.")
            else:
                print("Contato inválido!")
        elif escolha == "3":
            ler_registros()
        elif escolha == "0":
            exec = False
        else:
            opcao_invalida()
        input("Tecle <Enter> para continuar")

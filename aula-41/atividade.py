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

def gravar_db(contato: Contato) -> bool:
    conexao = gerar_conexao_db()
    cursor = conexao.cursor()
    sql_insert = """
         INSERT INTO EX_CONTATOS (nome, telefone, email, nascimento) VALUES (:1, :2, :3, :4)"""
    
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

    sql_create = """
CREATE TABLE EX_CONTATOS(
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

def ler_registros():
    print("""Sub menu (3) Ler registros, escolha uma opção:
                (1) Atualizar o registro
                (2) Remover o Registro
                (0) Voltar
>""", end="")
    escolha = input()

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

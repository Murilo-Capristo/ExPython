import oracledb
from oracledb import Connection
import os
from contato import Contato

class ContatoRepositorioDB:
    def __init__(self):
        self.usuario = os.environ.get("FIAP_ORACLE_USER")
        self.senha = os.environ.get("FIAP_ORACLE_PASS")
        self.db_path="oracle.fiap.com.br:1521/orcl"

    def gerar_conexao(self) -> Connection:
        con = oracledb.connect(
            user=self.usuario,
            password=self.senha,
            dsn = self.db_path
        )
        return con
    
    def cadastrar(self, contato : Contato) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor
        sql = "insert into Contatos (nome, telefone, email) values (:1, :2, :2)"
        try:
            cursor.execute(sql, (contato.nome, contato.telefone ,contato.email ))
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True
    
    def pesquisar_por_nome(self, nome : str) -> list:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = "select from contatos where nome like :1"
        cursor.execute(sql, ("%" + nome + "%" , ))
        resultado = []
        for dados in cursor:
            c1 = Contato(dados[0],
                        dados[1],
                        dados[2],
                        dados[3])
            resultado.append(c1)
            
        conexao.close()
        return resultado
    
    def remover(self, contato_id : int) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = "delete from contatos where id = :1"
        try:
            cursor.execute(sql, contato_id)
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True        
    
    def atualizar(self, contato_id : int, contato : Contato) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql = "update contatos set nome = :1, telefone = :2, email = :3 where id = :4"
        try:
            cursor.execute(sql, (contato.nome, contato.telefone, contato.email, contato_id))
            conexao.commit()
        except Exception:
            conexao.rollback()
            return False
        conexao.close()
        return True
    
    def gerar_tabela(self) -> bool:
        conexao = self.gerar_conexao()
        cursor = conexao.cursor()
        sql_check = "select 1 from contatos"
        sql_drop = "drop table contatos cascade constraints"
        sql_create =  """
            CREATE TABLE contatos (
                id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
                nome varchar2(100),
                telefone varchar2(20),
                email varchar2(50)
            )
            """
        resultado = None
        try:
            print("Testando se a tabela existe...")
            resultado = cursor.execute(sql_check)
            print("Resultado: ", resultado)
            if resultado:
                print("Dropando a tabela e suas constraints")
                cursor.execute(sql_drop)
                conexao.commit()
        except Exception:
            print("Tabela não existe")
        try:
            print("Criando a tabela")
            cursor.execute(sql_create)
            conexao.commit()
        except Exception as err:
            print("Erro: ", err)
            conexao.rollback()
            return False
        conexao.close()
        return True
            
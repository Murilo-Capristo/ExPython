import os
import oracledb
from contato_model import Contato



class ContatoRepository:
    user : str = ""
    passw : str = ""
    url = str = ""

    def __init__(self):
        self.user = os.environ.get("FIAP_ORACLE_USER")
        self.passw = os.environ.get("FIAP_ORACLE_PASS")
        self.url = os.environ.get("FIAP_ORACLE_URL")
        print("Contato Repository Gerado")
        pass

    def gerarConexao(self):
        conexao = oracledb.connect(
            user=self.user,
            password = self.passw,
            dsn=self.url
        )
        return conexao

    def ler_todos(self) -> list:
        conexao = self.gerarConexao()
        cursor = conexao.cursor()
        cursor.execute("Select * from contatos")
        resultado = []
        for contato in cursor:
            c1 = Contato(
                contato[0],
                contato[1],
                contato[2],
                contato[3]
            )
            resultado.append(c1)
        conexao.close()
        return resultado
        
        

    def salvar(self, contato : Contato):
        conexao = self.gerarConexao()
        cursor= conexao.cursor()
        try:
            cursor.execute("insert into contatos (nome, telefone, email) values(:1, :2, :3)",(contato.nome, contato.telefone, contato.email,))
            conexao.commit()
        except Exception as e:
            print(e)
            print("Erro ao salvar o cliente")
            conexao.rollback()

        conexao.close()
    

#  Fazer em Kivy O TESTE-CONEXAO-O

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

import os
import oracledb

usuario = os.environ.get("FIAP_ORACLE_USER")
senha = os.environ.get("FIAP_ORACLE_PASS")

con = oracledb.connect(user=usuario, 
                       password=senha, 
                       dsn="oracle.fiap.com.br:1521/orcl")
print("Database version:", con.version)
def criar_tabela():
    try: 
        cursor = con.cursor()
        cursor.execute("""
            CREATE TABLE Contatos (
                id NUMBER(9) not null,
                nome VARCHAR2(100),
                telefone VARCHAR2(30),
                email VARCHAR2(100),
                CONSTRAINT Contato_pk PRIMARY KEY (id)
            )
        """)
        con.commit()
    except:
        None

    

class AppAgenda2 ( App):






    txt_id = TextInput(size_hint=(0.7,1.0))
    txt_nome = TextInput(size_hint=(0.7,1.0))
    txt_email = TextInput(size_hint=(0.7,1.0))
    txt_telefone = TextInput(size_hint=(0.7,1.0))

    def inserir( self, e):
        print("Botão Pressionado")
        try:
            cursor = con.cursor()
            sql = (f"""  INSERT INTO Contatos (id, nome, telefone, email) VALUES (:1, :2, :3, :4)""" )
            cursor.execute(sql,(int(self.txt_id), self.txt_nome, self.txt_telefone, self.txt_email))
            con.commit()
        except:
            print("Erro ao inserir contato.")
    

        



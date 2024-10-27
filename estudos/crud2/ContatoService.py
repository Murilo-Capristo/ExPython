import json
import requests
from contato import Contato

class ContatoService:
    def __init__(self):
        self.URL_BASE = "https://tdspm-f7cb0-default-rtdb.firebaseio.com"

    def salvar(self, contato : Contato) -> bool:
        contato_json = contato.to_dict()
        response = requests.post(url=f"{self.URL_BASE}/contatos.json",
                                 json = contato_json, timeout=5.0)
        return response.status_code == 200
    
    def ler_todos(self) -> list:
        response = requests.get(url=f"{self.URL_BASE}/contatos.json", timeout=5.0)
        lista = []
        if response.status_code == 200:
            dicionario = json.loads(response.text) #json.loads é para transformar em dict
            for item in dicionario.items():
                contato_dict = item[1]
                c1 = Contato(nome = contato_dict.get("nome", ""),
                             telefone = contato_dict.get("telefone", ""),
                             email = contato_dict.get("email", ""),
                             contato_id=item[0])
                lista.append(c1)
        return lista
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from contato_repository import ContatoRepository
from contato_model import Contato
# repository = ContatoRepository()
class ContatoBackend( BaseHTTPRequestHandler ):
    # def __init__(self, *args, **kvargs):
    #     # super.__init__(self)
    #     self.repository = ContatoRepository()
    



    def do_GET(self):
        print("Conexao recebida!")
        try:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()

            lista = []
            lista.extend(repository.ler_todos())
            texto_json = json.dumps(lista, default=vars)
            self.wfile.write(texto_json.encode('latin1'))
        except Exception as e:
            self.send_response(500)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Erro ao acessar o banco de dados".encode('latin1'))

    def do_POST(self):
        print("Conexão POST recebida")
        try:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()

            # Ler corpo do request para pegar os dados do contato
            texto = ""
            bytes_faltantes = int(self.headers['content-lenght'])
            
            line = self.rfile.read(bytes_faltantes)
            texto += line.decode('latin1')
            print("Lido: ", texto)
            bytes_faltantes -= len(line)
            dicionario_contato = json.loads(texto)
            contato = Contato(
                nome=dicionario_contato.get("nome", ""),
                telefone=dicionario_contato.get("telefone", ""),
                email=dicionario_contato.get("email", ""))
            repository.salvar(contato  )
        except Exception as e:
            print(e)
            self.send_response(500)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Erro ao acessar o banco de dados".encode('latin1'))




if __name__ == "__main__":
    repository = ContatoRepository()
    print("Backend iniciado")
    http_server = HTTPServer( ('127.0.0.1', 80), ContatoBackend)
    print("Http server iniciado, aguardando informações")
    http_server.serve_forever()
    

import socket

HOST = "127.0.0.1"
PORT = 10000
servidor = socket.socket(   socket.AF_INET,
                            socket.SOCK_STREAM)

print("Servidor Criado")
servidor.bind( (HOST,PORT))
print(f"Servidor Conectado na interface {HOST} na porta {PORT}")
print(f"Aguardando cliente se conectar na porta {PORT}")
servidor.listen()

cliente_conexao, cliente_address = servidor.accept()
print(f"Cliente no endereço {cliente_address} conectou no servidor")
mensagem = input("Mande uma mensagem de carinho: ")
cliente_conexao.sendall(mensagem.encode("utf-8"))

while True:
    mensagem_bytes = cliente_conexao.recv(1024)
    texto = mensagem_bytes.decode("utf-8")
    print(texto, end="")
    if texto == "*":
        break
    
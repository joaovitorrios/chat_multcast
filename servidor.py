import socket
import threading

clientes = []

def broadcast(mensagem, cliente_atual):
    for cliente in clientes:
        if cliente != cliente_atual:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                clientes.remove(cliente)

def handle_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            broadcast(mensagem, cliente)
        except:
            clientes.remove(cliente)
            cliente.close()
            break

def main():
    host = '127.0.0.1'
    porta = 5555

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()

    print(f"[Servidor] Rodando em {host}:{porta}")

    while True:
        cliente, endereco = servidor.accept()
        print(f"[Conectado] {endereco}")
        clientes.append(cliente)
        thread = threading.Thread(target=handle_cliente, args=(cliente,))
        thread.start()

if __name__ == "__main__":
    main()


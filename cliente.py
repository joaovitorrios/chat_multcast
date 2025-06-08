import socket
import threading

def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            print(mensagem)
        except:
            print("Erro ao receber mensagem.")
            cliente.close()
            break

def main():
    host = '127.0.0.1'
    porta = 5555

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    nome = input("Digite seu nome: ")

    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread_receber.start()

    while True:
        mensagem = input()
        cliente.send(f"{nome}: {mensagem}".encode('utf-8'))

if __name__ == "__main__":
    main()

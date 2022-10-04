import socket
import threading


counter = 0


    
def globalMessage(message):
    for client in clients:
        message = client.recv(2048).decode('ascii')
        if message == 'acertei uma letra':
            client.send('jogador {client} acertou 1 letra')
        if message == 'errei uma letra':
            client.send('jogador {client} perdeu 1 vida')

def fimDoJogo(message):
    if message == 'morri':
        s.send('imprime_mensagem_perdedor')
        #para o jogador que morreu
        s.send('imprime_mensagem_vencedor')
        #para o jogador que sobrou pode ou nao ter terminado   
    if message == 'terminei':
        s.send('imprime_mensagem_vencedor')
        #para o jogador que ganhou
        s.send('imprime_mensagem_perdedor')
        #para o jogador que que perdeu

    
if(__name__ == '__main__'):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1",3465))
    s.listen(2)
    print(f"Servidor está ONLINE 127.0.0.1:3465")

    clients = []
    usernames = [] 
    while True:
        try:
            client, address = s.accept()
            print(f"New Connetion: {address}")
            client.send('getUser'.encode('ascii'))
            username = client.recv(2048).decode('ascii')
            clients.append(client)
            username.append(username)
            user_thread = threading.Thread(target=client())
            user_thread.start()
        except:
            pass
    
    
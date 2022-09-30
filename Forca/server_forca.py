import socket
import threading

counter = 0


    
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

    
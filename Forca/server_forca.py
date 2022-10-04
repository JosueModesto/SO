import socket
from threading import Thread
counter = 0

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == "0"):
                client.send('terminei')
                print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(palavra_secreta.upper()))
        else:
            erros += 1
            print(letras_acertadas)
            print('Ainda faltam acertar {} letras'.format(letras_faltando))
            print('Você ainda tem {} tentativas'.format(7-erros))
            desenha_forca(erros)
            client.send('errei uma letra')

        enforcou = erros == 7
        client.send('morri')
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        msg = client.recv(1024).decode('ascii')
        if msg == 'imprime_mensagem_vencedor': 
            imprime_mensagem_vencedor()
        else:
            imprime_mensagem_perdedor()

    print("Fim do jogo")
    
def globalMessage(message):
    message = s.recv(2048).decode('ascii')
    nick = 'fulano'
    for s in client_list:
        if message == 'acertei uma letra':
            s.send(f'{client_list[nick]} acertou 1 letra','ascii')
        if message == 'errei uma letra':
            s.send(f'{client_list[nick]} perdeu 1 vida','ascii')

def fimDoJogo(message):
    message = client_list[nick].recv(2048).decode('ascii')
    if message == 'morri':
        s.send('imprime_mensagem_perdedor','ascii')
        #para o jogador que morreu
        s.send('imprime_mensagem_vencedor','ascii')
        #para o jogador que sobrou pode ou nao ter terminado   
    if message == 'terminei':
        s.send('imprime_mensagem_vencedor','ascii')
        #para o jogador que ganhou
        s.send('imprime_mensagem_perdedor','ascii')
        #para o jogador que que perdeu

    
if(__name__ == '__main__'):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1",3465))
    s.listen(2)
    print(f"Servidor está ONLINE 127.0.0.1:3465")

    threads = list()
    client_list = dict()

    for nick in ('fulano', 'ciclano'):
            client, address = s.accept()
            th = threads(target=jogar, atgs=((client,)))
            th.start()
            threads.append(th)
            client_list[nick]=client

            for th in threads:
                th.join

            for cl in client_list:
                cl.close

    
client_list['fulano'].send()
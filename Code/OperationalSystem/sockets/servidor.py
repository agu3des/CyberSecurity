import socket
from pathlib import Path

HOST = '127.0.0.1'
PORT = 5000

print('=== Servidor ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

def trata_opcoes(msg):
    # 1 /tmp
    operacao, caminho = msg.split(sep=':')
    caminho = Path(caminho)
  
    # LERDIR:/tmp/
    # CRIARDIR:/tmp/eu
    # EXCLUIRDIR:/tmp/eu
    # MOSTRAR:/tmp/eu/proxima_prova.txt

    msg = ''
    res = ''
    # Realiza a ação correspondente à opção do usuário
    if operacao == "LERDIR":
      # Mostra o conteúdo do diretório atual
      print('LERDIR:' + str(caminho))
      res += f'\nArquivos e pasta escontrados em {caminho}\n'
      for arquivo in caminho.iterdir():
        res += str(arquivo) + '\n'
    elif operacao == "CRIARDIR":
      # Cria um novo diretório
      print('CRIARDIR:' + str(caminho))
      caminho.mkdir(parents=True, exist_ok=True)
      res += f'\nPasta {caminho} criada com sucesso!\n'
    elif operacao == "EXCLUIRDIR":
      # Exclui um diretório
      print('EXCLUIRDIR:' + str(caminho))
      caminho.rmdir()
      res += f'\nPasta {caminho} excluída com sucesso!\n'
    elif operacao == "MOSTRAR":
      # Mostra o conteúdo de um arquivo
      print('MOSTRAR:' + str(caminho))
      res += f'\nLendo de {caminho}:\n'
      res += str(caminho.read_text())
    return res

while True:
    msg, cliente = udp.recvfrom(1024)
    res = trata_opcoes(msg.decode())
    print('Recebi de', cliente, 'a mensagem', msg.decode(encoding="utf-8"))

    # mini protocolo
    # LERDIR:/tmp/
    # CRIARDIR:/tmp/eu
    # EXCLUIRDIR:/tmp/eu
    # MOSTRAR:/tmp/eu/proxima_prova.txt



    resposta = 'mensagem recebida com sucesso!'
    udp.sendto(resposta.encode(), cliente)
    print('Resposta enviada!')
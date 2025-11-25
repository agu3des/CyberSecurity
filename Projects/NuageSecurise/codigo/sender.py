import socket
from diffie_hellman import DiffieHellman
from des import DES

# Configuração do cliente
host = 'localhost'
porta = 8004

# Parâmetros públicos (g e p)
g = 6
p = 745153968374 

# Inicializando o remetente (cliente) Diffie-Hellman
remetente = DiffieHellman(g, p)

# Criando socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:

    cliente_socket.connect((host, porta))
    print(f"Conectado ao servidor {host}:{porta}")

    # Envia a chave pública do remetente para o receptor
    cliente_socket.sendall(str(remetente.chave_publica).encode())
    print(f"Chave pública do remetente enviada: {remetente.chave_publica}")

    # Recebe a chave pública do receptor
    chave_publica_receptor = int(cliente_socket.recv(1024).decode())
    print(f"Chave pública do receptor recebida: {chave_publica_receptor}")

    # Calcula a chave compartilhada
    chave_compartilhada = str(remetente.gerar_chave_compartilhada(chave_publica_receptor))
    
    # Utiliza a chave comum Diffie-Hellman como a chave do DES
    des = DES(chave_compartilhada)
    
    # Enviar mensagem criptografada
    mensagem = input("Enviar mensagem: ")
    mensagem_criptografada = des.encrypt(mensagem)
    cliente_socket.sendall(mensagem_criptografada.encode())
    input('Pressione Enter para ver a mensagem criptografada ')
    
print(mensagem_criptografada)

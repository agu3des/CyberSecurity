import socket
from diffie_hellman import DiffieHellman
from des import DES

# Configuração do servidor
host = 'localhost'
porta = 8004

# Parâmetros públicos (g e p)
g = 6
p = 745153968374 
    
# Inicializando o receptor (servidor) Diffie-Hellman
receptor = DiffieHellman(g, p)

# Cria uma comunicação via socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
    servidor_socket.bind((host, porta)) 
    servidor_socket.listen(1)
    print(f"Aguardando conexão na porta {porta}...")

    conexao, endereco = servidor_socket.accept()
    with conexao:
        print(f"Conectado a: {endereco}")
        
        # Recebe a chave pública do remetente
        chave_publica_remetente = int(conexao.recv(1024).decode())
        print(f"Chave pública do remetente recebida: {chave_publica_remetente}")

        # Envia a chave pública do receptor para o remetente
        conexao.sendall(str(receptor.chave_publica).encode())
        print(f"Chave pública do receptor enviada: {receptor.chave_publica}")

        # Calcula a chave compartilhada
        chave_compartilhada = str(receptor.gerar_chave_compartilhada(chave_publica_remetente))

        # Utiliza a chave comum Diffie-Hellman como a chave do DES
        des = DES(chave_compartilhada)
        
        # Recebe a mensagem criptografada
        mensagem_criptografada = conexao.recv(1024).decode()
        print(mensagem_criptografada)
        input('Pressione Enter para descriptografar a mensagem ')

    print(f"Mensagem descriptografada: {des.decrypt(mensagem_criptografada)}")

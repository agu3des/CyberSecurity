### **1. Configuração do Cliente**
O código configura um cliente que se conecta a um servidor via sockets e usa Diffie-Hellman para troca de chaves seguras:

- `host`: Define o endereço do servidor (`localhost`).
- `porta`: Define a porta usada para comunicação.
- `cliente_socket`: Objeto socket criado para comunicação.

### **2. Implementação do Diffie-Hellman**
O cliente usa Diffie-Hellman para estabelecer uma chave compartilhada:

- `g`: Base pública do protocolo.
- `p`: Número primo usado como módulo.
- `remetente = DiffieHellman(g, p)`: Instância do Diffie-Hellman para gerar a chave compartilhada.

### **3. Processo de Comunicação**
A troca de mensagens entre cliente e servidor ocorre da seguinte forma:

1. **Estabelecimento da Conexão**
   - O cliente se conecta ao servidor com `cliente_socket.connect((host, porta))`.

2. **Troca de Chaves Diffie-Hellman**
   - O cliente envia sua chave pública ao servidor.
   - Recebe a chave pública do servidor.
   - Calcula a chave compartilhada com `gerar_chave_compartilhada()`.

3. **Criptografia com DES**
   - A chave compartilhada Diffie-Hellman é usada como chave do algoritmo DES.
   - O cliente solicita uma mensagem ao usuário.
   - A mensagem é criptografada e enviada ao servidor.

### **4. Envio da Mensagem Criptografada**
A mensagem digitada pelo usuário é criptografada e enviada ao servidor com:

```python
mensagem_criptografada = des.encrypt(mensagem)
cliente_socket.sendall(mensagem_criptografada.encode())
```
Após a transmissão, a mensagem criptografada pode ser exibida pressionando Enter.
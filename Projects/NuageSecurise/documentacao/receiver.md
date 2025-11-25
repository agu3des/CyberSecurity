### **1. Configuração do Servidor**
O código configura um servidor que utiliza Diffie-Hellman para troca de chaves e DES para criptografia:

- `host`: Define o endereço do servidor (neste caso, `localhost`).
- `porta`: Define a porta onde o servidor escutará conexões.
- `servidor_socket`: Objeto socket criado para comunicação.

### **2. Implementação do Diffie-Hellman**
O protocolo Diffie-Hellman é usado para gerar uma chave compartilhada segura:

- `g`: Base pública do protocolo.
- `p`: Número primo usado como módulo.
- `receptor = DiffieHellman(g, p)`: Instância do Diffie-Hellman que calculará a chave compartilhada.

### **3. Processo de Comunicação**
A comunicação entre cliente e servidor ocorre via sockets:

1. **Estabelecimento da Conexão**
   - O servidor aguarda conexões (`servidor_socket.listen(1)`).
   - Aceita conexões (`conexao, endereco = servidor_socket.accept()`).

2. **Troca de Chaves Diffie-Hellman**
   - O servidor recebe a chave pública do cliente.
   - Envia sua chave pública ao cliente.
   - Calcula a chave compartilhada com `gerar_chave_compartilhada()`.

3. **Criptografia com DES**
   - A chave compartilhada Diffie-Hellman é usada para inicializar o algoritmo DES.
   - O servidor recebe uma mensagem criptografada.
   - O usuário pode pressionar Enter para visualizar a mensagem descriptografada.

### **4. Descriptografia com DES**
A mensagem criptografada recebida é descriptografada usando:

```python
des.decrypt(mensagem_criptografada)
```
Essa operação converte o texto cifrado de volta ao formato original.
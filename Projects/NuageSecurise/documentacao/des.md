
# Documentação - Implementação do Algoritmo DES
## Introdução
Este documento descreve a implementação do algoritmo `DES`, bem como funções auxiliares. O código implementa a classe DES, que representa a criptografia Data Encryption Standard. É um algoritmo de criptografia simétrica de blocos, que opera em blocos de 64 bits, usando uma chave de 56 bits (com 8 bits adicionais usados como bits de paridade).

O código define as etapas principais do DES:
1. **Pré-processamento da chave e da mensagem**.
2. **Geração das subchaves** para cada uma das 16 rodadas.
3. **Permutações, expansões e substituições** usando tabelas pré-calculadas.
4. **Rodadas Feistel** para processar os blocos da mensagem.

## **Documentação do Código**

### **1. Atributos da Classe**
A classe `DES` usa tabelas pré-definidas para operações de permutação e substituição:
- `__ip_tabela`: Tabela de permutação inicial (IP).
- `__pc1_tabela`: Permutação PC-1 usada para gerar chaves.
- `__shift_schedule`: Quantidade de deslocamentos para cada rodada na geração de subchaves.
- `__pc2_tabela`: Permutação PC-2 usada para reduzir a chave a 48 bits.
- `__exp_tabela`: Expansão de 32 para 48 bits do bloco direito em cada rodada Feistel.
- `__s_boxes`: Conjunto de 8 caixas de substituição (S-Boxes) usadas para compactar blocos de 6 bits em 4 bits.
- `__permutacao_tabela`: Tabela de permutação usada após as substituições.
- `__ip_f_inversa_tabela`: Permutação final (inversa de IP).

### **2. Métodos**
#### **Construtor: `__init__`**
Recebe uma chave como entrada e a processa:
1. Converte a chave de string para binário.
2. Aplica um padding (caso necessário) para garantir que tenha 64 bits.
3. Salva o resultado na variável `__key`.

#### **Pré-processamento da Mensagem**
- `__para_binario(input)`: Converte uma string de entrada em binário, representando cada caractere com 8 bits.
- `__add_pad_bits(input_bin)`: Adiciona zeros ao final de uma string binária até que ela tenha exatamente 64 bits.
- `__preprocessar_menssagem(menssagem_str)`: Converte a mensagem em binário, divide em blocos de 64 bits e adiciona padding.

### **Pré-processamento da Chave**
`__preprocessar_chave(chave_str)`: Converte a chave em binário, adiciona padding se necessário e garante que tenha 64 bits.

### **Geração de Subchaves**
`__gerar_subchaves()`: Gera as 16 subchaves necessárias para o algoritmo, aplicando as tabelas PC1 e PC2 e deslocamentos adequados.

### **Permutações e Expansões**
`__permutacao_inicial(bloco)`: Aplica a permutação inicial ao bloco de 64 bits com base na ip_tabela.
`__separar_bloco(bloco)`: Divide um bloco de 64 bits em duas metades de 32 bits.
`__expand_metade(metade_bloco)`: Expande a metade direita do bloco para 48 bits usando a tabela de expansão.

### **Substituições e Permutações**
`__substituir(bloco)`: Divide o bloco de 48 bits em 8 segmentos de 6 bits e substitui utilizando as S-boxes.
`__feistel_round(esquerda, direita, subchave)`: Executa uma rodada do Feistel Network, aplicando expansão, XOR com subchave, substituição e permutação P.
`__inversa_permutacao_inicial(bloco)`: Aplica a permutação final inversa ao bloco de 64 bits.

### **Conversões**
`__bin_to_ascii(binary_str)`: Converte uma string binária para uma representação ASCII.
`__bin_to_hex(binary_str)`: Converte uma string binária para hexadecimal.
`__hex_to_bin(hex_str)`: Converte uma string hexadecimal para binário.

### **Funções de Criptografia e Descriptografia**
`encrypt(plaintext)`: Converte a mensagem em blocos de 64 bits, aplica permutação inicial, Feistel rounds, permutação final e retorna o texto cifrado em hexadecimal.
`decrypt(hex)`: Converte o hexadecimal em binário, executa o processo inverso da criptografia e retorna o texto original.


### **Fluxo Completo do DES**
1. Pré-processar a chave e a mensagem.
2. Gerar subchaves.
3. Processar cada bloco com a permutação inicial, rodadas Feistel e permutação final.
4. Retornar o texto cifrado.



# Documentação - Implementação do Protocolo Diffie-Hellman

## Introdução
Este documento descreve a implementação do protocolo de troca de chaves seguras `Diffie-Hellman`, bem como funções auxiliares utilizadas para a geração de números aleatórios e primos. O protocolo permite que duas partes estabeleçam uma chave secreta compartilhada de maneira segura em um canal de comunicação público.

## 1. Funções Utilitárias

### 1.1 `generate_random_number(start=1, end=100)`

**Descrição:** 
Gera um número aleatório dentro do intervalo especificado.

**Parâmetros:**
- `start` (int): Valor inicial do intervalo (inclusivo). Padrão: 1.
- `end` (int): Valor final do intervalo (inclusivo). Padrão: 100.

**Retorno:**
- (int) Um número inteiro aleatório dentro do intervalo definido.


### 1.2 `generate_random_prime(start=2, end=100)`

**Descrição:**
Gera um número primo aleatório dentro do intervalo especificado.

**Parâmetros:**
- `start` (int): Valor inicial do intervalo (inclusivo). Padrão: 2.
- `end` (int): Valor final do intervalo (inclusivo). Padrão: 100.

**Retorno:**
- (int) Um número primo aleatório dentro do intervalo definido.

**Implementação:**
A função verifica a primalidade de um número gerado aleatoriamente e repete o processo até encontrar um número primo.


## 2. Classe `DiffieHellman`

A classe `DiffieHellman` implementa o protocolo de troca de chaves Diffie-Hellman.

### 2.1 `__init__(self, g, p)`

**Descrição:**
Inicializa a instância do protocolo Diffie-Hellman.

**Parâmetros:**
- `g` (int): Gerador de módulo.
- `p` (int): Número primo.

**Atributos Privados:**
- `__g`: Gerador de módulo.
- `__p`: Número primo.
- `__private_key`: Chave privada gerada aleatoriamente.
- `public_key`: Chave pública derivada da chave privada.


### 2.2 `__generate_private_key(self)`

**Descrição:**
Gera a chave privada como um número primo aleatório no intervalo entre 2 e 3333.

**Retorno:**
- (int) Chave privada aleatória.


### 2.3 `__generate_public_key(self)`

**Descrição:**
Calcula a chave pública baseada na chave privada e nos parâmetros de entrada.

**Fórmula:**
```
Chave Pública = (g^Chave Privada) mod p
```

**Retorno:**
- (int) Chave pública.


### 2.4 `generate_shared_key(self, public_key_other)`

**Descrição:**
Gera a chave compartilhada a partir da chave pública do outro participante.

**Fórmula:**
```
Chave Compartilhada = (Chave Pública Outro^Chave Privada) mod p
```

**Parâmetros:**
- `public_key_other` (int): Chave pública do outro participante.

**Retorno:**
- (int) Chave compartilhada.

### 2.5 `gerar_numero_aleatorio(self, inicio=1, fim=100)`

**Descrição:**  
Gera um número inteiro aleatório dentro do intervalo especificado.

**Parâmetros:**  
- `inicio` (int, opcional): Valor mínimo do intervalo (inclusivo). Padrão: 1.  
- `fim` (int, opcional): Valor máximo do intervalo (inclusivo). Padrão: 100.  

**Retorno:**  
- (int) Número inteiro aleatório dentro do intervalo especificado.

---

### 2.6 `gerar_numero_primo_aleatorio(self, inicio=2, fim=100)`

**Descrição:**  
Gera um número primo aleatório dentro do intervalo especificado.

**Parâmetros:**  
- `inicio` (int, opcional): Valor mínimo do intervalo (inclusivo). Padrão: 2.  
- `fim` (int, opcional): Valor máximo do intervalo (inclusivo). Padrão: 100.  

**Retorno:**  
- (int) Número primo aleatório dentro do intervalo especificado.  

**Detalhes da Implementação:**  
- A função verifica se um número é primo usando um teste de divisibilidade simples.  
- Um número aleatório é gerado repetidamente até que um número primo seja encontrado dentro do intervalo.

## 3. Conclusão
Esta implementação do protocolo Diffie-Hellman permite a troca segura de chaves entre dois participantes usando números primos e operações modulares exponenciais. As funções auxiliares garantem a geração segura de números aleatórios e primos necessários para o processo.


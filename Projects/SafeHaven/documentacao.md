# Implementação do Algoritmo MD5 em Python

O **MD5 (Message Digest Algorithm 5)** é um algoritmo de hash criptográfico que gera um valor fixo de **128 bits (16 bytes)** a partir de uma entrada de qualquer tamanho.

---

## 1. Estrutura da Classe `MD5`

A classe `MD5` encapsula todos os detalhes do cálculo do hash, incluindo funções auxiliares e valores de estado.

### 1.1 Atributos

* **\_s** → Lista de deslocamentos cíclicos usados em cada uma das 64 etapas. Esses valores são fixados pelo padrão MD5.
* **\_k** → Constantes derivadas das raízes cúbicas dos números primos. Cada constante é:

  $$
  k[i] = \text{int}\Big((2^{32}) \times |\sin(i+1)|\Big)
  $$
* **\_buffers** → Os quatro registradores de estado inicial do MD5 (valores fixos):

  * A = `0x67452301`
  * B = `0xEFCDAB89`
  * C = `0x98BADCFE`
  * D = `0x10325476`
* **\_original\_len** → Armazena o tamanho total dos dados processados, em bits.
* **\_buffer** → Guarda blocos de 64 bytes (512 bits) para processamento. Se a entrada ainda não tiver 64 bytes, permanece aqui até acumular.

---

## 2. Métodos

### 2.1 `_left_rotate(x, c)`

Executa uma rotação **à esquerda** no número `x` por `c` posições:

```python
return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF
```

👉 Essa operação garante a mistura adequada dos bits.

---

### 2.2 `update(input_bytes)`

Recebe dados e os adiciona ao buffer.
Sempre que o buffer acumula **64 bytes**, chama `_process_chunk`.

```python
while len(self._buffer) >= 64:
    self._process_chunk(self._buffer[:64])
    self._buffer = self._buffer[64:]
```

---

### 2.3 `_process_chunk(chunk)`

Processa o **bloco principal** do MD5.

* **Entrada** → bloco de 64 bytes.
* **Saída** → atualiza os buffers (A, B, C, D).

Etapas internas:

1. Decodifica o bloco em 16 inteiros de 32 bits (`struct.unpack`).
2. Executa 64 iterações divididas em 4 fases:

   * **Etapa 1** → `(b & c) | (~b & d)`
   * **Etapa 2** → `(d & b) | (~d & c)`
   * **Etapa 3** → `b ^ c ^ d`
   * **Etapa 4** → `c ^ (b | ~d)`
3. Atualiza os registradores com soma modular e rotação à esquerda.

---

### 2.4 `digest()`

Gera o hash MD5 final.

1. **Padding**:

   * Adiciona `0x80`.
   * Preenche com `0x00` até o tamanho ser ≡ 56 (mod 64).
2. **Comprimento**:

   * Insere o tamanho original dos dados (em bits) como um inteiro de 64 bits.
3. **Processamento Final**:

   * Executa `_process_chunk` no último bloco.
4. **Saída**:

   * Retorna o hash em 16 bytes.

---

### 2.5 `hexdigest()`

Converte o resultado em **hexadecimal** (32 caracteres).

---

## 3. Exemplo de Uso

```python
data = b"Hello World"
md5 = MD5()
md5.update(data)
print(md5.hexdigest())
```

**Entrada**:

```
b"Hello World"
```

**Saída esperada**:

```
b10a8db164e0754105b7a99be72e3fe5
```

---

## 4. Resumindo o Funcionamento

1. Divide os dados em blocos de 64 bytes.
2. Processa cada bloco em **64 etapas** com operações bitwise, soma modular e rotações.
3. Adiciona **padding** e o **comprimento original** da entrada.
4. O resultado final é um hash de **128 bits**, exibido como **32 caracteres hexadecimais**.

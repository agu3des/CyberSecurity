import struct
import math
import time

class MD5:
    """
    Implementação manual do algoritmo de hash MD5 (RFC 1321).
    
    Características:
    - Processa mensagens de tamanho arbitrário em blocos de 512 bits (64 bytes).
    - Produz um digest final de 128 bits (16 bytes).
    - Compatível com hashlib.md5 em termos de saída.
    - Suporta uso incremental via `update()`, e clonagem de estado via `copy()`.
    """

    def __init__(self):
        """
        Inicializa o estado interno do MD5:
        - Vetores de rotação (s).
        - Constantes derivadas do seno (k).
        - Buffers (A, B, C, D).
        - Comprimento da mensagem original (em bits).
        - Buffer temporário para dados não processados (< 64 bytes).
        """
        # Deslocamentos por rodada (cada grupo de 16 passos usa um conjunto diferente)
        self._s = [
            (7, 12, 17, 22),
            (5, 9, 14, 20),
            (4, 11, 16, 23),
            (6, 10, 15, 21)
        ]

        # Constantes K: floor(2^32 * abs(sin(i + 1)))
        self._k = [int((2**32) * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

        # Valores iniciais dos registradores (A, B, C, D)
        self._buffers = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

        # Tamanho acumulado da mensagem em bits
        self._original_len = 0

        # Buffer para armazenar dados até completar 64 bytes
        self._buffer = b""

    def _left_rotate(self, x, c):
        """
        Rotação circular à esquerda de 32 bits.
        Args:
            x (int): Valor a ser rotacionado.
            c (int): Quantidade de bits de rotação.
        Returns:
            int: Valor rotacionado.
        """
        return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

    def update(self, input_bytes):
        """
        Adiciona bytes à mensagem a ser processada.
        Processa blocos completos de 64 bytes conforme necessário.
        
        Args:
            input_bytes (bytes): Mensagem (ou parte dela).
        """
        self._buffer += input_bytes
        self._original_len += len(input_bytes) * 8

        # Processa blocos completos de 64 bytes
        while len(self._buffer) >= 64:
            self._process_chunk(self._buffer[:64])
            self._buffer = self._buffer[64:]

    def _process_chunk(self, chunk):
        """
        Processa um único bloco de 512 bits (64 bytes).
        
        Args:
            chunk (bytes): Bloco de 64 bytes.
        """
        a, b, c, d = self._buffers
        x = list(struct.unpack("<16I", chunk))

        # 64 iterações divididas em 4 rodadas
        for i in range(64):
            if i < 16:
                f = (b & c) | (~b & d)
                g = i
            elif i < 32:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + self._k[i] + x[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + self._left_rotate(f, self._s[i // 16][i % 4])) & 0xFFFFFFFF

        # Atualiza os buffers acumulados
        self._buffers = [
            (self._buffers[0] + a) & 0xFFFFFFFF,
            (self._buffers[1] + b) & 0xFFFFFFFF,
            (self._buffers[2] + c) & 0xFFFFFFFF,
            (self._buffers[3] + d) & 0xFFFFFFFF,
        ]

    def _finalize(self):
        """
        Finaliza o cálculo do hash MD5 sem modificar o estado original.
        
        - Aplica padding (1 bit seguido de zeros até 448 mod 512).
        - Acrescenta comprimento original da mensagem em 64 bits little-endian.
        - Processa blocos finais.
        
        Returns:
            list[int]: Buffers finais [A, B, C, D].
        """
        # Cópia do estado atual
        buffers_copy = self._buffers[:]
        buffer_copy = self._buffer
        length_copy = self._original_len

        # Padding: 0x80 seguido de zeros até alinhar em 56 mod 64
        padding = b"\x80" + b"\x00" * ((56 - (len(buffer_copy) + 1) % 64) % 64)
        length = struct.pack("<Q", length_copy)
        buffer_copy += padding + length

        # Processa blocos finais
        for i in range(0, len(buffer_copy), 64):
            a, b, c, d = buffers_copy
            x = list(struct.unpack("<16I", buffer_copy[i:i+64]))
            for j in range(64):
                if j < 16:
                    f = (b & c) | (~b & d)
                    g = j
                elif j < 32:
                    f = (d & b) | (~d & c)
                    g = (5 * j + 1) % 16
                elif j < 48:
                    f = b ^ c ^ d
                    g = (3 * j + 5) % 16
                else:
                    f = c ^ (b | ~d)
                    g = (7 * j) % 16
                f = (f + a + self._k[j] + x[g]) & 0xFFFFFFFF
                a, d, c, b = d, c, b, (b + self._left_rotate(f, self._s[j // 16][j % 4])) & 0xFFFFFFFF
            buffers_copy = [
                (buffers_copy[0] + a) & 0xFFFFFFFF,
                (buffers_copy[1] + b) & 0xFFFFFFFF,
                (buffers_copy[2] + c) & 0xFFFFFFFF,
                (buffers_copy[3] + d) & 0xFFFFFFFF,
            ]

        return buffers_copy

    def digest(self):
        """
        Retorna o digest MD5 como bytes (16 bytes).
        
        Returns:
            bytes: Digest em formato binário.
        """
        final_buffers = self._finalize()
        return struct.pack("<4I", *final_buffers)

    def hexdigest(self):
        """
        Retorna o digest MD5 como string hexadecimal (32 caracteres).
        
        Returns:
            str: Digest em hexadecimal.
        """
        return "".join(f"{byte:02x}" for byte in self.digest())

    def copy(self):
        """
        Retorna uma cópia independente do estado atual do hash.
        
        Returns:
            MD5: Novo objeto com o mesmo estado.
        """
        clone = MD5()
        clone._s = self._s
        clone._k = self._k
        clone._buffers = self._buffers[:]
        clone._original_len = self._original_len
        clone._buffer = self._buffer
        return clone


# ==============================
# Testes automáticos (RFC 1321)
# ==============================
def self_test():
    """
    Testa a implementação usando vetores oficiais da RFC 1321.
    """
    test_vectors = {
        b"": "d41d8cd98f00b204e9800998ecf8427e",
        b"a": "0cc175b9c0f1b6a831c399e269772661",
        b"abc": "900150983cd24fb0d6963f7d28e17f72",
        b"message digest": "f96b697d7cb7938d525a2f31aaf161d0",
        b"abcdefghijklmnopqrstuvwxyz": "c3fcd3d76192e4007dfb496cca67e13b",
        b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789": "d174ab98d277d9f5a5611c2c9f419d9f",
        b"12345678901234567890123456789012345678901234567890123456789012345678901234567890":
            "57edf4a22be3c955ac49da2e2107b67a",
    }

    for msg, expected in test_vectors.items():
        h = MD5()
        h.update(msg)
        assert h.hexdigest() == expected, f"Falhou para {msg}"

    print("✅ Todos os testes passaram!")


# Execução de exemplo
if __name__ == "__main__":
    self_test()

    start_time_manual = time.time()
    data = b"Hello World"
    md5 = MD5()
    md5.update(data)
    print(f"MD5 Manual: {md5.hexdigest()}")
    end_time_manual = time.time()
    print(f"Tempo de execução manual: {end_time_manual - start_time_manual} segundos")

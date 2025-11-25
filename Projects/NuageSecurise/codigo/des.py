class DES:

    # Variável privada que armazenará a chave de criptografia em binário
    __chave = None

    # precalc tabelas 
    # Realiza a permutação inicial no bloco de entrada (64 bits). Os índices mapeiam os bits de entrada para suas novas posições.
    __ip_tabela = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17,  9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    # PC1 permutacao tabela (Reduz a chave inicial (64 bits) para 56 bits para gerar subchaves.)
    __pc1_tabela = [
        57, 49, 41, 33, 25, 17,  9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15,  7, 62, 54, 46, 38,
        30, 22, 14,  6, 61, 53, 45, 37,
        29, 21, 13,  5, 28, 20, 12,  4
    ]
    # Indica quantas posições cada metade da chave deve ser rotacionada à esquerda em cada um dos 16 rounds.
    __shift_schedule = [1, 1, 2, 2,
                        2, 2, 2, 2,
                        1, 2, 2, 2,
                        2, 2, 2, 1]

    # PC2 permutacao tabela (Usada após os deslocamentos para reduzir cada chave intermediária para 48 bits.) 
    __pc2_tabela = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]
    #expension tabela (Expande os 32 bits do lado direito do bloco para 48 bits para serem usados na função de Feistel.)
    __exp_tabela = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]

    # S-box tabelas for DES (Um conjunto de 8 tabelas de substituição (S-boxes). Cada uma transforma blocos de 6 bits em 4 bits, comprimindo dados.)
    __s_boxes = [
        # S-box 1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        # S-box 2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        # S-box 3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        # S-box 4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        # S-box 5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        # S-box 6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        # S-box 7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        # S-box 8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]
    
    # Permutação aplicada ao resultado da substituição (S-box).
    __permutacao_tabela = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]

    # Permutação final (inversa da permutação inicial).
    __ip_f_inversa_tabela = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]


    # Recebe a chave e processa
    def __init__(self, chave) -> None:
        self.__chave = self.__preprocessar_chave(chave)
         
    
    # Converte cada caractere da string em seu valor binário (8 bits para cada caractere)    
    def __para_binario(self, input) -> str:
        return ''.join(f'{ord(c):08b}' for c in input)


    # Adiciona padding de zeros à direita até atingir o tamanho desejado (64-bits)
    def __add_pad_bits(self, input_bin) -> str:
        if len(input_bin) < 64:
            padded_bits = input_bin.ljust(64, '0')
        return padded_bits    
    

    # Converte a chave de string para binário
    def __preprocessar_chave(self, chave_str):
        chave_bin = self.__para_binario(chave_str)
        # Adiciona padding bits se necessário
        if len(chave_bin) < 64:
            chave_bin = self.__add_pad_bits(chave_bin)
        # Garante que a chave terá 64 bits
        chave_bin = chave_bin[:64]
        return chave_bin
    
    
    # Converte a mensagem para binário 
    def __preprocessar_menssagem(self, menssagem_str):
        menssagem_bin = self.__para_binario(menssagem_str)        
        # Divide a mensagem em blocos de 64 bits
        blocos = [menssagem_bin[i:i+64] for i in range(0, len(menssagem_bin), 64)]
        # Verifica se o último bloco tem menos de 64 bits e adiciona padding se necessário
        if len(blocos[-1]) < 64:
            blocos[-1] = self.__add_pad_bits(blocos[-1])
        return blocos


    # Gerar as subchaves para os 16 rounds
    def __gerar_subchaves(self):
        if self.__chave is None:
            raise ValueError("ERROR: The chave cannot be None")
    
        # PC1 permuta a chave inicial
        permutado_chave = ''.join(self.__chave[i-1] for i in self.__pc1_tabela)
        
        # Divida a chave permutada em duas metades
        c, d = permutado_chave[:28], permutado_chave[28:]
        
        subchaves = []
        for round_num in range(16):
            # Aplicar deslocamento
            c = c[self.__shift_schedule[round_num]:] + c[:self.__shift_schedule[round_num]]
            d = d[self.__shift_schedule[round_num]:] + d[:self.__shift_schedule[round_num]]

            # Aplicar PC2
            cd_concatenado = c + d
            subchave = ''.join(cd_concatenado[i-1] for i in self.__pc2_tabela)
            subchaves.append(subchave)        
        return subchaves
    
    
    # Realiza permutação com base na ip_tabela
    def __permutacao_inicial(self, bloco):      
        permutado_bloco = ''.join(bloco[i-1] for i in self.__ip_tabela)
        return permutado_bloco
    
    # Divide o bloco de 64-bits em duas metades de 32-bits
    def __separar_bloco(self, bloco):
        esquerda_metade = bloco[:32]
        direita_metade = bloco[32:]
        return esquerda_metade, direita_metade
    
    # Expande a metade da direita para 48-bits usando a tabela de expansão
    def __expand_metade(self, metade_bloco):
        expanded_metade = ''.join(metade_bloco[i-1] for i in self.__exp_tabela)
        return expanded_metade
    
    # Divide o bloco em 48-bits em 8 segmentos de 6 bits
    def __substituir(self, bloco):
        substituido = ''
        for i in range(8):
            segment = bloco[i*6:(i+1)*6]
            # Determina a linha usando os bits mais externos (o primeiro e o último)
            linha = int(segment[0] + segment[-1], 2) 
            # Determina usando os 4-bits do meio
            coluna = int(segment[1:5], 2)
            # Substitui o segmento por um valor de 4-bits da S-box correspondente
            substituido += f'{self.__s_boxes[i][linha][coluna]:04b}'
            # Retorna o resultado com 32-bits
        return substituido

    # Feistel
    def __feistel_round(self, esquerda, direita, subchave):
        # Expande a metade direita para 48-bits
        expanded_direita = self.__expand_metade(direita)
        # XOR com a subchave da rodada
        xored = ''.join('1' if expanded_direita[i] != subchave[i] else '0' for i in range(48))
        # Substituição com as S-boxes
        substituido = self.__substituir(xored)
        # Permutação P
        permutado = ''.join(substituido[i-1] for i in self.__permutacao_tabela)
        # XOR com a metade esquerda
        new_direita = ''.join('1' if permutado[i] != esquerda[i] else '0' for i in range(32))
        # Retorna a metade esquerda permutada que será a nova_direita e a direita como esquerda 
        return direita, new_direita
    
    def __inversa_permutacao_inicial(self, bloco):
        permutado_bloco = ''.join(bloco[i-1] for i in self.__ip_f_inversa_tabela)
        return permutado_bloco 
    
    def __bin_to_ascii(self, binary_str):
        ascii_str = ''.join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])
        return ascii_str

    def __bin_to_hex(self, binary_str):
        # Convertendo a string binária para inteiro
        decimal_valor = int(binary_str, 2)
        # Convertendo o inteiro para hexadecimal, removendo o prefixo '0x'
        hex_valor = hex(decimal_valor)[2:]
        # Garantindo que a saída seja em letras minúsculas e sem o prefixo '0x'
        return hex_valor.zfill(len(binary_str) // 4)  # Cada 4 bits são 1 dígito hexadecimal
    
    def __hex_to_bin(self, hex_str):
        # Convertendo a string hexadecimal para inteiro
        decimal_valor = int(hex_str, 16)

        # Convertendo o inteiro para binário, removendo o prefixo '0b'
        bin_valor = bin(decimal_valor)[2:]

        # Garantindo que o número de bits seja múltiplo de 4 (ou seja, 1 dígito hexadecimal = 4 bits)
        return bin_valor.zfill(len(hex_str) * 4)

    def encrypt(self, plaintext):
        # A menssagem de entrada é convertida em blocos de 64-bits
        blocos = self.__preprocessar_menssagem(plaintext)
        subchaves = self.__gerar_subchaves()
        ciphertext = ''
        for bloco in blocos:
            # Permutação inicial
            bloco = self.__permutacao_inicial(bloco)
            # Separa em direita e esquerda
            esquerda, direita = self.__separar_bloco(bloco)
            # Passa pelos 16 rounds de Feistel
            for subchave in subchaves:
                esquerda, direita = self.__feistel_round(esquerda, direita, subchave)
            # Concatena direita e esquerda
            combined_bloco = direita + esquerda
            # Permutação final
            ciphertext += self.__inversa_permutacao_inicial(combined_bloco)
        # COnverte para hexadecimal
        cipherhex = self.__bin_to_hex(ciphertext)      
        return cipherhex

    def decrypt(self, hex):
        # Transforma o hexadecimal para binario 
        blocos = self.__hex_to_bin(hex)
        # Cria um array de blocos de 64bits 
        blocos = [blocos[i:i+64] for i in range(0, len(blocos), 64)]
        # Inverte a ordem da lista de subchaves 
        subchaves = self.__gerar_subchaves()[::-1]
        # Realiza os mesmos passos de encrypt
        decrypted_bin = ''
        for bloco in blocos:
            bloco = self.__permutacao_inicial(bloco)
            esquerda, direita = self.__separar_bloco(bloco)
            for subchave in subchaves:
                esquerda, direita = self.__feistel_round(esquerda, direita, subchave)
            combined_bloco = direita + esquerda
            decrypted_bin += self.__inversa_permutacao_inicial(combined_bloco)
        decrypted_text = self.__bin_to_ascii(decrypted_bin)      
        return decrypted_text
        
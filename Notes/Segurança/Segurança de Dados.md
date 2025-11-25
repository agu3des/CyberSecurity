# Segurança de Dados

Pesquisar IANA e IEEE

- Introdução a Segurança de Dados
    - Exercício 1
        - Qual das opções abaixo descreve corretamente o comportamento de um **worm** em um sistema de rede?
            
            Se replica automaticamente em redes, sem intervenção do usuário
            
        - Qual é a principal característica que diferencia um **Trojan** de um **vírus**?
            
            Trojans se disfarçam como software legítimo, sem se replicarem.
            
        - Qual tipo de malware é conhecido por criptografar os arquivos do sistema e exigir um pagamento de resgate em troca da chave de descriptografia?
            
            Ransonware
            
        - Qual medida seria mais adequada para melhorar a disponibilidade em uma rede de computadores?
            
            Utilizar backups regulares e sistemas redundantes.
            
        - Qual das alternativas a seguir descreve corretamente uma vulnerabilidade no contexto de segurança da informação?
            
            Uma fraqueza ou falha em um sistema que pode ser explorada por ameaças.
            
        - Qual das opções caracteriza um script kiddie e diferencia esse tipo de atacante de hackers mais experientes?
            
            Script kiddies utilizam ferramentas prontas e scripts desenvolvidos por outros, sem profundo conhecimento técnico ou de programação.
            
        - Em um ataque de escalada de privilégios, qual é o objetivo principal do atacante?
            
            Obter permissões e acessos maiores do que os inicialmente autorizados.
            
        - Em uma análise de risco, quais fatores são normalmente considerados para calcular o nível de risco?
            
            Probabilidade de ocorrência e impacto da ameaça
            
- Hash
    
    colisão - duas entradas diferentes resultam na mesma saída
    
    **Características desejáveis:** 
    
    - probabilidade[colisão] → 0
    - viabilidade computacional: barato computar o hash y=H(x)
    - pré-image resistance: sabendo apenas o resultado é difícil e por vezes impossível encontrar sua entrada
    - collision resistence: é difícil encontrar duas entradas diferentes e com o mesmo hash
    - a saída deve ter tamanho fixo
    - a hash não pode ser two-way function
    - não-injetividade, não-sobrejetividade e impossibilidade de reversão direta
    
    **Verificação de integridade de uma mensagem M**
    
    calcule h¹ = H(M) → guarde h¹ → calcule h² = H(M) → Se h¹ **≠ h² →** M alterada
    
    **Armazenamento de senha**
    
    guarde h¹ = H(S) → na autenticação solicite senha Su do usuário → calcule h² = (Su) → h¹ = h² → S = Su
    
    **Calcular Hash**
    
    Pra entrar na função tem que ser múltiplo de 512, se não tiver a quantidade necessária faz-se o enchimento para poder calcular o hash
    
    Consome o arquivo em blocos e reutiliza partes que ele já usou
    
    Método salt do linux: entrada (senha original) + salt (número aleatório gerado durante a criação da senha)  → algoritmo de hash → hash
    
- MD5
    - Código
        
        ```python
        import struct
        import math
        
        class MD5:
            def __init__(self):
                # Tabela de senhas iniciais baseadas na raiz cúbica de números primos
                self._s = [
                    (7, 12, 17, 22), (5, 9, 14, 20),
                    (4, 11, 16, 23), (6, 10, 15, 21)
                ]
                self._k = [int((2**32) * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]
                self._buffers = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]
                self._original_len = 0
                self._buffer = b""
        
            def _left_rotate(self, x, c):
                return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF
        
            def update(self, input_bytes):
                self._buffer += input_bytes
                self._original_len += len(input_bytes) * 8
        
                while len(self._buffer) >= 64:
                    self._process_chunk(self._buffer[:64])
                    self._buffer = self._buffer[64:]
        
            def _process_chunk(self, chunk):
                a, b, c, d = self._buffers
                x = list(struct.unpack("<16I", chunk))
        
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
        
                self._buffers = [
                    (self._buffers[0] + a) & 0xFFFFFFFF,
                    (self._buffers[1] + b) & 0xFFFFFFFF,
                    (self._buffers[2] + c) & 0xFFFFFFFF,
                    (self._buffers[3] + d) & 0xFFFFFFFF,
                ]
        
            def digest(self):
                padding = b"\x80" + b"\x00" * ((56 - (len(self._buffer) + 1) % 64) % 64)
                length = struct.pack("<Q", self._original_len)
                self.update(padding + length)
        
                return struct.pack("<4I", *self._buffers)
        
            def hexdigest(self):
                return "".join(f"{byte:02x}" for byte in self.digest())
        
        # Uso:
        data = b"Hello World"
        md5 = MD5()
        md5.update(data)
        print(md5.hexdigest())
        
        '''
        
        import hashlib
        
        text = "Hello World"
        text2 = input()
        
        hash_object = hashlib.md5(text.encode())
        hash_object2 = hashlib.md5(text2.encode())
        
        print(hash_object.hexdigest())
        print(hash_object2.hexdigest())
        '''
        ```
        
    - IETF - MD5
        
        ```
        Network Working Group                                          R. Rivest
        Request for Comments: 1321           MIT Laboratory for Computer Science
                                                     and RSA Data Security, Inc.
                                                                      April 1992
        
                             The MD5 Message-Digest Algorithm
        
        Status of this Memo
        
           This memo provides information for the Internet community.  It does
           not specify an Internet standard.  Distribution of this memo is
           unlimited.
        
        Acknowlegements
        
           We would like to thank Don Coppersmith, Burt Kaliski, Ralph Merkle,
           David Chaum, and Noam Nisan for numerous helpful comments and
           suggestions.
        
        Table of Contents
        
           1. Executive Summary                                                1
           2. Terminology and Notation                                         2
           3. MD5 Algorithm Description                                        3
           4. Summary                                                          6
           5. Differences Between MD4 and MD5                                  6
           References                                                          7
           APPENDIX A - Reference Implementation                               7
           Security Considerations                                            21
           Author's Address                                                   21
        
        1. Executive Summary
        
           This document describes the MD5 message-digest algorithm. The
           algorithm takes as input a message of arbitrary length and produces
           as output a 128-bit "fingerprint" or "message digest" of the input.
           It is conjectured that it is computationally infeasible to produce
           two messages having the same message digest, or to produce any
           message having a given prespecified target message digest. The MD5
           algorithm is intended for digital signature applications, where a
           large file must be "compressed" in a secure manner before being
           encrypted with a private (secret) key under a public-key cryptosystem
           such as RSA.
        
        Rivest                                                          [Page 1]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
           The MD5 algorithm is designed to be quite fast on 32-bit machines. In
           addition, the MD5 algorithm does not require any large substitution
           tables; the algorithm can be coded quite compactly.
        
           The MD5 algorithm is an extension of the MD4 message-digest algorithm
           1,2]. MD5 is slightly slower than MD4, but is more "conservative" in
           design. MD5 was designed because it was felt that MD4 was perhaps
           being adopted for use more quickly than justified by the existing
           critical review; because MD4 was designed to be exceptionally fast,
           it is "at the edge" in terms of risking successful cryptanalytic
           attack. MD5 backs off a bit, giving up a little in speed for a much
           greater likelihood of ultimate security. It incorporates some
           suggestions made by various reviewers, and contains additional
           optimizations. The MD5 algorithm is being placed in the public domain
           for review and possible adoption as a standard.
        
           For OSI-based applications, MD5's object identifier is
        
           md5 OBJECT IDENTIFIER ::=
             iso(1) member-body(2) US(840) rsadsi(113549) digestAlgorithm(2) 5}
        
           In the X.509 type AlgorithmIdentifier [3], the parameters for MD5
           should have type NULL.
        
        2. Terminology and Notation
        
           In this document a "word" is a 32-bit quantity and a "byte" is an
           eight-bit quantity. A sequence of bits can be interpreted in a
           natural manner as a sequence of bytes, where each consecutive group
           of eight bits is interpreted as a byte with the high-order (most
           significant) bit of each byte listed first. Similarly, a sequence of
           bytes can be interpreted as a sequence of 32-bit words, where each
           consecutive group of four bytes is interpreted as a word with the
           low-order (least significant) byte given first.
        
           Let x_i denote "x sub i". If the subscript is an expression, we
           surround it in braces, as in x_{i+1}. Similarly, we use ^ for
           superscripts (exponentiation), so that x^i denotes x to the i-th
           power.
        
           Let the symbol "+" denote addition of words (i.e., modulo-2^32
           addition). Let X <<< s denote the 32-bit value obtained by circularly
           shifting (rotating) X left by s bit positions. Let not(X) denote the
           bit-wise complement of X, and let X v Y denote the bit-wise OR of X
           and Y. Let X xor Y denote the bit-wise XOR of X and Y, and let XY
           denote the bit-wise AND of X and Y.
        
        Rivest                                                          [Page 2]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
        3. MD5 Algorithm Description
        
           We begin by supposing that we have a b-bit message as input, and that
           we wish to find its message digest. Here b is an arbitrary
           nonnegative integer; b may be zero, it need not be a multiple of
           eight, and it may be arbitrarily large. We imagine the bits of the
           message written down as follows:
        
                  m_0 m_1 ... m_{b-1}
        
           The following five steps are performed to compute the message digest
           of the message.
        
        3.1 Step 1. Append Padding Bits
        
           The message is "padded" (extended) so that its length (in bits) is
           congruent to 448, modulo 512. That is, the message is extended so
           that it is just 64 bits shy of being a multiple of 512 bits long.
           Padding is always performed, even if the length of the message is
           already congruent to 448, modulo 512.
        
           Padding is performed as follows: a single "1" bit is appended to the
           message, and then "0" bits are appended so that the length in bits of
           the padded message becomes congruent to 448, modulo 512. In all, at
           least one bit and at most 512 bits are appended.
        
        3.2 Step 2. Append Length
        
           A 64-bit representation of b (the length of the message before the
           padding bits were added) is appended to the result of the previous
           step. In the unlikely event that b is greater than 2^64, then only
           the low-order 64 bits of b are used. (These bits are appended as two
           32-bit words and appended low-order word first in accordance with the
           previous conventions.)
        
           At this point the resulting message (after padding with bits and with
           b) has a length that is an exact multiple of 512 bits. Equivalently,
           this message has a length that is an exact multiple of 16 (32-bit)
           words. Let M[0 ... N-1] denote the words of the resulting message,
           where N is a multiple of 16.
        
        3.3 Step 3. Initialize MD Buffer
        
           A four-word buffer (A,B,C,D) is used to compute the message digest.
           Here each of A, B, C, D is a 32-bit register. These registers are
           initialized to the following values in hexadecimal, low-order bytes
           first):
        
        Rivest                                                          [Page 3]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
                  word A: 01 23 45 67
                  word B: 89 ab cd ef
                  word C: fe dc ba 98
                  word D: 76 54 32 10
        
        3.4 Step 4. Process Message in 16-Word Blocks
        
           We first define four auxiliary functions that each take as input
           three 32-bit words and produce as output one 32-bit word.
        
                  F(X,Y,Z) = XY v not(X) Z
                  G(X,Y,Z) = XZ v Y not(Z)
                  H(X,Y,Z) = X xor Y xor Z
                  I(X,Y,Z) = Y xor (X v not(Z))
        
           In each bit position F acts as a conditional: if X then Y else Z.
           The function F could have been defined using + instead of v since XY
           and not(X)Z will never have 1's in the same bit position.) It is
           interesting to note that if the bits of X, Y, and Z are independent
           and unbiased, the each bit of F(X,Y,Z) will be independent and
           unbiased.
        
           The functions G, H, and I are similar to the function F, in that they
           act in "bitwise parallel" to produce their output from the bits of X,
           Y, and Z, in such a manner that if the corresponding bits of X, Y,
           and Z are independent and unbiased, then each bit of G(X,Y,Z),
           H(X,Y,Z), and I(X,Y,Z) will be independent and unbiased. Note that
           the function H is the bit-wise "xor" or "parity" function of its
           inputs.
        
           This step uses a 64-element table T[1 ... 64] constructed from the
           sine function. Let T[i] denote the i-th element of the table, which
           is equal to the integer part of 4294967296 times abs(sin(i)), where i
           is in radians. The elements of the table are given in the appendix.
        
           Do the following:
        
           /* Process each 16-word block. */
           For i = 0 to N/16-1 do
        
             /* Copy block i into X. */
             For j = 0 to 15 do
               Set X[j] to M[i*16+j].
             end /* of loop on j */
        
             /* Save A as AA, B as BB, C as CC, and D as DD. */
             AA = A
             BB = B
        
        Rivest                                                          [Page 4]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
             CC = C
             DD = D
        
             /* Round 1. */
             /* Let [abcd k s i] denote the operation
                  a = b + ((a + F(b,c,d) + X[k] + T[i]) <<< s). */
             /* Do the following 16 operations. */
             [ABCD  0  7  1]  [DABC  1 12  2]  [CDAB  2 17  3]  [BCDA  3 22  4]
             [ABCD  4  7  5]  [DABC  5 12  6]  [CDAB  6 17  7]  [BCDA  7 22  8]
             [ABCD  8  7  9]  [DABC  9 12 10]  [CDAB 10 17 11]  [BCDA 11 22 12]
             [ABCD 12  7 13]  [DABC 13 12 14]  [CDAB 14 17 15]  [BCDA 15 22 16]
        
             /* Round 2. */
             /* Let [abcd k s i] denote the operation
                  a = b + ((a + G(b,c,d) + X[k] + T[i]) <<< s). */
             /* Do the following 16 operations. */
             [ABCD  1  5 17]  [DABC  6  9 18]  [CDAB 11 14 19]  [BCDA  0 20 20]
             [ABCD  5  5 21]  [DABC 10  9 22]  [CDAB 15 14 23]  [BCDA  4 20 24]
             [ABCD  9  5 25]  [DABC 14  9 26]  [CDAB  3 14 27]  [BCDA  8 20 28]
             [ABCD 13  5 29]  [DABC  2  9 30]  [CDAB  7 14 31]  [BCDA 12 20 32]
        
             /* Round 3. */
             /* Let [abcd k s t] denote the operation
                  a = b + ((a + H(b,c,d) + X[k] + T[i]) <<< s). */
             /* Do the following 16 operations. */
             [ABCD  5  4 33]  [DABC  8 11 34]  [CDAB 11 16 35]  [BCDA 14 23 36]
             [ABCD  1  4 37]  [DABC  4 11 38]  [CDAB  7 16 39]  [BCDA 10 23 40]
             [ABCD 13  4 41]  [DABC  0 11 42]  [CDAB  3 16 43]  [BCDA  6 23 44]
             [ABCD  9  4 45]  [DABC 12 11 46]  [CDAB 15 16 47]  [BCDA  2 23 48]
        
             /* Round 4. */
             /* Let [abcd k s t] denote the operation
                  a = b + ((a + I(b,c,d) + X[k] + T[i]) <<< s). */
             /* Do the following 16 operations. */
             [ABCD  0  6 49]  [DABC  7 10 50]  [CDAB 14 15 51]  [BCDA  5 21 52]
             [ABCD 12  6 53]  [DABC  3 10 54]  [CDAB 10 15 55]  [BCDA  1 21 56]
             [ABCD  8  6 57]  [DABC 15 10 58]  [CDAB  6 15 59]  [BCDA 13 21 60]
             [ABCD  4  6 61]  [DABC 11 10 62]  [CDAB  2 15 63]  [BCDA  9 21 64]
        
             /* Then perform the following additions. (That is increment each
                of the four registers by the value it had before this block
                was started.) */
             A = A + AA
             B = B + BB
             C = C + CC
             D = D + DD
        
           end /* of loop on i */
        
        Rivest                                                          [Page 5]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
        3.5 Step 5. Output
        
           The message digest produced as output is A, B, C, D. That is, we
           begin with the low-order byte of A, and end with the high-order byte
           of D.
        
           This completes the description of MD5. A reference implementation in
           C is given in the appendix.
        
        4. Summary
        
           The MD5 message-digest algorithm is simple to implement, and provides
           a "fingerprint" or message digest of a message of arbitrary length.
           It is conjectured that the difficulty of coming up with two messages
           having the same message digest is on the order of 2^64 operations,
           and that the difficulty of coming up with any message having a given
           message digest is on the order of 2^128 operations. The MD5 algorithm
           has been carefully scrutinized for weaknesses. It is, however, a
           relatively new algorithm and further security analysis is of course
           justified, as is the case with any new proposal of this sort.
        
        5. Differences Between MD4 and MD5
        
             The following are the differences between MD4 and MD5:
        
               1.   A fourth round has been added.
        
               2.   Each step now has a unique additive constant.
        
               3.   The function g in round 2 was changed from (XY v XZ v YZ) to
               (XZ v Y not(Z)) to make g less symmetric.
        
               4.   Each step now adds in the result of the previous step.  This
               promotes a faster "avalanche effect".
        
               5.   The order in which input words are accessed in rounds 2 and
               3 is changed, to make these patterns less like each other.
        
               6.   The shift amounts in each round have been approximately
               optimized, to yield a faster "avalanche effect." The shifts in
               different rounds are distinct.
        
        Rivest                                                          [Page 6]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
        References
        
           [1] Rivest, R., "The MD4 Message Digest Algorithm", RFC 1320, MIT and
               RSA Data Security, Inc., April 1992.
        
           [2] Rivest, R., "The MD4 message digest algorithm", in A.J.  Menezes
               and S.A. Vanstone, editors, Advances in Cryptology - CRYPTO '90
               Proceedings, pages 303-311, Springer-Verlag, 1991.
        
           [3] CCITT Recommendation X.509 (1988), "The Directory -
               Authentication Framework."
        
        APPENDIX A - Reference Implementation
        
           This appendix contains the following files taken from RSAREF: A
           Cryptographic Toolkit for Privacy-Enhanced Mail:
        
             global.h -- global header file
        
             md5.h -- header file for MD5
        
             md5c.c -- source code for MD5
        
           For more information on RSAREF, send email to <rsaref@rsa.com>.
        
           The appendix also includes the following file:
        
             mddriver.c -- test driver for MD2, MD4 and MD5
        
           The driver compiles for MD5 by default but can compile for MD2 or MD4
           if the symbol MD is defined on the C compiler command line as 2 or 4.
        
           The implementation is portable and should work on many different
           plaforms. However, it is not difficult to optimize the implementation
           on particular platforms, an exercise left to the reader. For example,
           on "little-endian" platforms where the lowest-addressed byte in a 32-
           bit word is the least significant and there are no alignment
           restrictions, the call to Decode in MD5Transform can be replaced with
           a typecast.
        
        A.1 global.h
        
        /* GLOBAL.H - RSAREF types and constants
         */
        
        /* PROTOTYPES should be set to one if and only if the compiler supports
          function argument prototyping.
        The following makes PROTOTYPES default to 0 if it has not already
        
        Rivest                                                          [Page 7]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
          been defined with C compiler flags.
         */
        #ifndef PROTOTYPES
        #define PROTOTYPES 0
        #endif
        
        /* POINTER defines a generic pointer type */
        typedef unsigned char *POINTER;
        
        /* UINT2 defines a two byte word */
        typedef unsigned short int UINT2;
        
        /* UINT4 defines a four byte word */
        typedef unsigned long int UINT4;
        
        /* PROTO_LIST is defined depending on how PROTOTYPES is defined above.
        If using PROTOTYPES, then PROTO_LIST returns the list, otherwise it
          returns an empty list.
         */
        #if PROTOTYPES
        #define PROTO_LIST(list) list
        #else
        #define PROTO_LIST(list) ()
        #endif
        
        A.2 md5.h
        
        /* MD5.H - header file for MD5C.C
         */
        
        /* Copyright (C) 1991-2, RSA Data Security, Inc. Created 1991. All
        rights reserved.
        
        License to copy and use this software is granted provided that it
        is identified as the "RSA Data Security, Inc. MD5 Message-Digest
        Algorithm" in all material mentioning or referencing this software
        or this function.
        
        License is also granted to make and use derivative works provided
        that such works are identified as "derived from the RSA Data
        Security, Inc. MD5 Message-Digest Algorithm" in all material
        mentioning or referencing the derived work.
        
        RSA Data Security, Inc. makes no representations concerning either
        the merchantability of this software or the suitability of this
        software for any particular purpose. It is provided "as is"
        without express or implied warranty of any kind.
        
        Rivest                                                          [Page 8]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
        These notices must be retained in any copies of any part of this
        documentation and/or software.
         */
        
        /* MD5 context. */
        typedef struct {
          UINT4 state[4];                                   /* state (ABCD) */
          UINT4 count[2];        /* number of bits, modulo 2^64 (lsb first) */
          unsigned char buffer[64];                         /* input buffer */
        } MD5_CTX;
        
        void MD5Init PROTO_LIST ((MD5_CTX *));
        void MD5Update PROTO_LIST
          ((MD5_CTX *, unsigned char *, unsigned int));
        void MD5Final PROTO_LIST ((unsigned char [16], MD5_CTX *));
        
        A.3 md5c.c
        
        /* MD5C.C - RSA Data Security, Inc., MD5 message-digest algorithm
         */
        
        /* Copyright (C) 1991-2, RSA Data Security, Inc. Created 1991. All
        rights reserved.
        
        License to copy and use this software is granted provided that it
        is identified as the "RSA Data Security, Inc. MD5 Message-Digest
        Algorithm" in all material mentioning or referencing this software
        or this function.
        
        License is also granted to make and use derivative works provided
        that such works are identified as "derived from the RSA Data
        Security, Inc. MD5 Message-Digest Algorithm" in all material
        mentioning or referencing the derived work.
        
        RSA Data Security, Inc. makes no representations concerning either
        the merchantability of this software or the suitability of this
        software for any particular purpose. It is provided "as is"
        without express or implied warranty of any kind.
        
        These notices must be retained in any copies of any part of this
        documentation and/or software.
         */
        
        #include "global.h"
        #include "md5.h"
        
        /* Constants for MD5Transform routine.
         */
        
        Rivest                                                          [Page 9]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
        #define S11 7
        #define S12 12
        #define S13 17
        #define S14 22
        #define S21 5
        #define S22 9
        #define S23 14
        #define S24 20
        #define S31 4
        #define S32 11
        #define S33 16
        #define S34 23
        #define S41 6
        #define S42 10
        #define S43 15
        #define S44 21
        
        static void MD5Transform PROTO_LIST ((UINT4 [4], unsigned char [64]));
        static void Encode PROTO_LIST
          ((unsigned char *, UINT4 *, unsigned int));
        static void Decode PROTO_LIST
          ((UINT4 *, unsigned char *, unsigned int));
        static void MD5_memcpy PROTO_LIST ((POINTER, POINTER, unsigned int));
        static void MD5_memset PROTO_LIST ((POINTER, int, unsigned int));
        
        static unsigned char PADDING[64] = {
          0x80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        };
        
        /* F, G, H and I are basic MD5 functions.
         */
        #define F(x, y, z) (((x) & (y)) | ((~x) & (z)))
        #define G(x, y, z) (((x) & (z)) | ((y) & (~z)))
        #define H(x, y, z) ((x) ^ (y) ^ (z))
        #define I(x, y, z) ((y) ^ ((x) | (~z)))
        
        /* ROTATE_LEFT rotates x left n bits.
         */
        #define ROTATE_LEFT(x, n) (((x) << (n)) | ((x) >> (32-(n))))
        
        /* FF, GG, HH, and II transformations for rounds 1, 2, 3, and 4.
        Rotation is separate from addition to prevent recomputation.
         */
        #define FF(a, b, c, d, x, s, ac) { \
         (a) += F ((b), (c), (d)) + (x) + (UINT4)(ac); \
         (a) = ROTATE_LEFT ((a), (s)); \
        
        Rivest                                                         [Page 10]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
         (a) += (b); \
          }
        #define GG(a, b, c, d, x, s, ac) { \
         (a) += G ((b), (c), (d)) + (x) + (UINT4)(ac); \
         (a) = ROTATE_LEFT ((a), (s)); \
         (a) += (b); \
          }
        #define HH(a, b, c, d, x, s, ac) { \
         (a) += H ((b), (c), (d)) + (x) + (UINT4)(ac); \
         (a) = ROTATE_LEFT ((a), (s)); \
         (a) += (b); \
          }
        #define II(a, b, c, d, x, s, ac) { \
         (a) += I ((b), (c), (d)) + (x) + (UINT4)(ac); \
         (a) = ROTATE_LEFT ((a), (s)); \
         (a) += (b); \
          }
        
        /* MD5 initialization. Begins an MD5 operation, writing a new context.
         */
        void MD5Init (context)
        MD5_CTX *context;                                        /* context */
        {
          context->count[0] = context->count[1] = 0;
          /* Load magic initialization constants.
        */
          context->state[0] = 0x67452301;
          context->state[1] = 0xefcdab89;
          context->state[2] = 0x98badcfe;
          context->state[3] = 0x10325476;
        }
        
        /* MD5 block update operation. Continues an MD5 message-digest
          operation, processing another message block, and updating the
          context.
         */
        void MD5Update (context, input, inputLen)
        MD5_CTX *context;                                        /* context */
        unsigned char *input;                                /* input block */
        unsigned int inputLen;                     /* length of input block */
        {
          unsigned int i, index, partLen;
        
          /* Compute number of bytes mod 64 */
          index = (unsigned int)((context->count[0] >> 3) & 0x3F);
        
          /* Update number of bits */
          if ((context->count[0] += ((UINT4)inputLen << 3))
        
        Rivest                                                         [Page 11]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
           < ((UINT4)inputLen << 3))
         context->count[1]++;
          context->count[1] += ((UINT4)inputLen >> 29);
        
          partLen = 64 - index;
        
          /* Transform as many times as possible.
        */
          if (inputLen >= partLen) {
         MD5_memcpy
           ((POINTER)&context->buffer[index], (POINTER)input, partLen);
         MD5Transform (context->state, context->buffer);
        
         for (i = partLen; i + 63 < inputLen; i += 64)
           MD5Transform (context->state, &input[i]);
        
         index = 0;
          }
          else
         i = 0;
        
          /* Buffer remaining input */
          MD5_memcpy
         ((POINTER)&context->buffer[index], (POINTER)&input[i],
          inputLen-i);
        }
        
        /* MD5 finalization. Ends an MD5 message-digest operation, writing the
          the message digest and zeroizing the context.
         */
        void MD5Final (digest, context)
        unsigned char digest[16];                         /* message digest */
        MD5_CTX *context;                                       /* context */
        {
          unsigned char bits[8];
          unsigned int index, padLen;
        
          /* Save number of bits */
          Encode (bits, context->count, 8);
        
          /* Pad out to 56 mod 64.
        */
          index = (unsigned int)((context->count[0] >> 3) & 0x3f);
          padLen = (index < 56) ? (56 - index) : (120 - index);
          MD5Update (context, PADDING, padLen);
        
          /* Append length (before padding) */
          MD5Update (context, bits, 8);
        
        Rivest                                                         [Page 12]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
          /* Store state in digest */
          Encode (digest, context->state, 16);
        
          /* Zeroize sensitive information.
        */
          MD5_memset ((POINTER)context, 0, sizeof (*context));
        }
        
        /* MD5 basic transformation. Transforms state based on block.
         */
        static void MD5Transform (state, block)
        UINT4 state[4];
        unsigned char block[64];
        {
          UINT4 a = state[0], b = state[1], c = state[2], d = state[3], x[16];
        
          Decode (x, block, 64);
        
          /* Round 1 */
          FF (a, b, c, d, x[ 0], S11, 0xd76aa478); /* 1 */
          FF (d, a, b, c, x[ 1], S12, 0xe8c7b756); /* 2 */
          FF (c, d, a, b, x[ 2], S13, 0x242070db); /* 3 */
          FF (b, c, d, a, x[ 3], S14, 0xc1bdceee); /* 4 */
          FF (a, b, c, d, x[ 4], S11, 0xf57c0faf); /* 5 */
          FF (d, a, b, c, x[ 5], S12, 0x4787c62a); /* 6 */
          FF (c, d, a, b, x[ 6], S13, 0xa8304613); /* 7 */
          FF (b, c, d, a, x[ 7], S14, 0xfd469501); /* 8 */
          FF (a, b, c, d, x[ 8], S11, 0x698098d8); /* 9 */
          FF (d, a, b, c, x[ 9], S12, 0x8b44f7af); /* 10 */
          FF (c, d, a, b, x[10], S13, 0xffff5bb1); /* 11 */
          FF (b, c, d, a, x[11], S14, 0x895cd7be); /* 12 */
          FF (a, b, c, d, x[12], S11, 0x6b901122); /* 13 */
          FF (d, a, b, c, x[13], S12, 0xfd987193); /* 14 */
          FF (c, d, a, b, x[14], S13, 0xa679438e); /* 15 */
          FF (b, c, d, a, x[15], S14, 0x49b40821); /* 16 */
        
         /* Round 2 */
          GG (a, b, c, d, x[ 1], S21, 0xf61e2562); /* 17 */
          GG (d, a, b, c, x[ 6], S22, 0xc040b340); /* 18 */
          GG (c, d, a, b, x[11], S23, 0x265e5a51); /* 19 */
          GG (b, c, d, a, x[ 0], S24, 0xe9b6c7aa); /* 20 */
          GG (a, b, c, d, x[ 5], S21, 0xd62f105d); /* 21 */
          GG (d, a, b, c, x[10], S22,  0x2441453); /* 22 */
          GG (c, d, a, b, x[15], S23, 0xd8a1e681); /* 23 */
          GG (b, c, d, a, x[ 4], S24, 0xe7d3fbc8); /* 24 */
          GG (a, b, c, d, x[ 9], S21, 0x21e1cde6); /* 25 */
          GG (d, a, b, c, x[14], S22, 0xc33707d6); /* 26 */
          GG (c, d, a, b, x[ 3], S23, 0xf4d50d87); /* 27 */
        
        Rivest                                                         [Page 13]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
          GG (b, c, d, a, x[ 8], S24, 0x455a14ed); /* 28 */
          GG (a, b, c, d, x[13], S21, 0xa9e3e905); /* 29 */
          GG (d, a, b, c, x[ 2], S22, 0xfcefa3f8); /* 30 */
          GG (c, d, a, b, x[ 7], S23, 0x676f02d9); /* 31 */
          GG (b, c, d, a, x[12], S24, 0x8d2a4c8a); /* 32 */
        
          /* Round 3 */
          HH (a, b, c, d, x[ 5], S31, 0xfffa3942); /* 33 */
          HH (d, a, b, c, x[ 8], S32, 0x8771f681); /* 34 */
          HH (c, d, a, b, x[11], S33, 0x6d9d6122); /* 35 */
          HH (b, c, d, a, x[14], S34, 0xfde5380c); /* 36 */
          HH (a, b, c, d, x[ 1], S31, 0xa4beea44); /* 37 */
          HH (d, a, b, c, x[ 4], S32, 0x4bdecfa9); /* 38 */
          HH (c, d, a, b, x[ 7], S33, 0xf6bb4b60); /* 39 */
          HH (b, c, d, a, x[10], S34, 0xbebfbc70); /* 40 */
          HH (a, b, c, d, x[13], S31, 0x289b7ec6); /* 41 */
          HH (d, a, b, c, x[ 0], S32, 0xeaa127fa); /* 42 */
          HH (c, d, a, b, x[ 3], S33, 0xd4ef3085); /* 43 */
          HH (b, c, d, a, x[ 6], S34,  0x4881d05); /* 44 */
          HH (a, b, c, d, x[ 9], S31, 0xd9d4d039); /* 45 */
          HH (d, a, b, c, x[12], S32, 0xe6db99e5); /* 46 */
          HH (c, d, a, b, x[15], S33, 0x1fa27cf8); /* 47 */
          HH (b, c, d, a, x[ 2], S34, 0xc4ac5665); /* 48 */
        
          /* Round 4 */
          II (a, b, c, d, x[ 0], S41, 0xf4292244); /* 49 */
          II (d, a, b, c, x[ 7], S42, 0x432aff97); /* 50 */
          II (c, d, a, b, x[14], S43, 0xab9423a7); /* 51 */
          II (b, c, d, a, x[ 5], S44, 0xfc93a039); /* 52 */
          II (a, b, c, d, x[12], S41, 0x655b59c3); /* 53 */
          II (d, a, b, c, x[ 3], S42, 0x8f0ccc92); /* 54 */
          II (c, d, a, b, x[10], S43, 0xffeff47d); /* 55 */
          II (b, c, d, a, x[ 1], S44, 0x85845dd1); /* 56 */
          II (a, b, c, d, x[ 8], S41, 0x6fa87e4f); /* 57 */
          II (d, a, b, c, x[15], S42, 0xfe2ce6e0); /* 58 */
          II (c, d, a, b, x[ 6], S43, 0xa3014314); /* 59 */
          II (b, c, d, a, x[13], S44, 0x4e0811a1); /* 60 */
          II (a, b, c, d, x[ 4], S41, 0xf7537e82); /* 61 */
          II (d, a, b, c, x[11], S42, 0xbd3af235); /* 62 */
          II (c, d, a, b, x[ 2], S43, 0x2ad7d2bb); /* 63 */
          II (b, c, d, a, x[ 9], S44, 0xeb86d391); /* 64 */
        
          state[0] += a;
          state[1] += b;
          state[2] += c;
          state[3] += d;
        
          /* Zeroize sensitive information.
        
        Rivest                                                         [Page 14]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
        */
          MD5_memset ((POINTER)x, 0, sizeof (x));
        }
        
        /* Encodes input (UINT4) into output (unsigned char). Assumes len is
          a multiple of 4.
         */
        static void Encode (output, input, len)
        unsigned char *output;
        UINT4 *input;
        unsigned int len;
        {
          unsigned int i, j;
        
          for (i = 0, j = 0; j < len; i++, j += 4) {
         output[j] = (unsigned char)(input[i] & 0xff);
         output[j+1] = (unsigned char)((input[i] >> 8) & 0xff);
         output[j+2] = (unsigned char)((input[i] >> 16) & 0xff);
         output[j+3] = (unsigned char)((input[i] >> 24) & 0xff);
          }
        }
        
        /* Decodes input (unsigned char) into output (UINT4). Assumes len is
          a multiple of 4.
         */
        static void Decode (output, input, len)
        UINT4 *output;
        unsigned char *input;
        unsigned int len;
        {
          unsigned int i, j;
        
          for (i = 0, j = 0; j < len; i++, j += 4)
         output[i] = ((UINT4)input[j]) | (((UINT4)input[j+1]) << 8) |
           (((UINT4)input[j+2]) << 16) | (((UINT4)input[j+3]) << 24);
        }
        
        /* Note: Replace "for loop" with standard memcpy if possible.
         */
        
        static void MD5_memcpy (output, input, len)
        POINTER output;
        POINTER input;
        unsigned int len;
        {
          unsigned int i;
        
          for (i = 0; i < len; i++)
        
        Rivest                                                         [Page 15]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
         output[i] = input[i];
        }
        
        /* Note: Replace "for loop" with standard memset if possible.
         */
        static void MD5_memset (output, value, len)
        POINTER output;
        int value;
        unsigned int len;
        {
          unsigned int i;
        
          for (i = 0; i < len; i++)
         ((char *)output)[i] = (char)value;
        }
        
        A.4 mddriver.c
        
        /* MDDRIVER.C - test driver for MD2, MD4 and MD5
         */
        
        /* Copyright (C) 1990-2, RSA Data Security, Inc. Created 1990. All
        rights reserved.
        
        RSA Data Security, Inc. makes no representations concerning either
        the merchantability of this software or the suitability of this
        software for any particular purpose. It is provided "as is"
        without express or implied warranty of any kind.
        
        These notices must be retained in any copies of any part of this
        documentation and/or software.
         */
        
        /* The following makes MD default to MD5 if it has not already been
          defined with C compiler flags.
         */
        #ifndef MD
        #define MD MD5
        #endif
        
        #include <stdio.h>
        #include <time.h>
        #include <string.h>
        #include "global.h"
        #if MD == 2
        #include "md2.h"
        #endif
        #if MD == 4
        
        Rivest                                                         [Page 16]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
        #include "md4.h"
        #endif
        #if MD == 5
        #include "md5.h"
        #endif
        
        /* Length of test block, number of test blocks.
         */
        #define TEST_BLOCK_LEN 1000
        #define TEST_BLOCK_COUNT 1000
        
        static void MDString PROTO_LIST ((char *));
        static void MDTimeTrial PROTO_LIST ((void));
        static void MDTestSuite PROTO_LIST ((void));
        static void MDFile PROTO_LIST ((char *));
        static void MDFilter PROTO_LIST ((void));
        static void MDPrint PROTO_LIST ((unsigned char [16]));
        
        #if MD == 2
        #define MD_CTX MD2_CTX
        #define MDInit MD2Init
        #define MDUpdate MD2Update
        #define MDFinal MD2Final
        #endif
        #if MD == 4
        #define MD_CTX MD4_CTX
        #define MDInit MD4Init
        #define MDUpdate MD4Update
        #define MDFinal MD4Final
        #endif
        #if MD == 5
        #define MD_CTX MD5_CTX
        #define MDInit MD5Init
        #define MDUpdate MD5Update
        #define MDFinal MD5Final
        #endif
        
        /* Main driver.
        
        Arguments (may be any combination):
          -sstring - digests string
          -t       - runs time trial
          -x       - runs test script
          filename - digests file
          (none)   - digests standard input
         */
        int main (argc, argv)
        int argc;
        
        Rivest                                                         [Page 17]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
        char *argv[];
        {
          int i;
        
          if (argc > 1)
         for (i = 1; i < argc; i++)
           if (argv[i][0] == '-' && argv[i][1] == 's')
             MDString (argv[i] + 2);
           else if (strcmp (argv[i], "-t") == 0)
             MDTimeTrial ();
           else if (strcmp (argv[i], "-x") == 0)
             MDTestSuite ();
           else
             MDFile (argv[i]);
          else
         MDFilter ();
        
          return (0);
        }
        
        /* Digests a string and prints the result.
         */
        static void MDString (string)
        char *string;
        {
          MD_CTX context;
          unsigned char digest[16];
          unsigned int len = strlen (string);
        
          MDInit (&context);
          MDUpdate (&context, string, len);
          MDFinal (digest, &context);
        
          printf ("MD%d (\"%s\") = ", MD, string);
          MDPrint (digest);
          printf ("\n");
        }
        
        /* Measures the time to digest TEST_BLOCK_COUNT TEST_BLOCK_LEN-byte
          blocks.
         */
        static void MDTimeTrial ()
        {
          MD_CTX context;
          time_t endTime, startTime;
          unsigned char block[TEST_BLOCK_LEN], digest[16];
          unsigned int i;
        
        Rivest                                                         [Page 18]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
          printf
         ("MD%d time trial. Digesting %d %d-byte blocks ...", MD,
          TEST_BLOCK_LEN, TEST_BLOCK_COUNT);
        
          /* Initialize block */
          for (i = 0; i < TEST_BLOCK_LEN; i++)
         block[i] = (unsigned char)(i & 0xff);
        
          /* Start timer */
          time (&startTime);
        
          /* Digest blocks */
          MDInit (&context);
          for (i = 0; i < TEST_BLOCK_COUNT; i++)
         MDUpdate (&context, block, TEST_BLOCK_LEN);
          MDFinal (digest, &context);
        
          /* Stop timer */
          time (&endTime);
        
          printf (" done\n");
          printf ("Digest = ");
          MDPrint (digest);
          printf ("\nTime = %ld seconds\n", (long)(endTime-startTime));
          printf
         ("Speed = %ld bytes/second\n",
          (long)TEST_BLOCK_LEN * (long)TEST_BLOCK_COUNT/(endTime-startTime));
        }
        
        /* Digests a reference suite of strings and prints the results.
         */
        static void MDTestSuite ()
        {
          printf ("MD%d test suite:\n", MD);
        
          MDString ("");
          MDString ("a");
          MDString ("abc");
          MDString ("message digest");
          MDString ("abcdefghijklmnopqrstuvwxyz");
          MDString
         ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789");
          MDString
         ("1234567890123456789012345678901234567890\
        1234567890123456789012345678901234567890");
        }
        
        /* Digests a file and prints the result.
        
        Rivest                                                         [Page 19]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
         */
        static void MDFile (filename)
        char *filename;
        {
          FILE *file;
          MD_CTX context;
          int len;
          unsigned char buffer[1024], digest[16];
        
          if ((file = fopen (filename, "rb")) == NULL)
         printf ("%s can't be opened\n", filename);
        
          else {
         MDInit (&context);
         while (len = fread (buffer, 1, 1024, file))
           MDUpdate (&context, buffer, len);
         MDFinal (digest, &context);
        
         fclose (file);
        
         printf ("MD%d (%s) = ", MD, filename);
         MDPrint (digest);
         printf ("\n");
          }
        }
        
        /* Digests the standard input and prints the result.
         */
        static void MDFilter ()
        {
          MD_CTX context;
          int len;
          unsigned char buffer[16], digest[16];
        
          MDInit (&context);
          while (len = fread (buffer, 1, 16, stdin))
         MDUpdate (&context, buffer, len);
          MDFinal (digest, &context);
        
          MDPrint (digest);
          printf ("\n");
        }
        
        /* Prints a message digest in hexadecimal.
         */
        static void MDPrint (digest)
        unsigned char digest[16];
        {
        
        Rivest                                                         [Page 20]
        
        RFC 1321              MD5 Message-Digest Algorithm            April 1992
        
          unsigned int i;
        
          for (i = 0; i < 16; i++)
         printf ("%02x", digest[i]);
        }
        
        A.5 Test suite
        
           The MD5 test suite (driver option "-x") should print the following
           results:
        
        MD5 test suite:
        MD5 ("") = d41d8cd98f00b204e9800998ecf8427e
        MD5 ("a") = 0cc175b9c0f1b6a831c399e269772661
        MD5 ("abc") = 900150983cd24fb0d6963f7d28e17f72
        MD5 ("message digest") = f96b697d7cb7938d525a2f31aaf161d0
        MD5 ("abcdefghijklmnopqrstuvwxyz") = c3fcd3d76192e4007dfb496cca67e13b
        MD5 ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") =
        d174ab98d277d9f5a5611c2c9f419d9f
        MD5 ("123456789012345678901234567890123456789012345678901234567890123456
        78901234567890") = 57edf4a22be3c955ac49da2e2107b67a
        
        Security Considerations
        
           The level of security discussed in this memo is considered to be
           sufficient for implementing very high security hybrid digital-
           signature schemes based on MD5 and a public-key cryptosystem.
        
        Author's Address
        
           Ronald L. Rivest
           Massachusetts Institute of Technology
           Laboratory for Computer Science
           NE43-324
           545 Technology Square
           Cambridge, MA  02139-1986
        
           Phone: (617) 253-5880
           EMail: rivest@theory.lcs.mit.edu
        
        Rivest                                                         [Page 21]
        
        ```
        
    - Anotações
        
        Message Digest 5
        
        Entrada de valor arbitrário
        
        Gera hash de 128 bits
        
        Usa 4 variáveis internas no seu mecanismo de consumo dos blocos e no final elas são concatenadas, possuem 32 bits cada uma
        
        Padding: mensagem preenchida para que seja congruente com 448 bits (módulo 512)
        
        Anexação do Comprimento da Mensagem Original: após preencher (antes do padding), o comprimento original da mensagem é expresso em 64 bits anexado ao final da mensagem
        
        Inicialização do buffer: utiliza as 4 variáveis de 32 bits inicializadas com valores específicos que quebra em 512 bits cada parte da messagem
        
        sub-blocks = m
        
        sub-constat = t
        
        Operações lógicas fixas 
        
        SHA - secure hash algorithm
        
        ![image.png](Seguran%C3%A7a%20de%20Dados%201282e5a697c38071a5c4f818fa65ac63/image.png)
        
        imagem do processo do md5
        
        se tenho um arquivo → hash¹
        
        coloco um ponto → hash²
        
        retiro o ponto → hash³
        
        **Tem que fazer em estilo artigo, para a primeira nota, a implementação do md5 - 17/12**
        
- Diffie-Hellman
    
    ```python
    # Diffie-Hellman Code
    # Power function to return value of a^b mod P
    def power(a, b, p):
        if b == 1:
            return a
        else:
            return pow(a, b) % p
    
    # Main function
    def main():
        # Both persons agree upon the public keys G and P
        # A prime number P is taken
        P = 23
        print("The value of P:", P)
    
        # A primitive root for P, G is taken
        G = 9
        print("The value of G:", G)
    
        # Alice chooses the private key a
        # a is the chosen private key
        a = 4
        print("The private key a for Alice:", a)
    
        # Gets the generated key
        x = power(G, a, P)
    
        # Bob chooses the private key b
        # b is the chosen private key
        b = 3
        print("The private key b for Bob:", b)
    
        # Gets the generated key
        y = power(G, b, P)
    
        # Generating the secret key after the exchange of keys
        ka = power(y, a, P)  # Secret key for Alice
        kb = power(x, b, P)  # Secret key for Bob
    
        print("Secret key for Alice is:", ka)
        print("Secret key for Bob is:", kb)
    
    if __name__ == "__main__":
        main()
    
    #https://www.geeksforgeeks.org/implementation-diffie-hellman-algorithm/ 
    ```
    
- DES
    - Exercício 3
        - Durante cada iteração do algoritmo DES, o bloco de 64 bits é dividido em duas partes (L, R). O que acontece com a metade L após a aplicação da função f()?
            
            A metade L é combinada com f() em uma operação XOR para gerar a nova metade R
            
        - O algoritmo 3DES (Triple DES) aplica o algoritmo DES três vezes para aumentar sua segurança. Considerando o funcionamento do 3DES no modo EDE (Encrypt-Decrypt-Encrypt), qual é o processo correto de encriptação de um bloco de dados quando três chaves independentes K1, K2 e K3 são utilizadas?
            
            O bloco de dados é criptografado com K1 , descriptografado com K2 e criptografado novamente com K3 .
            
        - O algoritmo DES utiliza uma série de rodadas para realizar a substituição e permutação dos dados. Em cada rodada, uma subchave é gerada a partir da chave principal de 56 bits. Qual é o número total de bits efetivamente usados no processo de geração de subchaves em todas as 16 rodadas do DES?
            
            48 bits por rodada, totalizando 768 bits. 
            
            No algoritmo DES (Data Encryption Standard), a chave principal tem 56 bits (efetivos, pois 8 bits adicionais são usados para paridade). Durante cada uma das 16 rodadas, uma subchave de **48 bits** é gerada e utilizada no processo de substituição e permutação. Como há 16 rodadas, o número total de bits utilizados é:
            
            48 bits/rodada×16 rodadas=768 bits.48 \, \text{bits/rodada} \times 16 \, \text{rodadas} = 768 \, \text{bits}.
            
            48bits/rodada×16rodadas=768bits.
            
        - Considere que a cifra de César está sendo utilizada para criptografar uma mensagem em um alfabeto de 26 caracteres. Se o deslocamento (k) usado para criptografar uma mensagem for desconhecido, qual é o número máximo de tentativas necessárias para descriptografar a mensagem por força bruta, assumindo que o atacante conhece o esquema de criptografia mas não a chave?
            
            A cifra de César utiliza um deslocamento k para criptografar uma mensagem, e o alfabeto possui 26 caracteres. Para descriptografar por força bruta:
            O deslocamento k pode assumir qualquer valor entre 0 e 25, totalizando **26 possíveis chaves**. 
            No entanto, se o deslocamento k=0 não altera a mensagem (é trivial), o número **máximo de tentativas necessárias é 25**.
            k=0k = 0
            A cifra de César é um tipo de substituição simples. Ao tentar todas as chaves possíveis (de 1 a 25), o atacante eventualmente encontrará a chave correta. A chave 0 não precisa ser testada, pois não modifica a mensagem.
            
        - Um dos desafios da criptografia simétrica é a escalabilidade no gerenciamento de chaves. Em uma rede com n usuários, qual é o número total de chaves simétricas exclusivas que precisam ser gerenciadas para garantir que cada par de usuários possa se comunicar de forma segura?
            
            n(n-1)/2, pois trabalha com chave compartilhada, ou seja: tenho um par de passoas → preciso de uma chave, aplicando a fórmula têm-se 2(2-1)/2 = 1
            
    - Código
        
        ```python
        # Python3 code for the above approach
        
        # Hexadecimal to binary conversion
        '''
        1. Conversões hexadecimais e binárias
        Função hex2bin(s)
        Converte uma string hexadecimal para binária:
        Um dicionário mapeia cada caractere hexadecimal (0-9, A-F) para seu equivalente binário de 4 bits.
        Para cada caractere da string hexadecimal s, concatena o binário correspondente na string bin.
        '''
        def hex2bin(s):
        	mp = {'0': "0000",
        		'1': "0001",
        		'2': "0010",
        		'3': "0011",
        		'4': "0100",
        		'5': "0101",
        		'6': "0110",
        		'7': "0111",
        		'8': "1000",
        		'9': "1001",
        		'A': "1010",
        		'B': "1011",
        		'C': "1100",
        		'D': "1101",
        		'E': "1110",
        		'F': "1111"}
        	bin = ""
        	for i in range(len(s)):
        		bin = bin + mp[s[i]]
        	return bin
        
        # Binary to hexadecimal conversion
        '''
        Função bin2hex(s)
        Converte uma string binária para hexadecimal:
        Divide a string binária em blocos de 4 bits e usa um dicionário para mapeá-los ao hexadecimal correspondente.
        Concatena o resultado em uma string hex.
        '''
        def bin2hex(s):
        	mp = {"0000": '0',
        		"0001": '1',
        		"0010": '2',
        		"0011": '3',
        		"0100": '4',
        		"0101": '5',
        		"0110": '6',
        		"0111": '7',
        		"1000": '8',
        		"1001": '9',
        		"1010": 'A',
        		"1011": 'B',
        		"1100": 'C',
        		"1101": 'D',
        		"1110": 'E',
        		"1111": 'F'}
        	hex = ""
        	for i in range(0, len(s), 4):
        		ch = ""
        		ch = ch + s[i]
        		ch = ch + s[i + 1]
        		ch = ch + s[i + 2]
        		ch = ch + s[i + 3]
        		hex = hex + mp[ch]
        
        	return hex
        
        # Binary to decimal conversion
        '''
        Função bin2dec(binary)
        Converte binário em decimal:
        Decompõe o número binário em dígitos, aplica a fórmula decimal+= bitx2**posicao, e acumula o resultado.
        '''
        def bin2dec(binary):
        
        	binary1 = binary
        	decimal, i, n = 0, 0, 0
        	while(binary != 0):
        		dec = binary % 10
        		decimal = decimal + dec * pow(2, i)
        		binary = binary//10
        		i += 1
        	return decimal
        
        # Decimal to binary conversion
        '''
        Função dec2bin(num)
        Converte decimal em binário, garantindo que o resultado tenha comprimento múltiplo de 4:
        Usa bin() para conversão e adiciona zeros à esquerda, se necessário.
        '''
        def dec2bin(num):
        	res = bin(num).replace("0b", "")
        	if(len(res) % 4 != 0):
        		div = len(res) / 4
        		div = int(div)
        		counter = (4 * (div + 1)) - len(res)
        		for i in range(0, counter):
        			res = '0' + res
        	return res
        
        # Permute function to rearrange the bits
        '''
        2. Funções de manipulação de bits
        Função permute(k, arr, n)
        Permuta os bits de k conforme uma tabela de permutação arr:
        Para cada índice na tabela, adiciona o bit correspondente de k na nova string permutation.
        '''
        def permute(k, arr, n):
        	permutation = ""
        	for i in range(0, n):
        		permutation = permutation + k[arr[i] - 1]
        	return permutation
        
        # shifting the bits towards left by nth shifts
        '''
        Função shift_left(k, nth_shifts)
        Realiza deslocamento circular à esquerda em uma string k:
        Desloca os bits pela quantidade nth_shifts.
        '''
        def shift_left(k, nth_shifts):
        	s = ""
        	for i in range(nth_shifts):
        		for j in range(1, len(k)):
        			s = s + k[j]
        		s = s + k[0]
        		k = s
        		s = ""
        	return k
        
        # calculating xow of two strings of binary number a and b
        '''
        Função xor(a, b)
        Calcula o XOR bit a bit entre duas strings binárias a e b:
        Para cada bit, compara se são iguais (0) ou diferentes (1).
        '''
        def xor(a, b):
        	ans = ""
        	for i in range(len(a)):
        		if a[i] == b[i]:
        			ans = ans + "0"
        		else:
        			ans = ans + "1"
        	return ans
        
        '''
        3. Tabelas do DES
        As tabelas definidas (ex.: initial_perm, exp_d, etc.) especificam como os bits devem ser organizados durante o processo de criptografia. 
        Elas fazem parte do padrão DES.
        '''
        # Table of Position of 64 bits at initial level: Initial Permutation Table
        initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
        				60, 52, 44, 36, 28, 20, 12, 4,
        				62, 54, 46, 38, 30, 22, 14, 6,
        				64, 56, 48, 40, 32, 24, 16, 8,
        				57, 49, 41, 33, 25, 17, 9, 1,
        				59, 51, 43, 35, 27, 19, 11, 3,
        				61, 53, 45, 37, 29, 21, 13, 5,
        				63, 55, 47, 39, 31, 23, 15, 7]
        # Expansion D-box Table
        exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
        		6, 7, 8, 9, 8, 9, 10, 11,
        		12, 13, 12, 13, 14, 15, 16, 17,
        		16, 17, 18, 19, 20, 21, 20, 21,
        		22, 23, 24, 25, 24, 25, 26, 27,
        		28, 29, 28, 29, 30, 31, 32, 1]
        # Straight Permutation Table
        per = [16, 7, 20, 21,
        	29, 12, 28, 17,
        	1, 15, 23, 26,
        	5, 18, 31, 10,
        	2, 8, 24, 14,
        	32, 27, 3, 9,
        	19, 13, 30, 6,
        	22, 11, 4, 25]
        # S-box Table
        sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        
        		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
        
        		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
        
        		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
        
        		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
        
        		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
        
        		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
        
        		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
        # Final Permutation Table
        final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
        			39, 7, 47, 15, 55, 23, 63, 31,
        			38, 6, 46, 14, 54, 22, 62, 30,
        			37, 5, 45, 13, 53, 21, 61, 29,
        			36, 4, 44, 12, 52, 20, 60, 28,
        			35, 3, 43, 11, 51, 19, 59, 27,
        			34, 2, 42, 10, 50, 18, 58, 26,
        			33, 1, 41, 9, 49, 17, 57, 25]
        
        '''
        4. Função de Criptografia
        Processo Geral
        '''
        def encrypt(pt, rkb, rk):
        	pt = hex2bin(pt)
        	#Conversão inicial: Converte o texto claro (plaintext) de hexadecimal para binário usando hex2bin(pt).
        
        	print(bin2hex(pt))
        
        	# Initial Permutation
        	pt = permute(pt, initial_perm, 64)
        	#Permutação inicial: Usa a tabela initial_perm para rearranjar os bits.
        
        	print("After initial permutation", bin2hex(pt))
        
        	'''
        	Divisão:
        	Divide o texto permutado em duas metades: left (32 bits) e right (32 bits).
        	
        	16 Rodadas de Criptografia:
        	Expande right de 32 para 48 bits usando exp_d.
        	Aplica XOR entre right_expanded e a chave da rodada.
        	Substitui valores com as tabelas S-box.
        	Permuta bits com a tabela per.
        	Aplica XOR com left e troca os lados (exceto na última rodada).
        	'''
        	# Splitting
        	left = pt[0:32]
        	right = pt[32:64]
        	for i in range(0, 16):
        		# Expansion D-box: Expanding the 32 bits data into 48 bits
        		right_expanded = permute(right, exp_d, 48)
        
        		# XOR RoundKey[i] and right_expanded
        		xor_x = xor(right_expanded, rkb[i])
        
        		# S-boxex: substituting the value from s-box table by calculating row and column
        		sbox_str = ""
        		for j in range(0, 8):
        			row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
        			col = bin2dec(
        				int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
        			val = sbox[j][row][col]
        			sbox_str = sbox_str + dec2bin(val)
        
        		# Straight D-box: After substituting rearranging the bits
        		sbox_str = permute(sbox_str, per, 32)
        
        		# XOR left and sbox_str
        		result = xor(left, sbox_str)
        		left = result
        
        		# Swapper
        		if(i != 15):
        			left, right = right, left
        		print("Round ", i + 1, " ", bin2hex(left),
        			" ", bin2hex(right), " ", rk[i])
        
        	# Combination
        	combine = left + right
        
        	# Final permutation: final rearranging of bits to get cipher text
        	cipher_text = permute(combine, final_perm, 64)
        	return cipher_text
        
        pt = "123456ABCD132536"
        key = "AABB09182736CCDD"
        
        # Key generation
        # --hex to binary
        key = hex2bin(key)
        
        # --parity bit drop table
        keyp = [57, 49, 41, 33, 25, 17, 9,
        		1, 58, 50, 42, 34, 26, 18,
        		10, 2, 59, 51, 43, 35, 27,
        		19, 11, 3, 60, 52, 44, 36,
        		63, 55, 47, 39, 31, 23, 15,
        		7, 62, 54, 46, 38, 30, 22,
        		14, 6, 61, 53, 45, 37, 29,
        		21, 13, 5, 28, 20, 12, 4]
        
        # getting 56 bit key from 64 bit using the parity bits
        key = permute(key, keyp, 56)
        
        # Number of bit shifts
        shift_table = [1, 1, 2, 2,
        			2, 2, 2, 2,
        			1, 2, 2, 2,
        			2, 2, 2, 1]
        
        # Key- Compression Table : Compression of key from 56 bits to 48 bits
        key_comp = [14, 17, 11, 24, 1, 5,
        			3, 28, 15, 6, 21, 10,
        			23, 19, 12, 4, 26, 8,
        			16, 7, 27, 20, 13, 2,
        			41, 52, 31, 37, 47, 55,
        			30, 40, 51, 45, 33, 48,
        			44, 49, 39, 56, 34, 53,
        			46, 42, 50, 36, 29, 32]
        
        # Splitting
        left = key[0:28] # rkb for RoundKeys in binary
        right = key[28:56] # rk for RoundKeys in hexadecimal
        
        rkb = []
        rk = []
        for i in range(0, 16):
        	# Shifting the bits by nth shifts by checking from shift table
        	left = shift_left(left, shift_table[i])
        	right = shift_left(right, shift_table[i])
        
        	# Combination of left and right string
        	combine_str = left + right
        
        	# Compression of key from 56 to 48 bits
        	round_key = permute(combine_str, key_comp, 48)
        
        	rkb.append(round_key)
        	rk.append(bin2hex(round_key))
        
        print("Encryption")
        cipher_text = bin2hex(encrypt(pt, rkb, rk))
        print("Cipher Text : ", cipher_text)
        
        print("Decryption")
        rkb_rev = rkb[::-1]
        rk_rev = rk[::-1]
        text = bin2hex(encrypt(cipher_text, rkb_rev, rk_rev))
        print("Plain Text : ", text)
        
        # This code is contributed by Aditya Jain
        # https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/ 
        ```
        
- Certificados e Assinaturas
    
    **Assinatura Digital:** confirmar que a pessoa é quem diz ser, ou seja, cifrar um hash com uma chave privada
    
    **HMAC (Hash-Based Message Authentication Code):**  cifrar de forma simétrica um hash com uma chave privada
    
    **SSL** (Secure Socket Layer) 3.0 - Netscape 1996 (Internet para o meio comercial)
    
    **TSl** - Ietf lança ele de forma gratuita, atualmente apenas a 1.2 e a 1.3 são consideradas seguras pois as outras versões utilizam funções hash
    
    Chave única para cada sessão, se abri uma aba mesmo que entre no mesmo site ele irá gerar uma nova chave
    
    Provém confidencialidade e integridade de dados na comunicação entre duas aplicações
    
    Conexão confidencial: dados cifrados com criptografia simétrica, com algoritmos e chaves negociados entre cliente e servidor, chave única
    
    Na aplicação cliente  → digito a url 
    
    Quando a conexão está estabelecida → socket (como sabe para onde cada pacote deve ir)
    
    ex: email e yt ele vai pegar o pacote e direcionar para qual porta ele  estabeleceu no socket (cada aplicação tem um)
    
    Não envia nem devolve diretamente vai esperar a verificação pelo SSL/TLS 
    
    Na nossa aplicação: usa s.socket no lugar do socket, isso não muda a lógica da aplicação
    
    - Conexão:
        
        ClientHello: “servirdor eu tenho esses recursos (algoritmos de criptografia) você consegue acompanhar?” → Precisam negociar parâmetros para comunicação
        
        cria um número randômico de 28 bytes (+algo do servidor) para chave se sessão
        
        Session ID: identificador único da sessão para o cliente
        
        Cipher suite: suite de cifras suportadas pelo cliente (no lado do servir ele escolhe apenas uma)
        
        Compression Method: método de compressão selecionado
        
        ClientKeyExchange é a chave de sessão
        
    
    **Cipher Block Chain**: antes de encriptar faz-se um xor com a saída do bloco anterior, com uma cadeia e blocos
    
    **MAC:** 
    
- SQL Injection
    - Exemplos
        - https://www.cisoadvisor.com.br/milhoes-de-registros-sao-roubados-de-sites-com-injecao-de-sql/
            
            Hackers do grupo autodenominado ResumeLooters comprometem sites de recrutamento e varejo usando injeção de SQL e ataques XSS (cross-site scripting). Entre novembro e dezembro do ano passado, a gangue roubou mais de 2 milhões de endereços de e-mail e outras informações pessoais de pelo menos 65 sites, informa a empresa de inteligência de ameaças Group-IB.Os ataques observados se assemelharam aos lançados pelo GambleForce, um operador de ameaças que depende de injeções de SQL para comprometer sites de jogos de azar e governamentais na Ásia-Pacífico. Assim como o GambleForce, o ResumeLooters foi visto usando várias ferramentas de código aberto e estruturas de teste de penetração em seus ataques de injeção de SQL. A principal diferença entre eles, no entanto, é que o ResumeLooters também usou scripts XSS injetados em sites legítimos de busca de empregos, destinados a exibir formulários de phishing e coletar credenciais administrativas. Os scripts foram executados em pelo menos quatro sites e em alguns dispositivos com acesso administrativo.Em um caso, o grupo criou um perfil de empregador falso em um site de recrutamento e injetou um script XSS usando um dos campos do perfil. Em outro caso, o código XSS foi incluído em um currículo falso. Através da injeção de consultas SQL maliciosas, o operador da ameaça conseguiu recuperar bases de dados contendo cerca de 2,2 milhões de linhas, das quais mais de 500 mil representavam dados de usuários de sites de emprego.É confirmado que ResumeLooters roubou vários bancos de dados contendo 2.079.027 e-mails exclusivos e outros registros, como nomes, números de telefone, datas de nascimento, bem como informações sobre a experiência e histórico de emprego dos candidatos a emprego”, afirma o Group-IB.
            
        - https://brightsec.com/blog/sql-injection-attack/
            
            Violações permitidas por injeção de SQL• Ataque GhostShell — hackers do grupo APT Team GhostShell atacaram 53 universidades usando injeção de SQL, roubaram e publicaram 36.000 registros pessoais pertencentes a alunos, professores e funcionários.• Governo turco — outro grupo APT, o coletivo RedHack, usou injeção de SQL para violar o site do governo turco e apagar dívidas com agências governamentais.• Violação da 7-Eleven — uma equipe de invasores usou injeção de SQL para invadir sistemas corporativos em diversas empresas, principalmente na rede de varejo 7-Eleven, roubando 130 milhões de números de cartão de crédito.• Violação da HBGary — hackers relacionados ao grupo ativista Anonymous usaram SQL Injection para derrubar o site da empresa de segurança de TI. O ataque foi uma resposta ao CEO da HBGary ter divulgado que ele tinha nomes de membros da organização Anonymous.
            
        - https://www.avg.com/en/signal/sql-injection
            
            Real-world SQL injection examples• In 2008, payment processor Heartland Payment Systems was hacked via SQL injection for over $130 million in losses. The attackers stole a whopping 130 million credit card numbers in one of the biggest data breaches of credit card data in history. • In 2014, a hacker gang collected over 1.2 billion unique IDS and password combinations from over 420,000 websites all across the internet. The Russian hacker group used SQL injections to command databases to reveal and dump their contents.• UK telecom giant TalkTalk came under fire in 2015 for weak web security that compromised hundreds of thousands of customers’ personal information. Even though SQL security risks were well-known at the time, the company was helpless against the attack.• For an SQL injection example that concerns the everyday gamer, Epic Games had their forums hacked in 2016, and 800,000 user accounts were leaked. SQL injections targeted the popular online message board software vBulletin, which has become infamous for its vulnerability to SQL exploits. In general, SQL injection attacks are spreading through the gaming industry like wildfire.
            
        
    - Fonte 1 - [w3schools](https://www.w3schools.com/sql/sql_injection.asp)
        
        # SQL Injection
        
        SQL injection is a code injection technique that might destroy your database.
        
        SQL injection is one of the most common web hacking techniques.
        
        SQL injection is the placement of malicious code in SQL statements, via web page input.
        
        ---
        
        # SQL in Web Pages
        
        SQL injection usually occurs when you ask a user for input, like their username/userid, and instead of a name/id, the user gives you an SQL statement that you will unknowingly run on your database.
        
        Look at the following example which creates a SELECT statement by adding a variable (txtUserId) to a select string. The variable is fetched from user input (getRequestString):
        
        ### Example
        
        ### [Get your own SQL Server](https://www.w3schools.com/sql/sql_server.asp)
        
        txtUserId = getRequestString("UserId");
        
        txtSQL = "SELECT * FROM Users WHERE UserId = " + txtUserId;
        
        The rest of this chapter describes the potential dangers of using user input in SQL statements.
        
        ---
        
        # SQL Injection Based on 1=1 is Always True
        
        Look at the example above again. The original purpose of the code was to create an SQL statement to select a user, with a given user id.
        
        If there is nothing to prevent a user from entering "wrong" input, the user can enter some "smart" input like this:
        
        UserId:
        
        Then, the SQL statement will look like this:
        
        SELECT * FROM Users WHERE UserId = 105 OR 1=1;
        
        The SQL above is valid and will return ALL rows from the "Users" table, since OR 1=1 is always TRUE.
        
        Does the example above look dangerous? What if the "Users" table contains names and passwords?
        
        The SQL statement above is much the same as this:
        
        SELECT UserId, Name, Password FROM Users WHERE UserId = 105 or 1=1;
        
        A hacker might get access to all the user names and passwords in a database, by simply inserting 105 OR 1=1 into the input field.
        
        ---
        
        ---
        
        # SQL Injection Based on ""="" is Always True
        
        Here is an example of a user login on a web site:
        
        Username:
        
        Password:
        
        ### Example
        
        uName = getRequestString("username");
        
        uPass = getRequestString("userpassword");
        
        sql = 'SELECT * FROM Users WHERE Name ="' + uName + '" AND Pass ="' + uPass + '"'
        
        ### Result
        
        SELECT * FROM Users WHERE Name ="John Doe" AND Pass ="myPass"
        
        A hacker might get access to user names and passwords in a database by simply inserting " OR ""=" into the user name or password text box:
        
        User Name:
        
        Password:
        
        The code at the server will create a valid SQL statement like this:
        
        ### Result
        
        SELECT * FROM Users WHERE Name ="" or ""="" AND Pass ="" or ""=""
        
        The SQL above is valid and will return all rows from the "Users" table, since OR ""="" is always TRUE.
        
        ---
        
        # SQL Injection Based on Batched SQL Statements
        
        Most databases support batched SQL statement.
        
        A batch of SQL statements is a group of two or more SQL statements, separated by semicolons.
        
        The SQL statement below will return all rows from the "Users" table, then delete the "Suppliers" table.
        
        ### Example
        
        SELECT * FROM Users; DROP TABLE Suppliers
        
        Look at the following example:
        
        ### Example
        
        txtUserId = getRequestString("UserId");
        
        txtSQL = "SELECT * FROM Users WHERE UserId = " + txtUserId;
        
        And the following input:
        
        User id:
        
        The valid SQL statement would look like this:
        
        ### Result
        
        SELECT * FROM Users WHERE UserId = 105; DROP TABLE Suppliers;
        
        ---
        
        # Use SQL Parameters for Protection
        
        To protect a web site from SQL injection, you can use SQL parameters.
        
        SQL parameters are values that are added to an SQL query at execution time, in a controlled manner.
        
        ### ASP.NET Razor Example
        
        txtUserId = getRequestString("UserId");
        
        txtSQL = "SELECT * FROM Users WHERE UserId = @0";
        
        db.Execute(txtSQL,txtUserId);
        
        Note that parameters are represented in the SQL statement by a @ marker.
        
        The SQL engine checks each parameter to ensure that it is correct for its column and are treated literally, and not as part of the SQL to be executed.
        
        ### Another Example
        
        txtNam = getRequestString("CustomerName");
        
        txtAdd = getRequestString("Address");
        
        txtCit = getRequestString("City");
        
        txtSQL = "INSERT INTO Customers (CustomerName,Address,City) Values(@0,@1,@2)";
        
        db.Execute(txtSQL,txtNam,txtAdd,txtCit);
        
        ---
        
        # Examples
        
        The following examples shows how to build parameterized queries in some common web languages.
        
        SELECT STATEMENT IN ASP.NET:
        
        txtUserId = getRequestString("UserId");
        
        sql = "SELECT * FROM Customers WHERE CustomerId = @0";
        
        command = new SqlCommand(sql);
        
        command.Parameters.AddWithValue("@0",txtUserId);
        
        command.ExecuteReader();
        
        INSERT INTO STATEMENT IN ASP.NET:
        
        txtNam = getRequestString("CustomerName");
        
        txtAdd = getRequestString("Address");
        
        txtCit = getRequestString("City");
        
        txtSQL = "INSERT INTO Customers (CustomerName,Address,City) Values(@0,@1,@2)";
        
        command = new SqlCommand(txtSQL);
        
        command.Parameters.AddWithValue("@0",txtNam);
        
        command.Parameters.AddWithValue("@1",txtAdd);
        
        command.Parameters.AddWithValue("@2",txtCit);
        
        command.ExecuteNonQuery();
        
        INSERT INTO STATEMENT IN PHP:
        
        $stmt = $dbh->prepare("INSERT INTO Customers (CustomerName,Address,City)
        
        VALUES (:nam, :add, :cit)");
        
        $stmt->bindParam(':nam', $txtNam);
        
        $stmt->bindParam(':add', $txtAdd);
        
        $stmt->bindParam(':cit', $txtCit);
        
        $stmt->execute();
        
        ---
        
        # Exercise
        
        What is SQL injection?
        
        A technique to optimize SQL queries
        
        A code injection technique to access or destroy a database
        
        A method to protect SQL queries from being hacked
        
        A debugging process for SQL queries
        
        What does the statement 1=1 in a SQL query imply?
        
        A logical statement that is always true
        
        A conditional operator for database sorting
        
        To copy data from one table into a new table
        
        To create an index on a table
        
        Which approach helps prevent SQL injection attacks?
        
        Using concatenated SQL strings
        
        Using the NULL operator
        
        Using SQL parameters
        
        Allowing multiple SQL statements in a query
        
        Drag and drop the correct parameterized placeholder to complete the SQL query.
        
        SELECT * FROM Customers WHERE CustomerId = ______ ;
        
        @0
        
        :id
        
        ?param
        
        @CustomerId
        
    - Fonte 2 - [devmedia](https://www.devmedia.com.br/sql-injection/6102)
        
        # **SQL Injection**
        
        ## Esse artigo ensina sobre o SQL Injection que é uma classe de ataque onde o invasor pode inserir ou manipular consultas criadas pela aplicação, que são enviadas diretamente para o banco de dados relacional.
        
        [Artigos](https://www.devmedia.com.br/artigos/)[Banco de Dados](https://www.devmedia.com.br/artigos/banco-de-dados)SQL Injection
        
        Segurança sempre foi e será um tema que preocupa todos nós, seja em casa, nas ruas ou no trabalho. Quando falamos de segurança em informática, não existe um só departamento de uma única empresa que não tenha também esta preocupação. Se questionarmos sobre segurança com desenvolvedores e DBAs, a preocupação será maior ainda, pois são justamente estes dois departamentos os principais responsáveis pelas aplicações que as empresas disponibilizam na rede local (intranet), ou global (internet). São vários os objetos dessa preocupação, mas existe um tema relativamente antigo, desconhecidos por muitos, mas com potencial devastador quando explorado: o SQL Injection, que será o assunto dessa matéria.
        
        ### **O que é SQL Injection?**
        
        O SQL Injection é uma técnica de ataque baseada na manipulação do código SQL, que é a linguagem utilizada para troca de informações entre aplicativos e bancos de dados relacionais. Como a maioria dos fabricantes de software utiliza o padrão SQL-92 ANSI (ver Nota 1) na escrita do código SQL, os problemas e as falhas de segurança aqui apresentadas se aplicam a todo ambiente que faz uso desse padrão para troca de informações - o que inclui, por exemplo, servidores Oracle. Nesse artigo foram utilizados servidores da plataforma Microsoft: Internet Information Server, Active Server Pages e Microsoft SQL Server.
        
        Relacionado: [Update Triggers: Como proteger tabelas de SQL Injection](https://www.devmedia.com.br/update-triggers-como-proteger-tabelas-de-sql-injection/37594)
        
        **Nota 1**: ANS
        
        O American National Standards Institute (ANSI) é uma organização sem fins lucrativos cuja finalidade é criar padrões de aceitação internacional sobre um determinado assunto.
        
        ### **SQL Injection: O que é? Por que funciona?**
        
        SQL Injection é uma classe de ataque onde o invasor pode inserir ou manipular consultas criadas pela aplicação, que são enviadas diretamente para o banco de dados relacional.
        
        Por que o SQL Injection funciona?
        
        - Por que a aplicação aceita dados arbitrários fornecidos pelo usuário (“confia” no texto digitado);
        - As conexões são feitas no contexto de um usuário com privilégios altos.
        
        Para entendermos um pouco melhor o que é SQL Injection e por que funciona, vamos analisar exemplos práticos.
        
        ### **Ataques de SQL Injection pela tela de Login**
        
        A técnica mais simples de ataque que explora SQL Injection é a que “engana” o formulário login de uma aplicação. Suponha que uma determinada aplicação web faça uso do código exibido na Listagem 1, em que o usuário digita seu nome e senha.
        
        [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfw8BkhsQ_r2k4TE1P_76_XB6RI3rLZhKm60oxjbnmF4Y3P2L6WPEnieavZfTJhkwGgySLhKD_6AFTCEwsE9nKFW0OBIqohYOaKC70LY1k6Bp2iKESFY20Y2XbID5XTy4tzTxufBQ?key=ZrbJaXHcJo6QVB-SCb6bUjpB)
        
        **Listagem 1**. Código de um formulário de uma aplicação web onde o usuário digita nome e senha
        
        A **Figura 1** ilustra como este formulário é exibido para o usuário
        
        [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcsn4BgJYpecGlFLqK60ff38XORRnqiuHTGWdDM54fjPydb7KbyvVzdvrdHB4flIiBCHVAzoENei2eo4DBqu1OdpB6MPObA5i3I7kkb82B84P7oWbNAKcoig5fDWXLh8ca9dUPt?key=ZrbJaXHcJo6QVB-SCb6bUjpB)
        
        **Figura 1**
        
        . Tela de Login onde o usuário digita nome (Username) e senha (Password)
        
        O código presente na **Listagem 2** mostra como a informação digitada pelo usuário será processada na aplicação web.
        
        [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcjBKP-kFbzGZpKcDW0F3f77Cx0bDkRBJ45pIH9ESBq_l2KK2Bq6hBs9lKRWd4uQOBVfWHcCpzmxbDq4wqBtoNlR4D99qmNjsLtE5nhEsNI3Hyfkzx-1Pl95i88EzEo7bOWPjCDmg?key=ZrbJaXHcJo6QVB-SCb6bUjpB)
        
        **Listagem 2**. Código de validação de usuário e senha
        
        Ao digitar o nome e senha (ver **Figura 1**), a aplicação web dispara uma consulta na tabela “USERS” para confirmação do cadastro do usuário. Se um registro for encontrado, o username será retornado e esta é a confirmação de que o usuário foi autenticado com sucesso. Se a consulta na tabela “USERS” não retornar registros, o usuário não será autenticado.
        
        O principal problema do código da **Listagem 2** é o trecho responsável pela montagem do comando sql que será executado (ver **Listagem 3**).
        
        var sql = "select * from users where username = '" + username + "' and password = '" + password + "'";
        
        **Listagem 3**. Código que concatena o comando sql a ser executado
        
        Este código é problemático porque não realiza nenhum tipo de validação nos dados que foram digitados pelo usuário. Isso permite que um usuário mal intencionado, que conheça somente o nome de um usuário válido, consiga “burlar” a digitação da senha informando os seguintes parâmetros na tela de autenticação (ver **Listagem 4** )
        
        Username: admin'--
        
        Password:
        
        **Listagem 4**. Parâmetro para login sem a necessidade de especificar a senha
        
        No exemplo da **Listagem 4** o usuário mal intencionado será autenticado com sucesso pois a seqüência de caracteres “--” faz com que todo o restante do comando após esta seqüência seja considerado como comentário. O comando será executado sem retornar erros, pois o código “"' AND PASSWORD = '" + PASSWORD + "'";” não será processado.
        
        Agora suponha que, em oposição ao exemplo anterior, o invasor não tenha conhecimento de um nome de usuário válido. Neste caso, ele pode se autenticar com as credenciais do primeiro usuário cadastrado na tabela “USERS” conforme mostra a **Listagem 5**.
        
        Username: ' or 1=1--
        
        Password:
        
        **Listagem 5**. Login com as credenciais do primeiro usuário cadastrado na tabela “USERS”
        
        A utilização destes parâmetros fará com que a comparação “1=1” seja processada como parte da consulta. Como esta comparação é sempre verdadeira, todos os registros da tabela serão retornados. Como seu resultado esta sendo armazenado em uma variável, o nome do primeiro usuário será considerado. Observe que também neste caso é utilizada a seqüência de caracteres “--” para que o restante do código não seja processado.
        
        Se o invasor estiver mal intencionado, ele pode, por exemplo, excluir todos os registros da tabela “USERS” de modo que nenhum usuário mais tenha acesso ao sistema, conforme exemplificado na **Listagem 6.**
        
        Username: '; delete from users--
        
        Password:
        
        **Listagem 6**. Parâmetros de usuário e senha especificados por um usuário mal intencionado
        
        Neste caso, a única novidade é o caractere “;” que especifica o término de um comando SQL e o início de outro.
        
        ### **Ataques através da interpretação das mensagens de erro**
        
        Para manipular os dados em um database, o usuário mal intencionado precisa descobrir a estrutura de alguns objetos. A tabela “USERS” utilizada nos exemplos anteriores poderia ter sido criada e populada através do código exibido na **Listagem 7**.
        
        create table users (
        
        id int,
        
        username varchar(255),
        
        password varchar(255),
        
        privs int )
        
        go
        
        insert into users values( 0, 'admin', 'r00tr0x!', 0xffff ) insert into users values( 0, 'guest', 'guest', 0x0000 )
        
        insert into users values( 0, 'chris', 'password', 0x00ff ) insert into users values( 0, 'fred', 'sesame', 0x00ff )
        
        go
        
        **Listagem 7**. Comando utilizado para a criação da tabela “USERS” e inserção de dados
        
        Suponha que nosso usuário mal intencionado queira cadastrar um usuário nessa tabela. Sem conhecer a estrutura da tabela, ele terá poucas chances de sucesso. Mesmo que ele tenha sorte, o significado das colunas pode não ser claro o bastante – veja o caso da coluna “PRIVS”, responsável pelo armazenamento dos privilégios dos usuários: um usuário mal intencionado poderia inserir o valor “1” nessa coluna, quando na verdade gostaria de atribuir o valor “65535” para que possuísse privilégios administrativos na aplicação.
        
        Felizmente, para este usuário mal intencionado, se as mensagens de erro forem retornadas diretamente da aplicação (comportamento padrão ASP), ele poderá descobrir não só a estrutura da tabela – dependendo do padrão de segurança atribuído ao usuário conectado no banco – mas também alterar e criar objetos diretamente no banco de dados SQL Server. Os exemplos a seguir irão ilustrar essa técnica.
        
        Inicialmente o usuário mal intencionado precisa descobrir os nomes das tabelas e colunas onde as consultas são executadas. Para isso, ele pode utilizar a cláusula HAVING do comando SELECT conforme demonstrado na **Listagem 8**.
        
        Username: ' having 1=1--
        
        - - Error Microsoft OLE DB Provider for ODBC Drivers error '80040e14'
        
        [Microsoft][ODBC SQL Server Driver][SQL Server]Column 'users.id' is invalid in the
        
        select list because it is not contained in an aggregate function and there is no GROUP BY clause.
        
        /process_login.asp, line 35
        
        **Listagem 8**. Uso da cláusula “HAVING” para obtenção de um erro que retorna o nome da tabela e da sua primeira coluna
        
        Nesse momento o usuário mal intencionado já sabe o nome da tabela (“USERSIS”) e sua primeira coluna (“ID”) e pode continuar reproduzindo este erro, introduzindo agora o nome da coluna descoberta em uma cláusula GROUP BY para descobrir o nome da coluna seguinte (ver **Listagem 9**).
        
        Username: ' group by users.id having 1=1--
        
        - - Error
        
        Microsoft OLE DB Provider for ODBC Drivers error '80040e14' [Microsoft][ODBC SQL Server Driver][SQL Server]Column 'users.username' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause.
        
        /process_login.asp, line 35
        
        **Listagem 9**. Uso da cláusula “HAVING” para obtenção de um erro que retorna o nome da segunda coluna da tabela
        
        Com isso, descobriu-se a coluna seguinte (“USERNAME”) e, em um processo de repetição, obtém-se os nomes de todas as colunas da tabela. Ao final – quando todas as colunas forem utilizadas – o comando não retornará erro e o nosso usuário mal intencionado ficará conhecendo a estrutura da tabela “USERS” (ver **Listagem 10**).
        
        Username: ' group by users.id, users.username, users.password, users.privs having 1=1--
        
        **Listagem 10**. Uso da cláusula “HAVING” com todos os campos da tabela
        
        A consulta processada pelo servidor na **Listagem 10** é equivalente ao comando exibido na **Listagem 11**.
        
        select * from users where username = ''
        
        **Listagem 11**. Comando equivalente ao processado pelo servidor ao final do processo
        
        Com isso o usuário mal intencionado já sabe que a consulta referencia somente a tabela “USERS” e as colunas utilizadas são “ID,USERNAME, PASSWORD, PRIVS” nesta ordem.
        
        Seria interessante descobrir o tipo de dado de cada coluna. Isso pode ser obtido com a utilização de uma mensagem de erro do tipo “type conversion” conforme exibido na **Listagem 12.**
        
        Username: ' union select sum(username) from users--
        
        - - Error
        
        Microsoft OLE DB Provider for ODBC Drivers error '80040e07'
        
        [Microsoft][ODBC SQL Server Driver][SQL Server]The sum or average aggregate operation cannot take a varchar data type as an argument.
        
        /process_login.asp, line 35
        
        **Listagem 12**. Erro que permite identificar o tipo de dado de uma coluna
        
        Esta técnica se aproveita do fato do SQL Server processar a cláusula SUM antes de verificar se o número de colunas presentes nos dois comandos SELECT (necessário para processar o UNION) são iguais. A tentativa de executar uma soma em uma coluna tipo caracter resulta em uma incompatibilidade, caracterizada pelo erro que descreve a coluna “USERNAME” como VARCHAR. Se por outro lado tentássemos executar a soma de um campo numérico, o erro retornado informaria que o numero de colunas nos dois comandos SELECT é diferente, o que pode ser constatado pelo código presente na **Listagem 13**.
        
        Username: ' union select sum(id) from users--
        
        - - Error
        
        Microsoft OLE DB Provider for ODBC Drivers error '80040e14' [Microsoft][ODBC SQL Server Driver][SQL Server]All queries in an SQL statement containing a UNION operator must have an equal number of expressions in their target lists. /process_login.asp, line 35
        
        **Listagem 13**. Erro que permite identificar o tipo de dado de uma é numérico
        
        Esta técnica pode ser utilizada para identificar, de modo aproximado, o tipo de dado de cada coluna em cada tabela no banco de dados. Assim, conhecendo-se as colunas da tabela “USERS”, nosso usuário mal intencionado pode criar um comando INSERT coerente com a estrutura da tabela (ver **Listagem 14** ).
        
        Username: '; insert into users values( 666, 'attacker', 'foobar', 0xffff )--
        
        **Listagem 14**. Cadastro realizado pelo usuário mal intencionado depois obter a estrutura aproximada da tabela
        
        O problema é que o potencial desta técnica não está limitado a esse tipo de ação. Nosso usuário mal intencionado pode se aproveitar de qualquer mensagem de erro que revele informações sobre o ambiente ou banco de dados que está sendo utilizado. Uma forma de explorar este recurso é através de mensagens relacionadas com conversão de tipo de dados: se você tentar converter um tipo de dado caractere (CHAR) em um tipo de dado numérico (INTEGER), todos os caracteres são retornados na mensagem de erro. Com isso, o usuário mal intencionado pode obter, por exemplo, a versão do SQL Server que você esta utilizando e o sistema operacional. Um exemplo disso pode ser visto na **Listagem 15** a seguir.
        
        Username: ' union select @@version,1,1,1--
        
        - - Error Microsoft OLE DB Provider for ODBC Drivers error '80040e07' [Microsoft]
        
        [ODBC SQL Server Driver][SQL Server]Syntax error converting the nvarchar value 'Microsoft SQL Server 2000 - 8.00.760 (Intel X86)
        
        Dec 17 2002 14:22:05 Copyright (c) 1988-2003 Microsoft Corporation Standard Edition on Windows NT 5.2 (Build 3790: Service Pack 1)' to a column of data type int. /process_login.asp, line 35
        
        **Listagem 15**. Erro que retorna a versão do SQL Server e do sistema operacional
        
        Esta mensagem de erro é devido à tentativa de conversão da variável global @@VERSION em um tipo de dado numérico, fato que acontece porque a primeira coluna da tabela “USERS” é numérica.
        
        Esta técnica pode ser utilizada para leitura de qualquer valor em qualquer tabela no banco de dados. Para obter nomes de usuários e senhas, o usuário mal intencionado pode obter o nome dos usuários a partir da tabela “USERS” utilizando o comando exibido na **Listagem 16.**
        
        Username: ' union select min(username),1,1,1 from users where username > 'a'--
        
        - - Error Microsoft OLE DB Provider for ODBC Drivers error '80040e07'
        
        [Microsoft][ODBC SQL Server Driver] [SQL Server]Syntax error converting the varchar value 'admin' to a column of data type int.
        
        /process_login.asp, line 35
        
        **Listagem 16**. Erro que retorna o nome do primeiro usuário cadastrado na tabela “USERS”
        
        O que este comando faz é selecionar o menor nome de usuário que é maior do que ‘a’ e depois tenta convertê-lo para um tipo de dado numérico. Com isso, nosso usuário mal intencionado já sabe que a conta “ADMIN” existe. Agora ele pode navegar entre as linhas da tabela substituindo cada novo nome de usuário descoberto na cláusula WHERE (ver **Listagem 17**).
        
        Username: ' union select min(username),1,1,1 from users where username > 'admin'--
        
        - - Error Microsoft OLE DB Provider for ODBC Drivers error '80040e07' [Microsoft][ODBC SQL Server Driver]
        
        [SQL Server]Syntax error converting the varchar value 'chris' to a column of data type int.
        
        /process_login.asp, line 35
        
        **Listagem 17**. Erro que retorna o nome do segundo usuário cadastrado na tabela “USERS”
        
        Uma vez descobertos todos os usuários cadastrados, nosso usuário mal intencionado pode ampliar seus horizontes descobrindo senhas, conforme exibido na **Listagem 18.**
        
        Username: ' union select password,1,1,1 from users where username = 'admin'--
        
        - - Error Microsoft OLE DB Provider for ODBC Drivers error '80040e07' [Microsoft][ODBC SQL Server Driver]
        
        [SQL Server]Syntax error converting the varchar value 'r00tr0x!' to a column of data type int.
        
        /process_login.asp, line 35
        
        **Listagem 18**. Erro que retorna a senha do usuário “ADMIN”
        
        Uma forma mais elegante de obter estas informações é concatenar todos os usuários e senhas em uma única seqüência de caracteres e então tentar converter esta seqüência para um tipo de dado numérico. E isso mostra uma outra informação, a de que comandos T-SQL podem ser concatenados na mesma linha sem que seu resultado seja alterado. A **Listagem 19** mostra um exemplo disso.
        
        Username: '; begin declare @ret varchar(8000) set @ret=':' select @ret=@ret+' '+ username +'/'+ password from users where username>@ret select @ret as ret into foo end--
        
        Username: ' union select ret,1,1,1 from foo--
        
        - - Error
        
        Microsoft OLE DB Provider for ODBC Drivers error '80040e07' [Microsoft][ODBC SQL Server Driver] [SQL Server]Syntax error converting the varchar value ': admin/r00tr0x! guest/guest chris/password fred/sesame' to a column of data type int. /process_login.asp, line 35
        
        **Listagem 19**. Erro que retorna a todos os usuários e as senhas da tabela “USERS”
        
        Na **Listagem 19** o usuário mal intencionado precisou executar dois comandos: o primeiro cria uma tabela “FOO” e insere na coluna “RET” uma seqüência de caracteres. Se o usuário não possuir privilégios para criação de uma tabela permanente, existe a opção de criar uma temporária. O passo seguinte foi tentar converter esta string em um valor numérico.
        
        Estes exemplos dão uma visão superficial da flexibilidade desta técnica. De modo geral, quanto mais detalhada for a mensagem de erro que o usuário mal intencionado recebe, mais fácil o seu trabalho.
        
        ### **Obtendo mais acessos**
        
        Uma vez que o usuário mal intencionado adquiriu o controle da estrutura dos objetos do banco de dados, o próximo passo é utilizar os direitos inerentes ao usuário para controle da rede, o que pode ser feito de várias formas:
        
        1. A extended stored-procedure XP_CMDSHELL pode ser utilizada para processar comados no contexto do usuário que está executando o serviço do SQL Server no servidor de banco de dados;
        2. A extended stored procedure XP_REGREAD pode ser utilizada na leitura de chaves do registro e potencialmente o SAM (Security Accounts Manager) – caso o SQL Server esteja sendo executado com Local System Account;
        3. Pela utilização de outras extended stored procedure no servidor;
        4. Através a criação de extended stored procedures para execução de aplicativos no contexto do processo do SQL Server;
        5. O comando BULK INSERT pode ser utilizado na leitura de qualquer arquivo no servidor;
        6. O comando BCP pode ser utilizado para criação de arquivos arbitrários no servidor;
        7. As rotinas sp_OACreate e sp_OAGetProperty podem ser utilizadas para criação de aplicações do tipo Ole Automation (ActiveX) que podem executar tudo o que um script ASP pode executar.
        
        Estes são alguns exemplos de ataques mais comuns. É bastante provável que um usuário mal intencionado possa utilizar um cenário não mencionado aqui. Estes cenários foram listados como os mais óbvios em um ataque a um servidor SQL Server através de SQL Injection. Vamos analisar esses pontos.
        
        ### **Ataque a comandos do sistema operacional com XP_CMDSHELL**
        
        Extended stored procedures são essencialmente DDLs (Dynamic Link Libraries) compiladas que fazem uso de uma convenção de chamada específica do SQL Server para a execução de suas funções. Elas permitem que aplicações SQL Server tenham acesso a todo o potencial de programação do C/C++ e são um recurso extremamente útil. Um grande número de extended stored procedures já vem embutidas no SQL Server e realizam várias tarefas, como envio de e-mails e interação com o registro do servidor.
        
        XP_CMDSHELL é uma das extended stored procedures que já vem com o SQL Server e que permite a execução de linhas de comandos da mesma forma que executamos no Command Prompt do Windows. A **Listagem 20** mostra um exemplo da execução desta rotina com seu resultado.
        
        [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeFvR6Eg7PgNiAA5q0DQzBGYz58z6_9ICQdvQm8EnAqiuK6OrDQ682GqjQP8uWRx1jwm_obP4OLU22QycsG4w9NHQAkHo9cpavTW6-aMZMOTB7U3C5PQvMEamdlHncze6Iao3FuPg?key=ZrbJaXHcJo6QVB-SCb6bUjpB)
        
        **Listagem 20**. Exemplo de execução da rotina “XP_CMDSHELL”
        
        exec master..xp_cmdshell 'net1 user'
        
        output --------------------------------------------------------------
        
        NULL
        
        User accounts for NULL --------------------------------------------------------------
        
        Administrator ASPNET Guest
        
        IUSR_LOKI IWAM_LOKI SQLDebugger
        
        SUPPORT_388945a0 WADM_LOKI
        
        The command completed with one or more errors.
        
        NULL
        
        NULL
        
        (10 row(s) affected)
        
        **Listagem 21**. Exemplo de execução da rotina “XP_CMDSHELL” para listar todos os usuários do servidor
        
        Como o servidor SQL está sempre sendo executado com uma conta de domínio ou como “Local System Account”, o usuário mal intencionado pode fazer um grande estrago utilizando esta rotina (ver **Nota 2**).
        
        **Nota 2**: “XP_CMDSHELL” no SQL Server 2005
        
        O SQL Server 2005 já vem com a extended stored procedure “XP_CMDSHELL” desabilitada diferentemente do SQL Server 2000, que vem com ela habilitada.
        
        ### **Ataque ao registro com XP_REGREAD**
        
        Um outro conjunto de extended stored procedures que já vem embutidas no SQL Server são funções que começam com “XP_REG”. Elas são as seguintes:
        
        - xp_regaddmultistring
        - xp_regdeletekey
        - xp_regdeletevalue
        - xp_regenumkeys
        - xp_regenumvalues
        - xp_regread
        - xp_regremovemultistring
        - xp_regwrite
        
        Estas rotinas podem ser utilizadas, por exemplo, para determinar todos os null-session shares do servidor (ver **Nota 3**), conforme mostra a **Listagem 22**.
        
        exec master..xp_regread HKEY_LOCAL_MACHINE,
        
        'SYSTEM\CurrentControlSet\Services\lanmanserver\parameters', 'nullsessionshares'
        
        Value Data
        
        - ----------------------------- --------- ----- nullsessionshares - Item #1 COMCFG NULL
        
        nullsessionshares - Item #2 DFS
        
        (2row(s)affected)
        
        **Listagem 22**. Exemplo de execução da rotina “XP_REGREAD” para listar todos null-session shares do servidor
        
        **Nota 3**: Null Session Shares
        
        Null Session Shares são recursos compartilhados utilizados por aplicações que não são executadas no contexto do usuário-por exemplo aplicações executadas como Local System Account.
        
        Através destas rotinas, o usuário mal intencionado pode alterar configurações de um determinado serviço para que ele seja inicializado quando for realizado um boot no servidor.
        
        ### **Ataques através a outras extended stored procedures**
        
        A extended stored procedure XP_SERVICECONTROL permite que o usuário inicialize, finalize, pare ou continue um determinado serviço. A **Listagem 23** mostra exemplos dessa rotina.
        
        exec master..xp_servicecontrol 'start', 'schedule'
        
        exec master..xp_servicecontrol 'start', 'server'
        
        **Listagem 23**. Exemplo de execução da rotina “XP_SERVICECONTROL” para iniciar serviços no servidor
        
        Outras extended stored procedures podem ser utilizadas em ataques:
        
        - XP_ENUMDSN (lista os dispositivos ODBC criados no servidor);
        - XP_LOGINCONFIG (exibe o modo de segurança do servidor);
        - XP_MAKECAB (permite que o usuário crie arquivos compactados no servidor);
        - XP_NTSEC_ENUMDOMAINS (exibe os domínios que o servidor tem acesso);
        - XP_TERMINATE_PROCESS (finaliza um processo com um PID específico).
        
        ### **Ataque com criação de extended stored procedures**
        
        A API das extended stored procedures é relativamente simples, assim como não é muito difícil criar uma DLL que contenha código malicioso. Pode-se enviar uma DLL para um servidor SQL Server utilizando linhas de comando Command Prompt, assim como pode-se utilizar mecanismos de comunicação que podem ser automatizados como downloads HTTP ou scripts FTP.
        
        Uma vez que a DLL esta presente no servidor onde o SQL Server esta instalado, o usuário malicioso pode criar, executar, e excluir uma extended stored procedure utilizando os comandos presentes na **Listagem 24**.
        
        use master
        
        go
        
        sp_addextendedproc 'xp_webserver', 'c:\temp\xp_foo.dll'
        
        go
        
        exec xp_webserver go sp_dropextendedproc 'xp_webserver'
        
        go
        
        **Listagem 24**. Exemplo de criação, execução e exclusão de uma extended stored procedure
        
        ### **Ataque pela leitura de arquivos-texto com BULK INSERT**
        
        Através do uso do comando BULK INSERT é possível atualizar uma tabela a partir de um arquivo-texto. Assim, o usuário malicioso pode, por exemplo, inserir o conteúdo de um arquivo qualquer do seu servidor em uma tabela e ler o seu conteúdo utilizando qualquer uma das técnicas de mensagens de erro comentadas anteriormente. A **Listagem 25** mostra um exemplo disso.
        
        create table foo( line varchar(8000) )
        
        go
        
        bulk insert foo from 'c:\inetpub\wwwroot\process_login.asp' gov
        
        **Listagem 25**. Exemplo de uso do “BULK INSERT”
        
        ### **Ataque que resulta na criação de arquivos com o comando BCP**
        
        O usuário mal intencionado pode facilmente criar arquivos no servidor utilizando uma técnica inversa à técnica ilustrada anteriormente. Essa técnica, entretanto, requer a utilização de um utilitário de linha de comando nativo do SQL Server: o BCP (Bulk Copy Program).
        
        Como o BCP acessa o banco de dados através de um processo externo ao SQL Server, é necessário um usuário válido para ativar a conexão. Se o servidor estiver configurado para segurança integrada, o trabalho fica ainda mais fácil. Um exemplo da utilização do BCP pode ser visto na **Listagem 26**.
        
        bcp "SELECT * FROM test..foo" queryout c:\inetpub\wwwroot\runcommand.asp -c -Slocalhost -Usa
        
        - Pfoobar
        
        **Listagem 26**. Exemplo de uso do “BCP”
        
        Os parâmetros utilizados aqui são, “-S” para o nome do servidor, “-U” para o nome do usuário SQL e “-P” para a senha deste usuário no servidor SQL. Para utilizar segurança integrada, basta substituir os parâmetros -U e -P por -E.
        
        ### **Criação de scripts ActiveX: sp_OACreate e sp_OAGetProperty**
        
        Várias extended stored procedures que já vêm com o SQL Server permitem a criação de scripts ActiveX no SQL Server. Estes scripts têm a mesma funcionalidade de scripts que são executados no contexto do Windows Scripting Host ou de scripts ASP - eles normalmente são escritos em VBScript ou JavaScript, e podem criar objetos e interagir com eles. Um script desses escrito em Transact-SQL pode fazer tudo o que um script ASP ou WSH pode fazer. O exemplo da **Listagem 27** utiliza o objeto “WSCRIPT.SHELL” para criar uma instancia do aplicativo Notepad.
        
        - - wscript.shell example
        
        declare @o int
        
        exec sp_oacreate 'wscript.shell', @o out
        
        exec sp_oamethod @o, 'run', NULL, 'notepad.exe'
        
        **Listagem 27**. Exemplo de uso das rotinas sp_OACreate e sp_OAGetProperty para executar o Notepad
        
        ### **SQL Injection: como prevenir**
        
        ### **Valide sempre os dados digitados pelo usuário**
        
        A validação dos dados digitados pelo usuário pode ser um tema aparentemente inofensivo, mas é um dos principais motivos pelo qual se faz possível ataques SQL Injection. Para endereçá-lo, podemos adotar as seguintes abordagens:
        
        1. Rejeitar dados que são conhecidamente inválidos;
        2. Aceitar somente dados que são conhecidamente válidos.
        
        A abordagem (1) possui como principal problema o fato do desenvolvedor não estar necessariamente ciente do que sejam dados inválidos que devem ser modificados, visto que novas formas de “dados inválidos” são sempre descobertos.
        
        A abordagem (2) é a melhor opção e é a que deve ser utilizada. Um exemplo de implementação desta abordagem pode ser visto na **Listagem 28** e poderia ser implementado no código da **Listagem 2** exibido no inicio deste artigo.
        
        function validate( input )
        
        goodchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        
        validate = true
        
        for i = 1 to len( input )
        
        c = mid( input, i, 1 )
        
        if ( InStr( goodchars, c ) = 0 ) then
        
        validate = false
        
        exit function
        
        end if
        
        next
        
        end function
        
        **Listagem 28**. Exemplo de função de validação que só permite letras e números
        
        ### **Crie usuários com permissões adequadas**
        
        Nunca se deve conectar no [servidor SQL Server](https://www.devmedia.com.br/monitorando-uma-instancia-sql-server/29449) com um usuário genérico que seja proprietário do banco ou administrador do servidor. Este item é o segundo mais importante para a prevenção de ataques SQL Injection.
        
        ### **Nunca retorne as mensagens do servidor SQL para o usuário**
        
        Não retorne mensagens de erro do banco de dados diretamente para o usuário. Estas mensagens podem revelar informações importantes sobre seu servidor conforme vimos anteriormente.
        
        ### **Remova objetos que não serão utilizados**
        
        Muitas extended stored procedures podem ser removidas sem causar impacto para o servidor SQL Server. Se você não se sente seguro a pondo de remover uma determinada expended stored procedure, certifique-se de que nenhum usuário possa utilizá-la.
        
        Remova os bancos de dados de exemplo: PUBS e NORTHWIND.
        
        ### **Habilite logs de segurança no servidor**
        
        Habilite os logs de segurança no servidor que achar necessário e certifique-se de que eles são verificados periodicamente. Você pode, por exemplo, habilitar o log das tentativas de login que foram rejeitadas pelo servidor SQL.
        
        ### **Finalizando o papo sobre SQL Injection**
        
        Neste artigo vimos que SQL Injection é uma classe de ataque onde o invasor pode manipular consultas criadas pela aplicação. Vimos também através de exemplos práticos que os dois principais fatores que contribuem para este tipo de ataque são a falta de validação dos dados digitados pelo usuário e a utilização de um usuário com altos privilégios pela aplicação. Com esses dados fica bem mais fácil entender a potencialidade dos ataques SQL Injection e, como medida preventiva, trabalhar para que sua aplicação não esteja sujeita a esse tipo de vulnerabilidade.
        
    - Fonte 3 - [gocache](https://gocache.com.br/en/seguranca/o-que-e-sql-injection-para-iniciantes/)
        
        # **O que é SQL Injection? Para iniciantes**
        
        16 de February de 2021/in [Security](https://gocache.com.br/en/categoria/seguranca/)
        
        A injeção de SQL (**ou SQL injection**) é uma vulnerabilidade de segurança da web que permite que um invasor interfira nas consultas que um aplicativo faz ao seu banco de dados. Geralmente, permite que um invasor visualize dados que normalmente ele não é capaz de recuperar. Isso pode incluir dados pertencentes a outros usuários ou quaisquer outros dados que o próprio aplicativo é capaz de acessar. Em muitos casos, um invasor pode modificar ou excluir esses dados, causando alterações persistentes no conteúdo ou comportamento do aplicativo.
        
        Em algumas situações, um invasor pode escalar um ataque de injection de SQL para comprometer o servidor subjacente ou outra infraestrutura de back-end, ou realizar um ataque de negação de serviço.
        
        ### **Qual é o impacto de um ataque de SQL Injection bem-sucedido?**
        
        Um ataque de SQL injection bem-sucedido pode resultar em acesso não autorizado a dados confidenciais, como senhas, detalhes de cartão de crédito ou informações pessoais do usuário. Muitas violações de dados de alto perfil nos últimos anos foram resultado de ataques de SQL injection, levando a danos à reputação e multas regulatórias. Em alguns casos, um invasor pode obter um backdoor persistente nos sistemas de uma organização, levando a um comprometimento de longo prazo que pode passar despercebido por um longo período.
        
        ### **Exemplos de SQL Injection**
        
        Há uma grande variedade de vulnerabilidades, ataques e técnicas de SQL Injection que surgem em diferentes situações. Alguns exemplos comuns de injeção de SQL incluem:
        
        - **Recuperando dados ocultos,** onde você pode modificar uma consulta SQL para retornar resultados adicionais.
        - **Subvertendo a lógica do aplicativo,** onde você pode alterar uma consulta para interferir com a lógica do aplicativo.
        - **Ataques UNION**, onde você pode recuperar dados de diferentes tabelas de banco de dados.
        - **Examinando o banco de dados**, onde você pode extrair informações sobre a versão e estrutura do banco de dados.
        - **Injeção cega de SQL**, onde os resultados de uma consulta que você controla não são retornados nas respostas do aplicativo.
        
        ### **Recuperando dados ocultos**
        
        Considere um aplicativo de compras que exibe produtos em diferentes categorias. Quando o usuário clica na categoria Presentes, o navegador solicita o URL: https://insecure-website.com/products?category=Gifts
        
        Isso faz com que o aplicativo faça uma consulta SQL para recuperar detalhes dos produtos relevantes do banco de dados:
        
        SELECIONE * DE produtos ONDE categoria = ‘Presentes’ E lançados = 1
        
        Esta consulta SQL pede ao banco de dados para retornar:
        
        - todos os detalhes (*)
        - da tabela de produtos
        - onde a categoria é Presentes
        
        e lançado é 1.
        
        A restrição lançado = 1 está sendo usada para ocultar produtos que não foram lançados.
        
        Para produtos não lançados, presumivelmente lançado = 0.
        
        O aplicativo não implementa nenhuma defesa contra ataques de injeção de SQL, então um invasor pode construir um ataque como: https://insecure-website.com/products?category=Gifts’–
        
        Isso resulta na consulta SQL:
        
        SELECIONE * DE produtos ONDE categoria = ‘Presentes’ – ‘E lançado = 1
        
        O principal aqui é que a sequência de dois traços - é um indicador de comentário em SQL e significa que o resto da consulta é interpretado como um comentário. Isso remove efetivamente o restante da consulta, de forma que não inclui mais E lançado = 1. Isso significa que todos os produtos são exibidos, incluindo os não lançados.
        
        Indo além, um invasor pode fazer com que o aplicativo exiba todos os produtos em qualquer categoria, incluindo categorias que ele não conhece: https://insecure-website.com/products?category=Gifts’+OR+1=1– Isso resulta na consulta SQL:
        
        SELECIONE * DE produtos ONDE categoria = ‘Presentes’ OU 1 = 1– ‘E lançado = 1
        
        A consulta modificada retornará todos os itens em que a categoria seja Presentes ou 1 é igual a 1. Como 1 = 1 é sempre verdadeiro, a consulta retornará todos os itens.
        
        ### **Subvertendo a lógica do aplicativo**
        
        Considere um aplicativo que permite que os usuários façam login com um nome de usuário e senha. Se um usuário enviar o nome de usuário wiener e a senha  bluecheese, o aplicativo verifica as credenciais executando a seguinte consulta SQL:
        
        SELECIONE * DE usuários ONDE o usuário = ‘wiener’ E a senha = ‘bluecheese’
        
        Se a consulta retornar os detalhes de um usuário, o login foi bem-sucedido. Caso contrário, é rejeitado.
        
        Aqui, um invasor pode fazer login como qualquer usuário sem uma senha, simplesmente usando a sequência de comentário SQL -para remover a verificação de senha da cláusula de consulta ONDE. Por exemplo, enviar o nome de usuárioadministrador’–e uma senha em branco resulta na seguinte consulta:
        
        SELECIONE * DE usuários ONDE o usuário = ‘administrador’ – ‘E senha =’ ‘
        
        Esta consulta retorna o usuário cujo nome de usuário é administrador e loga com sucesso o invasor como esse usuário.
        
        ### **Recuperando dados de outras tabelas de banco de dados**
        
        Nos casos em que os resultados de uma consulta SQL são retornados nas respostas do aplicativo, um invasor pode aproveitar uma vulnerabilidade de injeção SQL para recuperar dados de outras tabelas no banco de dados. Isso é feito usando a  palavra-chave UNION, que permite executar uma  consulta SELECIONE adicional e acrescenta os resultados à consulta original.
        
        Por exemplo, se um aplicativo executa a seguinte consulta contendo a entrada do usuário “Presentes”:
        
        SELECIONE o nome, a descrição DOS produtos ONDE categoria = ‘Presentes’
        
        então um invasor pode enviar a entrada:
        
        ‘UNION SELECIONE nome de usuário, senha DE usuários–
        
        Isso fará com que o aplicativo retorne todos os nomes de usuário e senhas junto com os nomes e descrições dos produtos.
        
        ### **Examinando o banco de dados**
        
        Após a identificação inicial de uma vulnerabilidade de injeção de SQL, geralmente é útil obter algumas informações sobre o próprio banco de dados. Muitas vezes, essas informações podem abrir caminho para uma maior exploração.
        
        Você pode consultar os detalhes da versão do banco de dados. A maneira como isso é feito depende do tipo de banco de dados, portanto, você pode inferir o tipo de banco de dados de qualquer técnica que funcione. Por exemplo, no Oracle você pode executar:
        
        SELECT * FROM v$version
        
        Você também pode determinar quais tabelas de banco de dados existem e quais colunas elas contêm. Por exemplo, na maioria dos bancos de dados, você pode executar a seguinte consulta para listar as tabelas:
        
        SELECT * FROM information_schema.tables
        
        ### **Vulnerabilidades cegas de SQL Injection**
        
        Muitas instâncias de injeção de SQL são vulnerabilidades cegas. Isso significa que o aplicativo não retorna os resultados da consulta SQL ou os detalhes de quaisquer erros de banco de dados em suas respostas. Vulnerabilidades cegas ainda podem ser exploradas para acessar dados não autorizados, mas as técnicas envolvidas são geralmente mais complicadas e difíceis de executar.
        
        Dependendo da natureza da vulnerabilidade e do banco de dados envolvido, as seguintes técnicas podem ser usadas para explorar vulnerabilidades cegas de injeção SQL:
        
        - Você pode alterar a lógica da consulta para acionar uma diferença detectável na resposta do aplicativo, dependendo da verdade de uma única condição. Isso pode envolver a injeção de uma nova condição em alguma lógica booleana ou o disparo condicional de um erro, como divisão por zero.
        - Você pode acionar condicionalmente um atraso de tempo no processamento da consulta, permitindo inferir a verdade da condição com base no tempo que o aplicativo leva para responder.
        - Você pode acionar uma interação de rede fora de banda, usando técnicas OAST. Esta técnica é extremamente poderosa e funciona em situações onde as outras técnicas não funcionam. Frequentemente, você pode exfiltrar dados diretamente por meio do canal fora de banda, por exemplo, colocando os dados em uma pesquisa DNS de um domínio que você controla.
        
        ### **Como detectar vulnerabilidades de SQL Injection**
        
        A maioria das vulnerabilidades de injeção de SQL podem ser encontradas de forma rápida e confiável usando o Burp Suite scanner de vulnerabilidade da web.
        
        A injeção de SQL pode ser detectada manualmente usando um conjunto sistemático de testes em cada ponto de entrada no aplicativo. Isso normalmente envolve:
        
        - Enviar o caractere de aspas simples’e procurar por erros ou outras anomalias.
            
            Enviar alguma sintaxe específica de SQL que avalia o valor base (original) do ponto de entrada e um valor diferente e procurar por diferenças sistemáticas nas respostas do aplicativo resultante.
            
        - Enviar condições booleanas, como OR 1=1 e OR 1=2, e procurar diferenças nas respostas do aplicativo.
        - Enviar cargas úteis projetadas para disparar atrasos quando executados em uma consulta SQL e procurar diferenças no tempo necessário para responder.
        - Enviar cargas OAST projetadas para acionar uma interação de rede fora de banda quando executado em uma consulta SQL e monitorar todas as interações resultantes.
        
        ### **SQL Injection em diferentes partes da consulta**
        
        A maioria das vulnerabilidades de injeção de SQL surgem dentro da cláusula ONDE de uma consulta SELECIONE.
        
        Esse tipo de injeção de SQL é geralmente bem conhecido por testadores experientes.
        
        Mas as vulnerabilidades de injeção de SQL podem, em princípio, ocorrer em qualquer local dentro da consulta e em diferentes tipos de consulta. Os outros locais mais comuns onde a injeção de SQL surge são:
        
        - Em declarações de ATUALIZAR, dentro dos valores atualizados ou na cláusula ONDE.
        - Em declarações de INSERIR, dentro dos valores inseridos.
        - Em declarações de SELECIONE, dentro da tabela ou nome da coluna.
        - Em declarações de SELECIONE, dentro da cláusula ORDENAR POR.
        
        ### **SQL Injection de segunda ordem**
        
        A injeção SQL de primeira ordem surge quando o aplicativo obtém a entrada do usuário de uma solicitação HTTP e, no decorrer do processamento dessa solicitação, incorpora a entrada em uma consulta SQL de uma maneira insegura.
        
        Na injeção SQL de segunda ordem (também conhecida como injeção SQL armazenada), o aplicativo obtém a entrada do usuário de uma solicitação HTTP e a armazena para uso futuro. Isso geralmente é feito colocando a entrada em um banco de dados, mas nenhuma vulnerabilidade surge no ponto onde os dados são armazenados. Posteriormente, ao lidar com uma solicitação HTTP diferente, o aplicativo recupera os dados armazenados e os incorpora a uma consulta SQL de maneira insegura.
        
        A injeção SQL de segunda ordem geralmente surge em situações em que os desenvolvedores estão cientes das vulnerabilidades da injeção SQL e, portanto, lidam com segurança com o posicionamento inicial da entrada no banco de dados. Quando os dados são posteriormente processados, são considerados seguros, uma vez que foram previamente colocados na base de dados de forma segura. Nesse ponto, os dados são tratados de maneira insegura, porque o desenvolvedor erroneamente considera que eles são confiáveis.
        
        ### **Fatores específicos do banco de dados**
        
        Alguns recursos básicos da linguagem SQL são implementados da mesma maneira em plataformas de banco de dados populares, e muitas maneiras de detectar e explorar vulnerabilidades de injeção de SQL funcionam de forma idêntica em diferentes tipos de banco de dados.
        
        No entanto, também existem muitas diferenças entre os bancos de dados comuns. Isso significa que algumas técnicas para detectar e explorar injeção de SQL funcionam de maneira diferente em plataformas diferentes. Por exemplo:
        
        - Sintaxe para concatenação de strings.
        - Comentários.
        - Consultas em lote (ou empilhadas).
        - APIs específicas da plataforma.
        - Mensagens de erro.
        
        ### **Como evitar injeção de SQL**
        
        A maioria das instâncias de injeção de SQL pode ser evitada usando consultas parametrizadas (também conhecidas como instruções preparadas) em vez da concatenação de strings na consulta.
        
        O código a seguir é vulnerável à injeção de SQL porque a entrada do usuário é concatenada diretamente na consulta:
        
        Consulta string = “SELECIONE * DE produtos ONDE categoria = ‘” + input + “‘”;
        
        Instrução de instrução = connection.createStatement ();
        
        ResultSet resultSet = instrução.executeQuery (consulta);
        
        Este código pode ser facilmente reescrito de forma a evitar que a entrada do usuário interfira na estrutura da consulta:
        
        Instrução PreparedStatement =
        
        connection.prepareStatement (“SELECIONE * DOS produtos ONDE
        
        categoria =? “);
        
        instrução.setString (1, input);
        
        ResultSet resultSet = instrução.executeQuery ();
        
        As consultas parametrizadas podem ser usadas para qualquer situação em que a entrada não confiável apareça como dados dentro da consulta, incluindo a cláusula ONDE e valores em uma declaração INSERIR ou ATUALIZAR. Elas não podem ser usadas para lidar com entradas não confiáveis em outras partes da consulta, como nomes de tabela ou coluna, ou a cláusula ORDENAR POR.
        
        A funcionalidade do aplicativo que coloca dados não confiáveis nessas partes da consulta precisará adotar uma abordagem diferente, como valores de entrada permitidos na lista branca ou usando uma lógica diferente para fornecer o comportamento necessário.
        
        Para que uma consulta parametrizada seja eficaz na prevenção da injeção de SQL, a string usada na consulta deve ser sempre uma constante embutida no código e nunca deve conter dados variáveis de qualquer origem. Não fique tentado a decidir caso a caso se um item de dados é confiável e continue usando a concatenação de string dentro da consulta para casos considerados seguros.
        
        É muito fácil cometer erros sobre a possível origem dos dados ou que as alterações em outro código violem suposições sobre quais dados estão corrompidos.
        
    - Fonte 4 - [kaspersky](https://www.kaspersky.com.br/resource-center/definitions/sql-injection)
        
        # **O que é injeção de SQL? Definição e explicação**
        
        Os ataques de injeção de SQL são uma das vulnerabilidades mais antigas das aplicações da Web, que têm sido discutidas desde o final dos anos 90, mas ainda permanecem relevantes hoje. Este explicador descreve o que são, como funcionam e como você pode evitá-los.
        
        ## **Injeção de SQL: significado e definição**
        
        Uma injeção de SQL, às vezes abreviada como SQLi, é um tipo de vulnerabilidade em que um invasor usa uma parte do código SQL (Structured Query Language) para manipular um banco de dados e obter acesso a informações potencialmente valiosas. Esse é um dos tipos de ataque mais comuns e perigosos porque pode ser usado contra qualquer aplicação de Web ou site que utilize um banco de dados SQL (ou seja, a maioria deles).
        
        ## **Como funcionam os ataques de injeção de SQL?**
        
        Para entender a injeção de SQL, é importante saber o que é Structured Query Language (SQL). A SQL é uma linguagem de consulta usada em programação para acessar, modificar e excluir dados armazenados em bancos de dados relacionais. Como a grande maioria dos sites e aplicativos da Web depende de bancos de dados SQL, um ataque de injeção de SQL pode ter sérias consequências para as organizações.
        
        Uma consulta SQL é uma solicitação enviada a um banco de dados para que seja realizado algum tipo de atividade ou função, como consulta de dados ou execução de código SQL a ser realizada. Um exemplo é quando as informações de login são enviadas através de um formulário web para permitir o acesso de um usuário a um site. Normalmente, esse tipo de formulário da Web é projetado para aceitar somente alguns tipos específicos de dados, como um nome e/ou uma senha. Ao serem inseridas, essas informações são verificadas no banco de dados e, se corresponderem, o usuário terá permissão de acesso. Caso contrário, o acesso será negado.
        
        Possíveis problemas ocorrem porque a maioria dos formulários da Web não consegue impedir a entrada de informações adicionais. Os invasores podem explorar esse ponto fraco e usar caixas de entrada no formulário para enviar suas próprias solicitações ao banco de dados. Isso poderia permitir a realização de uma série de atividades mal-intencionadas, como roubo de dados confidenciais e manipulação de informações no banco de dados para seus próprios fins.
        
        Devido à predominância de sites e servidores que utilizam bancos de dados, as vulnerabilidades de injeção de SQL são um dos tipos mais antigos e comuns de ataque cibernético. A evolução da comunidade de hackers aumentou o risco desse tipo de ataque, principalmente com o surgimento de ferramentas para detectar e explorar a injeção de SQL. Disponibilizadas livremente por desenvolvedores de código aberto, essas ferramentas permitem que cibercriminosos conduzam ataques automáticos em questão de alguns minutos, permitindo que acessem qualquer tabela ou coluna do banco de dados apenas com um processo de clicar e atacar.
        
        ## **Sintomas da SQLi**
        
        Um ataque bem-sucedido de injeção de SQL pode não apresentar sintomas. No entanto, às vezes há indicações externas, que incluem:
        
        - Recebimento de um número excessivo de solicitações em um curto período. Por exemplo, você pode receber vários e-mails por meio do formulário de contato de sua página da Web.
        - Anúncios que redirecionam para sites suspeitos.
        - Pop-ups e mensagens de erro estranhos.
        
        ## **Tipos de injeção de SQL**
        
        Dependendo de como obtêm acesso aos dados de back-end e da extensão dos danos potenciais que causam, as injeções de SQL se enquadram em três categorias:
        
        **SQLi em banda:**
        
        Esse tipo de ataque de SQLi é simples para os invasores, pois eles usam o mesmo canal de comunicação para desencadear ataques e obter resultados. Esse tipo de ataque de SQLi tem duas subvariações:
        
        - **SQLi com base em erro:** o banco de dados gera uma mensagem de erro devido às ações do invasor. Com base nos dados gerados pelas mensagens de erro, o invasor coleta informações sobre a infraestrutura do banco de dados.
        - **SQLi com base em Union:** o invasor usa o operador UNION SQL para obter os dados desejados reunindo várias instruções select em uma única resposta HTTP.
        
        **SQLi de inferência (também conhecido como injeção de SQL cego):**
        
        Nesse tipo de SQLi, após enviar cargas de dados, os invasores usam os padrões de resposta e comportamento do servidor para obter mais informações sobre a estrutura dele. Os dados não são transferidos do banco de dados do site para o invasor. Portanto, o invasor não vê informações sobre o ataque em banda (essa é a origem do termo "SQLi cego"). O SQLi de inferência pode ser classificado em dois subtipos:
        
        - **SQLi com base em tempo:** os invasores enviam uma consulta SQL ao banco de dados, fazendo com que ele aguarde alguns segundos antes de responder à consulta como verdadeiro ou falso.
        - **SQLi booliano:** os invasores enviam uma consulta SQL ao banco de dados, permitindo que o aplicativo responda com a geração de um resultado verdadeiro ou falso.
        
        **SQLi fora de banda:**
        
        Esse tipo de ataque SQL ocorre em dois cenários:
        
        - Quando os invasores não conseguem usar o mesmo canal para desencadear o ataque e coletar informações; ou
        - Quando um servidor está muito lento ou instável para executar essas ações.
        
        ## **Impacto de ataques de injeção de SQL**
        
        Um ataque de injeção de SQL bem-sucedido pode acarretar sérias consequências a uma empresa. Isso ocorre porque um ataque de injeção de SQL pode:
        
        - **Expor dados confidenciais.** Os invasores podem recuperar dados, o que gera o risco de exposição de dados confidenciais armazenados no servidor SQL.
        - **Comprometer a integridade dos dados.** Os invasores podem alterar ou excluir informações de seu sistema.
        - **Comprometer a privacidade dos usuários.** Dependendo dos dados armazenados no servidor SQL, um ataque pode expor informações confidenciais dos usuários, como endereços, números de telefone e dados de cartões de crédito.
        - **Conceder a um invasor acesso de administrador a seu sistema.** Se um usuário de banco de dados tiver privilégios administrativos, um invasor poderá obter acesso ao sistema usando código mal-intencionado.
        - **Dar a um invasor acesso geral a seu sistema.** Se você usar comandos SQL fracos para verificar nomes de usuário e senhas, um invasor poderá obter acesso a seu sistema sem saber as credenciais de um usuário. Depois disso, o invasor poderá causar danos acessando e manipulando informações confidenciais.
        
        O custo de um ataque de injeção de SQL não é apenas financeiro: também pode envolver perda de confiança dos clientes e danos à reputação, caso sejam roubadas informações pessoais como nomes, endereços, números de telefone e dados de cartões de crédito. Quando a confiança do cliente é perdida, pode ser muito difícil reconquistá-la.
        
        ## **Exemplos de injeção de SQL**
        
        Ao longo dos anos, muitas organizações foram vítimas de SQLi. Estes são alguns exemplos de destaque:
        
        **Fortnite, 2019**Fortnite é um jogo on-line com mais de 350 milhões de usuários. Em 2019, [foi descoberta uma vulnerabilidade de injeção de SQL](https://www.vice.com/en/article/vba5nb/fornite-login-hack-epic-games-website) que poderia permitir que invasores acessassem contas de usuários. A vulnerabilidade foi corrigida.
        
        **Cisco, 2018**
        
        Em 2018, foi encontrada uma vulnerabilidade de injeção de SQL no Cisco Prime License Manager. A vulnerabilidade permitiu que invasores obtivessem acesso de shell aos sistemas nos quais o gerenciador de licenças foi implantado. Posteriormente, a Cisco corrigiu a vulnerabilidade.
        
        **Tesla, 2014**
        
        Em 2014, os pesquisadores de segurança anunciaram que conseguiram violar o site da Tesla usando injeção de SQL, obtendo privilégios administrativos e roubando dados dos usuários.
        
        ## **Perguntas frequentes sobre ataques de injeção de SQL**
        
        As perguntas mais frequentes sobre SQLi são:
        
        ### **O que é um ataque de injeção de SQL?**
        
        Um ataque de injeção de SQL usa código SQL mal-intencionado para manipulação de um banco de dados de back-end a fim de acessar informações privadas. As informações podem incluir dados confidenciais de empresas, listas de usuários ou detalhes de clientes. SQL é a abreviação de "structured query language", e às vezes a injeção de SQL é abreviada como SQLi.
        
        ### **O que a injeção de SQL faz?**
        
        Os ataques de injeção de SQL permitem que os invasores [falsifiquem](https://www.kaspersky.com.br/resource-center/definitions/spoofing) a identidade, alterem dados existentes, divulguem dados no sistema, destruam dados ou os tornem indisponíveis e se tornem administradores do servidor de banco de dados. Os ataques de injeção de SQL podem acarretar sérios danos às empresas, inclusive a perda da confiança dos clientes, caso dados confidenciais de usuários sejam violados.
        
        ### **Qual é a frequência dos ataques de injeção de SQL?**
        
        Por serem relativamente fáceis de implementar e terem uma grande recompensa potencial, os ataques de injeção de SQL não são raros. As estatísticas variam, mas é estimado que os ataques de injeção de SQL constituam a maioria dos ataques a aplicativos de software. Segundo o Open Web Application Security Project, os ataques de injeção, que incluem injeções de SQL, foram [o terceiro risco de segurança mais sério a aplicativos da Web em 2021](https://owasp.org/Top10/A03_2021-Injection/).
        
        ## **Como evitar ataques de injeção de SQL**
        
        Para empresas preocupadas com a prevenção da injeção de SQL, os princípios-chave para defender sites e aplicativos da Web são:
        
        **Treinamento da equipe:**Promova a conscientização da equipe responsável pela aplicação da Web sobre os riscos decorrentes de SQLi e ministre o treinamento necessário, com base em função, para todos os usuários.
        
        **Mantenha o controle da entrada dos usuários:**Qualquer entrada dos usuários em uma consulta SQL gera riscos. Até que ela seja verificada, lide com a entrada de usuários autenticados e/ou internos da mesma forma como lida com a entrada pública. Dê às contas que se conectam ao banco de dados SQL apenas os privilégios mínimos necessários. Como prática padrão, use listas de permissões em vez de listas de bloqueio para verificar e filtrar a entrada dos usuários.
        
        **Use as versões mais recentes:**é importante usar a versão mais recente do ambiente de desenvolvimento para maximizar a proteção, pois as versões mais antigas podem não ter recursos de segurança atualizados. Instale o software e os patches de segurança mais recentes quando estiverem disponíveis.
        
        **Verifique continuamente aplicações da Web:**
        
        Use ferramentas abrangentes de gerenciamento de desempenho de aplicações. A verificação regular de aplicações da Web identificará e tratará de possíveis vulnerabilidades antes que elas causem danos sérios.
        
        **Use um firewall:**um [firewall](https://www.kaspersky.com.br/resource-center/definitions/firewall) de aplicação da Web (WAF) é frequentemente usado para filtrar SQLi, bem como outras ameaças on-line. Um WAF conta com uma lista grande e atualizada de assinaturas para filtrar consultas SQL mal-intencionadas. Normalmente, a lista contém assinaturas para lidar com vetores de ataque específicos e é corrigida regularmente quando há vulnerabilidades recém-descobertas.
        
    - Fonte 5 - [portswigger](https://portswigger.net/web-security/sql-injection)
        
        **SQL injection**
        
        In this section, we explain:
        
        - What SQL injection (SQLi) is.
        - How to find and exploit different types of SQLi vulnerabilities.
        - How to prevent SQLi.
        
        [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdEptst50WiBXRsxam0J4YcV9behBV6h22ZVEyNjDF1eT46LA8t2-fCQptMS6Vy7QWgBp4lkwquAfcqWJqob2Z21ZA19XEsK6TwAqPHbS03zeuMnDFGf3OEk7DAqE8gynpLwWjhmA?key=ZrbJaXHcJo6QVB-SCb6bUjpB)
        
        **Labs**
        
        If you're familiar with the basic concepts behind SQLi vulnerabilities and want to practice exploiting them on some realistic, deliberately vulnerable targets, you can access labs in this topic from the link below.
        
        - [View all SQL injection labs](https://portswigger.net/web-security/all-labs#sql-injection)
        
        ## **What is SQL injection (SQLi)?**
        
        SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. This can allow an attacker to view data that they are not normally able to retrieve. This might include data that belongs to other users, or any other data that the application can access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application's content or behavior.
        
        In some situations, an attacker can escalate a SQL injection attack to compromise the underlying server or other back-end infrastructure. It can also enable them to perform denial-of-service attacks.
        
        ## **What is the impact of a successful SQL injection attack?**
        
        A successful SQL injection attack can result in unauthorized access to sensitive data, such as:
        
        - Passwords.
        - Credit card details.
        - Personal user information.
        
        SQL injection attacks have been used in many high-profile data breaches over the years. These have caused reputational damage and regulatory fines. In some cases, an attacker can obtain a persistent backdoor into an organization's systems, leading to a long-term compromise that can go unnoticed for an extended period.
        
        ## **How to detect SQL injection vulnerabilities**
        
        You can detect SQL injection manually using a systematic set of tests against every entry point in the application. To do this, you would typically submit:
        
        - The single quote character ' and look for errors or other anomalies.
        - Some SQL-specific syntax that evaluates to the base (original) value of the entry point, and to a different value, and look for systematic differences in the application responses.
        - Boolean conditions such as OR 1=1 and OR 1=2, and look for differences in the application's responses.
        - Payloads designed to trigger time delays when executed within a SQL query, and look for differences in the time taken to respond.
        - OAST payloads designed to trigger an out-of-band network interaction when executed within a SQL query, and monitor any resulting interactions.
        
        Alternatively, you can find the majority of SQL injection vulnerabilities quickly and reliably using Burp Scanner.
        
        ## **SQL injection in different parts of the query**
        
        Most SQL injection vulnerabilities occur within the WHERE clause of a SELECT query. Most experienced testers are familiar with this type of SQL injection.
        
        However, SQL injection vulnerabilities can occur at any location within the query, and within different query types. Some other common locations where SQL injection arises are:
        
        - In UPDATE statements, within the updated values or the WHERE clause.
        - In INSERT statements, within the inserted values.
        - In SELECT statements, within the table or column name.
        - In SELECT statements, within the ORDER BY clause.
        
        ## **SQL injection examples**
        
        There are lots of SQL injection vulnerabilities, attacks, and techniques, that occur in different situations. Some common SQL injection examples include:
        
        - [Retrieving hidden data](https://portswigger.net/web-security/sql-injection#retrieving-hidden-data), where you can modify a SQL query to return additional results.
        - [Subverting application logic](https://portswigger.net/web-security/sql-injection#subverting-application-logic), where you can change a query to interfere with the application's logic.
        - [UNION attacks](https://portswigger.net/web-security/sql-injection/union-attacks), where you can retrieve data from different database tables.
        - [Blind SQL injection](https://portswigger.net/web-security/sql-injection/blind), where the results of a query you control are not returned in the application's responses.
        
        ## **Retrieving hidden data**
        
        Imagine a shopping application that displays products in different categories. When the user clicks on the **Gifts** category, their browser requests the URL:
        
        https://insecure-website.com/products?category=Gifts
        
        This causes the application to make a SQL query to retrieve details of the relevant products from the database:
        
        SELECT * FROM products WHERE category = 'Gifts' AND released = 1
        
        This SQL query asks the database to return:
        
        - all details (*)
        - from the products table
        - where the category is Gifts
        - and released is 1.
        
        The restriction released = 1 is being used to hide products that are not released. We could assume for unreleased products, released = 0.
        
        The application doesn't implement any defenses against SQL injection attacks. This means an attacker can construct the following attack, for example:
        
        https://insecure-website.com/products?category=Gifts'--
        
        This results in the SQL query:
        
        SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
        
        Crucially, note that -- is a comment indicator in SQL. This means that the rest of the query is interpreted as a comment, effectively removing it. In this example, this means the query no longer includes AND released = 1. As a result, all products are displayed, including those that are not yet released.
        
        You can use a similar attack to cause the application to display all the products in any category, including categories that they don't know about:
        
        https://insecure-website.com/products?category=Gifts'+OR+1=1--
        
        This results in the SQL query:
        
        SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
        
        The modified query returns all items where either the category is Gifts, or 1 is equal to 1. As 1=1 is always true, the query returns all items.
        
        ### **Warning**
        
        Take care when injecting the condition OR 1=1 into a SQL query. Even if it appears to be harmless in the context you're injecting into, it's common for applications to use data from a single request in multiple different queries. If your condition reaches an UPDATE or DELETE statement, for example, it can result in an accidental loss of data.
        
        **LAB**
        
        APPRENTICE[**SQL injection vulnerability in WHERE clause allowing retrieval of hidden data**](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)
        
        ## **Subverting application logic**
        
        Imagine an application that lets users log in with a username and password. If a user submits the username wiener and the password bluecheese, the application checks the credentials by performing the following SQL query:
        
        SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'
        
        If the query returns the details of a user, then the login is successful. Otherwise, it is rejected.
        
        In this case, an attacker can log in as any user without the need for a password. They can do this using the SQL comment sequence -- to remove the password check from the WHERE clause of the query. For example, submitting the username administrator'-- and a blank password results in the following query:
        
        SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
        
        This query returns the user whose username is administrator and successfully logs the attacker in as that user.
        
        **LAB**
        
        APPRENTICE[**SQL injection vulnerability allowing login bypass**](https://portswigger.net/web-security/sql-injection/lab-login-bypass)
        
        ## **Retrieving data from other database tables**
        
        In cases where the application responds with the results of a SQL query, an attacker can use a SQL injection vulnerability to retrieve data from other tables within the database. You can use the UNION keyword to execute an additional SELECT query and append the results to the original query.
        
        For example, if an application executes the following query containing the user input Gifts:
        
        SELECT name, description FROM products WHERE category = 'Gifts'
        
        An attacker can submit the input:
        
        ' UNION SELECT username, password FROM users--
        
        This causes the application to return all usernames and passwords along with the names and descriptions of products.
        
        ### **Read more**
        
        - [SQL injection UNION attacks](https://portswigger.net/web-security/sql-injection/union-attacks)
        
        ## **Blind SQL injection vulnerabilities**
        
        Many instances of SQL injection are blind vulnerabilities. This means that the application does not return the results of the SQL query or the details of any database errors within its responses. Blind vulnerabilities can still be exploited to access unauthorized data, but the techniques involved are generally more complicated and difficult to perform.
        
        The following techniques can be used to exploit blind SQL injection vulnerabilities, depending on the nature of the vulnerability and the database involved:
        
        - You can change the logic of the query to trigger a detectable difference in the application's response depending on the truth of a single condition. This might involve injecting a new condition into some Boolean logic, or conditionally triggering an error such as a divide-by-zero.
        - You can conditionally trigger a time delay in the processing of the query. This enables you to infer the truth of the condition based on the time that the application takes to respond.
        - You can trigger an out-of-band network interaction, using OAST techniques. This technique is extremely powerful and works in situations where the other techniques do not. Often, you can directly exfiltrate data via the out-of-band channel. For example, you can place the data into a DNS lookup for a domain that you control.
        
        ### **Read more**
        
        - [Blind SQL injection](https://portswigger.net/web-security/sql-injection/blind)
        
        ## **Second-order SQL injection**
        
        First-order SQL injection occurs when the application processes user input from an HTTP request and incorporates the input into a SQL query in an unsafe way.
        
        Second-order SQL injection occurs when the application takes user input from an HTTP request and stores it for future use. This is usually done by placing the input into a database, but no vulnerability occurs at the point where the data is stored. Later, when handling a different HTTP request, the application retrieves the stored data and incorporates it into a SQL query in an unsafe way. For this reason, second-order SQL injection is also known as stored SQL injection.
        
        [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdQHe_Jq1YXXjxnZftlfYTCYBWL8gH9dH5T4CR3F1FK__RhKkECVipyafOwNuS6pKYe34clAX8Gzlq3NiyZFpVLJJGQc67u-_3fd8F9R3mZC45xPluZ1ZZaisLhhBgDfglEi8o3Qw?key=ZrbJaXHcJo6QVB-SCb6bUjpB)
        
        Second-order SQL injection often occurs in situations where developers are aware of SQL injection vulnerabilities, and so safely handle the initial placement of the input into the database. When the data is later processed, it is deemed to be safe, since it was previously placed into the database safely. At this point, the data is handled in an unsafe way, because the developer wrongly deems it to be trusted.
        
        ## **Examining the database**
        
        Some core features of the SQL language are implemented in the same way across popular database platforms, and so many ways of detecting and exploiting SQL injection vulnerabilities work identically on different types of database.
        
        However, there are also many differences between common databases. These mean that some techniques for detecting and exploiting SQL injection work differently on different platforms. For example:
        
        - Syntax for string concatenation.
        - Comments.
        - Batched (or stacked) queries.
        - Platform-specific APIs.
        - Error messages.
        
        ### **Read more**
        
        [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
        
        After you identify a SQL injection vulnerability, it's often useful to obtain information about the database. This information can help you to exploit the vulnerability.
        
        You can query the version details for the database. Different methods work for different database types. This means that if you find a particular method that works, you can infer the database type. For example, on Oracle you can execute:
        
        SELECT * FROM v$version
        
        You can also identify what database tables exist, and the columns they contain. For example, on most databases you can execute the following query to list the tables:
        
        SELECT * FROM information_schema.tables
        
        ### **Read more**
        
        - [Examining the database in SQL injection attacks](https://portswigger.net/web-security/sql-injection/examining-the-database)
        - [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
        
        ## **SQL injection in different contexts**
        
        In the previous labs, you used the query string to inject your malicious SQL payload. However, you can perform SQL injection attacks using any controllable input that is processed as a SQL query by the application. For example, some websites take input in JSON or XML format and use this to query the database.
        
        These different formats may provide different ways for you to [obfuscate attacks](https://portswigger.net/web-security/essential-skills/obfuscating-attacks-using-encodings#obfuscation-via-xml-encoding) that are otherwise blocked due to WAFs and other defense mechanisms. Weak implementations often look for common SQL injection keywords within the request, so you may be able to bypass these filters by encoding or escaping characters in the prohibited keywords. For example, the following XML-based SQL injection uses an XML escape sequence to encode the S character in SELECT:
        
        <stockCheck>
        
        <productId>123</productId>
        
        <storeId>999 &#x53;ELECT * FROM information_schema.tables</storeId>
        
        </stockCheck>
        
        This will be decoded server-side before being passed to the SQL interpreter.
        
        **LAB**
        
        PRACTITIONER[**SQL injection with filter bypass via XML encoding**](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)
        
        ## **How to prevent SQL injection**
        
        You can prevent most instances of SQL injection using parameterized queries instead of string concatenation within the query. These parameterized queries are also know as "prepared statements".
        
        The following code is vulnerable to SQL injection because the user input is concatenated directly into the query:
        
        String query = "SELECT * FROM products WHERE category = '"+ input + "'";
        
        Statement statement = connection.createStatement();
        
        ResultSet resultSet = statement.executeQuery(query);
        
        You can rewrite this code in a way that prevents the user input from interfering with the query structure:
        
        PreparedStatement statement = connection.prepareStatement("SELECT * FROM products WHERE category = ?");
        
        statement.setString(1, input);
        
        ResultSet resultSet = statement.executeQuery();
        
        You can use parameterized queries for any situation where untrusted input appears as data within the query, including the WHERE clause and values in an INSERT or UPDATE statement. They can't be used to handle untrusted input in other parts of the query, such as table or column names, or the ORDER BY clause. Application functionality that places untrusted data into these parts of the query needs to take a different approach, such as:
        
        - Whitelisting permitted input values.
        - Using different logic to deliver the required behavior.
        
        For a parameterized query to be effective in preventing SQL injection, the string that is used in the query must always be a hard-coded constant. It must never contain any variable data from any origin. Do not be tempted to decide case-by-case whether an item of data is trusted, and continue using string concatenation within the query for cases that are considered safe. It's easy to make mistakes about the possible origin of data, or for changes in other code to taint trusted data.
        
    - Fonte 6 - [owasp](https://owasp.org/www-community/attacks/SQL_Injection)
        
        # **SQL Injection**
        
        Contributor(s): kingthorin, zbraiterman
        
        ## **Overview**
        
        A [SQL injection](https://owasp.org/www-community/attacks/SQL_Injection) attack consists of insertion or “injection” of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.
        
        ## **Threat Modeling**
        
        - SQL injection attacks allow attackers to spoof identity, tamper with existing data, cause repudiation issues such as voiding transactions or changing balances, allow the complete disclosure of all data on the system, destroy the data or make it otherwise unavailable, or become administrators of the database server.
        - SQL Injection is very common with PHP and ASP applications due to the prevalence of older functional interfaces. Due to the nature of programmatic interfaces available, J2EE and ASP.NET applications are less likely to have easily exploited SQL injections.
        - The severity of SQL Injection attacks is limited by the attacker’s skill and imagination, and to a lesser extent, defense in depth countermeasures, such as low privilege connections to the database server and so on. In general, consider SQL Injection a high impact severity.
        
        ## **Related Security Activities**
        
        ### **How to Avoid SQL Injection Vulnerabilities**
        
        See the OWASP [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html). See the OWASP [Query Parameterization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html).
        
        ### **How to Review Code for SQL Injection Vulnerabilities**
        
        See the [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/) article on how to Review Code for SQL Injection vulnerabilities.
        
        ### **How to Test for SQL Injection Vulnerabilities**
        
        See the [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) for information on testing for SQL Injection vulnerabilities.
        
        ### **How to Bypass Web Application Firewalls with SQLi**
        
        See the OWASP Article on [using SQL Injection to bypass a WAF](https://owasp.org/www-community/attacks/SQL_Injection_Bypassing_WAF)
        
        ## **Description**
        
        SQL injection attack occurs when:
        
        1. An unintended data enters a program from an untrusted source.
        2. The data is used to dynamically construct a SQL query
        
        The main consequences are:
        
        - **Confidentiality**: Since SQL databases generally hold sensitive data, loss of confidentiality is a frequent problem with SQL Injection vulnerabilities.
        - **Authentication**: If poor SQL commands are used to check user names and passwords, it may be possible to connect to a system as another user with no previous knowledge of the password.
        - **Authorization**: If authorization information is held in a SQL database, it may be possible to change this information through the successful exploitation of a SQL Injection vulnerability.
        - **Integrity**: Just as it may be possible to read sensitive information, it is also possible to make changes or even delete this information with a SQL Injection attack.
        
        ## **Risk Factors**
        
        The platform affected can be:
        
        - Language: SQL
        - Platform: Any (requires interaction with a SQL database)
        
        SQL Injection has become a common issue with database-driven web sites. The flaw is easily detected, and easily exploited, and as such, any site or software package with even a minimal user base is likely to be subject to an attempted attack of this kind.
        
        Essentially, the attack is accomplished by placing a meta character into data input to then place SQL commands in the control plane, which did not exist there before. This flaw depends on the fact that SQL makes no real distinction between the control and data planes.
        
        ## **Examples**
        
        ### **Example 1**
        
        In SQL: select id, firstname, lastname from authors
        
        If one provided: Firstname: evil'ex and Lastname: Newman
        
        the query string becomes:
        
        select id, firstname, lastname from authors where firstname = 'evil'ex' and lastname ='newman'
        
        which the database attempts to run as:
        
        Incorrect syntax near il' as the database tried to execute evil.
        
        A safe version of the above SQL statement could be coded in Java as:
        
        String firstname = req.getParameter("firstname");
        
        String lastname = req.getParameter("lastname");
        
        // FIXME: do your own validation to detect attacks
        
        String query = "SELECT id, firstname, lastname FROM authors WHERE firstname = ? and lastname = ?";
        
        PreparedStatement pstmt = connection.prepareStatement( query );
        
        pstmt.setString( 1, firstname );
        
        pstmt.setString( 2, lastname );
        
        try
        
        {
        
        ResultSet results = pstmt.execute( );
        
        }
        
        ### **Example 2**
        
        The following C# code dynamically constructs and executes a SQL query that searches for items matching a specified name. The query restricts the items displayed to those where owner matches the user name of the currently-authenticated user.
        
        ...
        
        string userName = ctx.getAuthenticatedUserName();
        
        string query = "SELECT * FROM items WHERE owner = '"
        
        + userName + "' AND itemname = '"
        
        + ItemName.Text + "'";
        
        sda = new SqlDataAdapter(query, conn);
        
        DataTable dt = new DataTable();
        
        sda.Fill(dt);
        
        ...
        
        The query that this code intends to execute follows:
        
        SELECT * FROM items
        
        WHERE owner =
        
        AND itemname = ;
        
        However, because the query is constructed dynamically by concatenating a constant base query string and a user input string, the query only behaves correctly if itemName does not contain a single-quote character. If an attacker with the user name wiley enters the string "name' OR
        
        'a'='a" for itemName, then the query becomes the following:
        
        SELECT * FROM items
        
        WHERE owner = 'wiley'
        
        AND itemname = 'name' OR 'a'='a';
        
        The addition of the OR 'a'='a' condition causes the where clause to always evaluate to true, so the query becomes logically equivalent to the much simpler query:
        
        SELECT * FROM items;
        
        This simplification of the query allows the attacker to bypass the requirement that the query only return items owned by the authenticated user; the query now returns all entries stored in the items table, regardless of their specified owner.
        
        ### **Example 3**
        
        This example examines the effects of a different malicious value passed to the query constructed and executed in Example 1. If an attacker with the user name hacker enters the string "name'); DELETE FROM items; --" for itemName, then the query becomes the following two queries:
        
        SELECT * FROM items
        
        WHERE owner = 'hacker'
        
        AND itemname = 'name';
        
        DELETE FROM items;
        
        - -'
        
        Many database servers, including Microsoft® SQL Server 2000, allow multiple SQL statements separated by semicolons to be executed at once. While this attack string results in an error in Oracle and other database servers that do not allow the batch-execution of statements separated by semicolons, in databases that do allow batch execution, this type of attack allows the attacker to execute arbitrary commands against the database.
        
        Notice the trailing pair of hyphens (--), which specifies to most database servers that the remainder of the statement is to be treated as a comment and not executed. In this case the comment character serves to remove the trailing single-quote left over from the modified query. In a database where comments are not allowed to be used in this way, the general attack could still be made effective using a trick similar to the one shown in Example 1. If an attacker enters the string "name'); DELETE FROM items; SELECT \* FROM items WHERE 'a'='a", the following three valid statements will be created:
        
        SELECT * FROM items
        
        WHERE owner = 'hacker'
        
        AND itemname = 'name';
        
        DELETE FROM items;
        
        SELECT * FROM items WHERE 'a'='a';
        
        One traditional approach to preventing SQL injection attacks is to handle them as an input validation problem and either accept only characters from an allow list of safe values or identify and escape a deny list of potentially malicious values. An allow list can be a very effective means of enforcing strict input validation rules, but parameterized SQL statements require less maintenance and can offer more guarantees with respect to security. As is almost always the case, deny listing is riddled with loopholes that make it ineffective at preventing SQL injection attacks. For example, attackers can:
        
        - Target fields that are not quoted
        - Find ways to bypass the need for certain escaped meta-characters
        - Use stored procedures to hide the injected meta-characters
        
        Manually escaping characters in input to SQL queries can help, but it will not make your application secure from SQL injection attacks.
        
        Another solution commonly proposed for dealing with SQL injection attacks is to use stored procedures. Although stored procedures prevent some types of SQL injection attacks, they fail to protect against many others. For example, the following PL/SQL procedure is vulnerable to the same SQL injection attack shown in the first example.
        
        procedure get_item (
        
        itm_cv IN OUT ItmCurTyp,
        
        usr in varchar2,
        
        itm in varchar2)
        
        is
        
        open itm_cv for ' SELECT * FROM items WHERE ' ||
        
        'owner = '''|| usr ||
        
        ' AND itemname = ''' || itm || '''';
        
        end get_item;
        
        Stored procedures typically help prevent SQL injection attacks by limiting the types of statements that can be passed to their parameters. However, there are many ways around the limitations and many interesting statements that can still be passed to stored procedures. Again, stored procedures can prevent some exploits, but they will not make your application secure against SQL injection attacks.
        
        ## **Related [Attacks](https://owasp.org/www-community/attacks/)**
        
        - [SQL Injection Bypassing WAF](https://www.owasp.org/index.php/SQL_Injection_Bypassing_WAF)
        - [Blind SQL Injection](https://owasp.org/www-community/attacks/Blind_SQL_Injection)
        - [Code Injection](https://owasp.org/www-community/attacks/Code_Injection)
        - [Double Encoding](https://owasp.org/www-community/Double_Encoding)
        - [ORM Injection](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.7-Testing_for_ORM_Injection.html)
        
        ## **References**
        
        - [SQL Injection Knowledge Base](https://book.hacktricks.xyz/pentesting-web/sql-injection) - A reference guide for MySQL, MSSQL and Oracle SQL Injection attacks.
        - [GreenSQL Open Source SQL Injection Filter](http://www.greensql.net/) - An Open Source database firewall used to protect databases from SQL injection attacks.
        - [An Introduction to SQL Injection Attacks for Oracle Developers](https://web.archive.org/web/20151005235207/http://www.net-security.org/dl/articles/IntegrigyIntrotoSQLInjectionAttacks.pdf)
        
        This also includes recommended defenses.
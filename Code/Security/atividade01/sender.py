from scapy.all import send, IP, UDP
from receiverCaesar import caesar  # Importa a função de criptografia de César
import sys

def main():
    m = "Ola Mundo"    
    key = 10  # Chave de criptografia
    ciphered_message = caesar(m, key, 0)  # Criptografa a mensagem

    packet = IP(dst='192.168.1.2') / UDP(dport=12345) / ciphered_message
    packet.show()
    send(packet)  # Envia o pacote criptografado

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_data = ''
    for c in data:
        index = alphabet.find(c.lower())  # Trabalha com letras minúsculas
        if index == -1:
            new_data += c  # Mantém caracteres não alfabéticos
        else:
            new_index = index + key if mode == 0 else index - key
            new_index = new_index % len(alphabet)
            new_char = alphabet[new_index]
            # Preserva maiúsculas e minúsculas
            new_data += new_char.upper() if c.isupper() else new_char
    return new_data

if __name__ == "__main__":
    main()
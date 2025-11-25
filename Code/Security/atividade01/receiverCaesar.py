from scapy.all import sniff, UDP
import sys

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

def packet_handler(packet):
    ciphered_message = packet.load.decode()  # Extrai a mensagem criptografada
    print(f"Mensagem criptografada recebida: {ciphered_message}")
    
    key = 10  # A chave que Bob usaria para decifrar
    plain_message = caesar(ciphered_message, key, 1)  # Descriptografa a mensagem
    print(f"Mensagem descriptografada: {plain_message}")

def main():
    sniff(filter="udp port 12345", prn=packet_handler)  # Escuta pacotes UDP na porta 12345

if __name__ == "__main__":
    main()

from scapy.all import sniff, UDP
import sys

def hackingCaesar(ciphered):
    possible_messages = []  # Lista para armazenar as tentativas de decifração

    for key in range(26):  # Testar todas as chaves de 0 a 25
        decrypted_message = ""
        for char in ciphered:
            if char.isalpha():  # Se for uma letra
                offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - offset - key) % 26 + offset)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char  # Mantém outros caracteres inalterados

        possible_messages.append(f"Key {key}: {decrypted_message}")  # Adiciona tentativa
    return possible_messages  # Retorna todas as mensagens possíveis

def packet_handler(packet):
    ciphered_message = packet.load.decode()  # Extrai a mensagem criptografada
    print(f"Mensagem criptografada recebida: {ciphered_message}")

    possible_decryptions = hackingCaesar(ciphered_message)  # Força bruta para descriptografar
    for decryption in possible_decryptions:
        print(decryption)  # Exibe todas as tentativas de descriptografar

def main():
    sniff(filter="udp port 12345", prn=packet_handler)  # Escuta pacotes UDP na porta 12345

if __name__ == "__main__":
    main()
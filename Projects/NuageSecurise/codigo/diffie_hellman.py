import random

class DiffieHellman:
    # Recebe os parâmetros
    def __init__(self, g, p) -> None:
        self.__g = g  # Gerador de módulo
        self.__p = p  # Número primo
        # Utiliza a função para gerar as chaves públicas e privadas
        self.__chave_privada = self.__gerar_chave_privada()
        self.chave_publica = self.__gerar_chave_publica()
        

    def gerar_numero_aleatorio(self, inicio=1, fim=100):
        """
        Gera um número aleatório dentro do intervalo especificado.
        
        :param inicio: Valor inicial do intervalo (inclusivo)
        :param fim: Valor final do intervalo (inclusivo)
        :return: Número inteiro aleatório
        """
        return random.randint(inicio, fim)
    

    def gerar_numero_primo_aleatorio(self, inicio=2, fim=100):
        """
        Gera um número primo aleatório dentro do intervalo especificado.
        
        :param inicio: Valor inicial do intervalo (inclusivo)
        :param fim: Valor final do intervalo (inclusivo)
        :return: Número primo aleatório
        """
        eh_primo = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
        while True:
            numero = self.gerar_numero_aleatorio(inicio, fim)
            if eh_primo(numero):
                return numero


    def __gerar_chave_privada(self):
        return self.gerar_numero_primo_aleatorio(2, 3333)
    
    def __gerar_chave_publica(self):
        # Chave pública: g**X mod p
        return (self.__g ** self.__chave_privada) % self.__p
    
    # Gera a chave compartilhada
    def gerar_chave_compartilhada(self, chave_publica_outro):
        # Chave compartilhada: b**x mod p
        return (chave_publica_outro ** self.__chave_privada) % self.__p

from AbstractMesa import *
from Carta import *


class Mesa(AbstractMesa):

    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 cartaJogador1: Carta, cartaJogador2: Carta):
        if isinstance(jogador1, Jogador) and jogador1 is not None and \
        isinstance(jogador2, Jogador) and jogador2 is not None and \
        isinstance(cartaJogador1, Carta) and cartaJogador1 is not None and \
        isinstance(cartaJogador2, Carta) and cartaJogador2 is not None:
            self.__jogador1 = jogador1
            self.__jogador2 = jogador2
            self.__cartaJogador1 = cartaJogador1
            self.__cartaJogador2 = cartaJogador2

    @property
    def jogador1(self) -> Jogador:
        return self.__jogador1

    @property
    def jogador2(self) -> Jogador:
        return self.__jogador2

    @property
    def carta_jogador1(self) -> Carta:
        return self.__cartaJogador1

    @property
    def carta_jogador2(self) -> Carta:
        return self.__cartaJogador2
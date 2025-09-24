from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        if isinstance(nome, str) and nome is not None:
            self.__nome = nome
            self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    def baixa_carta_da_mao(self) -> Carta:
        carta_usada = random.choice(self.__mao)
        self.__mao.remove(carta_usada)
        return carta_usada

    @property
    def mao(self) -> list:
        return self.__mao

    def inclui_carta_na_mao(self, carta:Carta):
        self.__mao.append(carta)

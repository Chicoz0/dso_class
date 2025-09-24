from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    def valor_total_carta(self) -> int:
        return(self.__personagem.energia + self.__personagem.habilidade +
               self.__personagem.resistencia + self.__personagem.velocidade)

    @property
    def personagem(self) -> Personagem:
        return self.__personagem

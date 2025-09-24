from AbstractPersonagem import *

class Personagem(AbstractPersonagem):
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        if isinstance(tipo,Tipo) and tipo is not None:
            atributos = [energia, habilidade, velocidade, resistencia]
            error = False
            for atributo in atributos:
                if atributo >= 0 and atributo <= 100:
                    pass
                else:
                    error = True
                    break
            if error == False:
                self.__energia = energia
                self.__habilidade = habilidade
                self.__velocidade = velocidade
                self.__resistencia = resistencia
                self.__tipo = tipo

    @property
    def tipo(self) -> Tipo:
        return self.__tipo

    @property
    def energia(self) -> int:
        return self.__energia

    @property
    def habilidade(self) -> int:
        return self.__habilidade

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def resistencia(self) -> int:
        return self.__resistencia

from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagens = []
        self.__turno = 1

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        novo_personagem = Personagem(energia,habilidade,velocidade,resistencia,tipo)
        self.__personagens.append(novo_personagem)
        return novo_personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        nova_carta = Carta(personagem)
        self.__baralho.append(nova_carta)
        return nova_carta

    def jogada(self, mesa: Mesa) -> Jogador:
        vencedor = None
        if self.__turno <= 50:
            if mesa.carta_jogador1 > mesa.carta_jogador2:
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
            elif mesa.carta_jogador1 < mesa.carta_jogador2:
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            else:
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            self.__turno += 1
            if mesa.jogador1.mao == []:
                vencedor = mesa.jogador2
            elif mesa.jogador2.mao == []:
                vencedor = mesa.jogador1
        return vencedor

from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    def subir(self) -> str:
        try:
            self.__elevador.subir()
        except:
            raise

    def descer(self) -> str:
        try:
            self.__elevador.descer()
        except:
            raise

    def entra_pessoa(self) -> str:
        try:
            self.__elevador.entra_pessoa()
        except:
            raise

    def sai_pessoa(self) -> str:
        try:
            self.__elevador.sai_pessoa()
        except:
            raise

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializar_elevador(self, andar_atual: int,
                             total_andares_predio: int,
                             capacidade: int, total_pessoas: int):
        params = [andar_atual, total_andares_predio, capacidade, total_pessoas]
        for param in params:
            if type(param) is not int or param < 0:
                raise ComandoInvalidoException
        if andar_atual > total_andares_predio:
            raise ComandoInvalidoException
        if total_pessoas > capacidade:
            raise ComandoInvalidoException
        self.__elevador = Elevador(andar_atual, total_andares_predio,
                                   capacidade, total_pessoas)

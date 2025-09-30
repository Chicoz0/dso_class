from abc import ABC, abstractmethod
from elevador import Elevador


class AbstractControladorElevador(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    '''
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador 
    @throws ElevadorJahNoUltimoAndarException 
    '''
    @abstractmethod
    def subir(self) -> str:
        pass
    
    '''
    Faz o elevador descer um andar. Se jah estiver no terreo, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    '''
    @abstractmethod
    def descer(self) -> str:
        pass

    @abstractmethod
    def entra_pessoa(self) -> str:
        pass

    @abstractmethod
    def sai_pessoa(self) -> str:
        pass

    @property
    @abstractmethod
    def elevador(self) -> Elevador:
        pass
    
    @abstractmethod
    def inicializar_elevador(self, andar_atual: int, total_andares_predio: int, capacidade: int, total_pessoas: int):
        pass
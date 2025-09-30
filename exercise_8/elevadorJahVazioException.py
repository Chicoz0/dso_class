class ElevadorJahVazioException(Exception):
    def __init__(self):
        super().__init__("O elevador já esta vazio!")

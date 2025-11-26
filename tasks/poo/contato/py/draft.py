class Fone:
    def __init__(self, nome: str, numero: int):
        self.nome = nome
        self.fone = numero

    def __str__(self) -> str:
        return f"{self.nome}:{self.fone}"
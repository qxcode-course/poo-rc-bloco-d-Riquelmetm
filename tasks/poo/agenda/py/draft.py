class Fone:
    def __init__(self, nome:str, numero:str):
        self.nome = nome
        self.numero = numero

    def __str__(self) -> str:
        return f"{self.nome}:{self.numero}"
     


class Contato:
    def __init__(self, nome:str):
        self.nome = nome
        self.fones: list[Fone] = []
        self.favorito = False
    
    def adicionar (self,nome:str, numero:str):
        fone = Fone(nome, numero)
        self.fones.append(fone)
        return

    def remover (self, indice:int):
        self.fones.pop(indice)
        return
    
    def reverter (self):
        if self.favorito is False:
            self.favorito = True
            return
        elif self.favorito is True:
            self.favorito = False
            return
    
    def __str__(self) -> str:
        return f""

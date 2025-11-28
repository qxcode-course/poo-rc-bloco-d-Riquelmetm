class Fone:
    def __init__(self, nome:str, numero:str):
        self.nome = nome
        self.numero = numero

    def __str__(self) -> str:
        return f"{self.nome}:{self.numero}"
     


class Contato:
    def __init__(self):
        self.fones: list[Fone] = []
        self.favorito = False
    
    def adicionar (self,nome:str, numero:str):
        fone = Fone(nome, numero)
        self.fones.append(fone)
        return

    def remover (self, indice:int):
        self.fones.pop(indice)
        return
    
    def favoritar (self):
        if self.favorito is False:
            self.favorito = True
            return
        elif self.favorito is True:
            self.favorito = False
            return
    
    def __str__(self) -> str:
        if self.favorito is True:
            arroba = "@"
        else:
            arroba = "-"
            fones_str = ", ".join([str(f) for f in self.fones])
            return f"{arroba},[{fones_str}]"

class Agenda:
    def __init__(self, name:str):
        self.contatos: dict[str,list[Contato]] = {}
        self.name = name
    
    def adicionar(self, name:str, ):
        if name in self.contatos:
            



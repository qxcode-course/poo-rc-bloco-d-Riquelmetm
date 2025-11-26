class Fone:
    def __init__(self, nome: str, numero: str):
        
        self.nome = nome
        self.fone = numero

    def __str__(self) -> str:
        return f"{self.nome}:{self.fone}"

class Contato:
    def __init__(self,contato:str):
        self.nome_contato = contato
        self.fones: list[Fone] = []
        self.favorito =  False
    
    def adicionar(self, nome:str, numero:str):
        n = list("0123456789()")
        numero_listado = list(numero)
        if numero_listado in  n:
            

class Fone:
    def __init__(self, nome: str, numero: str):
        
        self.id = nome
        self.number = numero
    
    def isValid(self) -> bool:
        validos = "0123456789()-."
        for c in self.number:
            if c not in validos:
                return False
        return True

    def __str__(self) -> str:
        return f"{self.id}:{self.number}"

class Contato:
    def __init__(self, nome:str):
        self.nome = nome
        self.fones: list[Fone] = []
        self.favorito =  False
    
    def adicionar(self, nome:str, numero:str):
        fone = Fone(nome, numero)
        if fone.isValid():
            self.fones.append(fone)
            return
        else:
            print("fail: invalid number")
    
    def remover(self, indice:int):
        self.fones.pop(indice)
    
    def favoritar(self):
        self.favorito = not self.favorito
    
    def __str__(self) -> str:
        if self.favorito is True:
            arroba = "@"
        else:
            arroba = "-"
        fones_str = ", ".join([str(f) for f in self.fones])
        return f"{arroba} {self.nome} [{fones_str}]"

contato = Contato("")
def main():
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")


        if args[0] == "end":
            break
        
        elif  args[0] == "show":
            print(contato)
        
        elif args[0] == "init":
            contato = Contato(args[1])

        elif args[0] == "add":
            contato.adicionar(args[1], args[2])
        
        elif args[0] == "rm":
            contato.remover(int(args[1]))
        
        elif args[0] == "tfav":
            contato.favoritar()
main()
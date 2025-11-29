class Fone:
    def __init__(self, id:str, numero:str):
        self.id = id
        self.numero = numero

    def isValid(self) -> bool:
        validos = "0123456789()-"
        for c in self.numero:
            if c not in validos:
                return False
        return True

    def __str__(self) -> str:
        return f"{self.id}:{self.numero}"
     


class Contato:
    def __init__(self, nome:str):
        self.fones: list[Fone] = []
        self.favorito = False
        self.nome = nome
    
    def adicionar (self,nome:str, numero:str):
        fone = Fone(nome, numero)
        if fone.isValid():
            self.fones.append(fone)
            return
        else:
            return f"Fone Invalido"


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
        
    def getfavorito(self):
        if self.favorito is True:
            return True
        else:
            return False
    
    def __str__(self) -> str:
        if self.favorito is True:
            arroba = "@"
        else:
            arroba = "-"
        fones_str = ", ".join([str(f) for f in self.fones])
        return f"{arroba} {self.nome} [{fones_str}]"

class Agenda:
    def __init__(self):
        self.contatos: list[Contato] = []
    
    def findposbyname(self, nome:str) -> int:
        for i, contato in enumerate(self.contatos):
            if contato.nome == nome:
                return i
        return -1
    
    def adicionar(self, nome:str, fones: list[Fone]):
        pos = self.findposbyname(nome)

        if pos != -1:
            contato_existe = self.contatos[pos]
            for fone in fones:
                contato_existe.adicionar(fone.id, fone.numero)


        else:
            novo_contato = Contato(nome)
            for fone in fones:
                novo_contato.adicionar(fone.id, fone.numero)
            
            self.contatos.append(novo_contato)
            self.contatos.sort(key=lambda contato: contato.nome)

    def removercontat(self, nome:str):
        pos = self.findposbyname(nome)
        if pos != -1:
            self.contatos.pop(pos)

    def getcontato(self, nome:str):
        pos = self.findposbyname(nome)
        if pos != -1:
            return self.contatos[pos]
        else:
            return None

    def search(self, palavra:str):
        resultado = []
        for contato in self.contatos:
            if palavra in contato.nome:
                resultado.append(contato)
                continue
            for fone in contato.fones:
                    if palavra in fone.id or palavra in fone.numero:
                        resultado.append(contato)
                        break
        return

    def getFavoritos(self):
        favs = []
        for c in self.contatos:
            if c.favorito:
                favs.append(c)
        return favs
    
    def __str__(self):
        return "\n".join([str(c) for c in self.contatos])
    

    
def main():
    agenda = Agenda()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
            
        elif args[0] == "add":
            nome = args[1]
            fones_add = []
            for token in args[2:]:
                partes = token.split(":")
                if len(partes) == 2:
                    fones_add.append(Fone(partes[0], partes[1]))
            
            agenda.adicionar(nome, fones_add)
    

        elif args[0] == "show":
            print(agenda)

        elif args[0] == "rm":
            agenda.removercontat(args[1])
        
        elif args[0] == "rmFone":
            contato = agenda.getcontato(args[1])

            if contato:
                contato.remover(int(args[2]))

        elif args[0] == "tfav":
            contato = agenda.getcontato(args[1])
            if contato:
                contato.favoritar()

        elif args[0] == "favs":
                favoritos = agenda.getFavoritos()
                for fav in favoritos:
                    print(fav)

        elif args[0] == "search":
            pattern = args[1]
            res = agenda.search(pattern)
            for c in res:
                print(c)

main()



import contas

class Pessoas:
    def __init__(self, nome:str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        self._nome
    
    @nome.setter
    def nome(self, nome: str):
         self._nome = nome
    
    @property
    def idade(self) -> int:
        self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade 

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r} {self.idade!r})'
        return f'{class_name}{attrs}'    

class Cliente(Pessoas):
    def __init__(self, nome:str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None
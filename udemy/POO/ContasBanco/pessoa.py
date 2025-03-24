class Pessoa:
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

class Cliente(Pessoa):
    def __init__(self, nome:str, idade: int) -> None:
        super().__init__(nome, idade)
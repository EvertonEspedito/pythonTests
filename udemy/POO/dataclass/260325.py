from dataclasses import dataclass
 
 
@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def nomeCompleto(self):
        return f'{self.nome} {self.sobrenome}'
 
 
if __name__ == '__main__':
    p1 = Pessoa('Everton','Espedito')
    print(p1.nomeCompleto())
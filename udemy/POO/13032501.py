# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    #é equivalente ao contructor
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


p1 = Pessoa("Everton", "Santos",21)
print(p1.nome)
print(p1.sobrenome) 
print(p1.idade)  # 21


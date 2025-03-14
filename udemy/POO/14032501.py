class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        
    def comendo (self,alimento):
        print(f'{self.name} está comendo {alimento}')

leao = Animal("Everton",21,"SEXÃO BAGAÇADOR")

print(f'O Animal se chama {leao.name}\nÉ da especie {leao.species}\nE tem {leao.age} anos')
print(leao.comendo("carne"))
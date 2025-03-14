# Metodos e Instacias de classes Python

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f'O {self.modelo} da marca: {self.marca}, esta Acelerando')

    def dadosCarro(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano : {self.ano}')

c1 = Carro('Ford', 'Focus', '2001')
c1.acelerar()
c1.dadosCarro()
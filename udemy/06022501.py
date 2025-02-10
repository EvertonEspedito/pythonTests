#Concatenação
print("Olá!, tudo bem?")
anoNascimento = input("Digite sua data de nascimento, e veremos quantos anos vc vai ter em 2035:")
anoNascimento = int(anoNascimento)
idadeAtual = 2025 - anoNascimento
idadeFuturo = 2035 - anoNascimento
print(f"Vc tem {idadeAtual } anos e em 2035 vc irá ter {idadeFuturo} anos")

#Media de gastos de Combustivel
distancia_percorrida = "2254"
combustivel_gasto = "239.7"
mediaConsul =  float(combustivel_gasto)/float(distancia_percorrida)  * 100
print(f"{mediaConsul:.3f} km/l")

#imc do Usúario
print("Vamos Calcular o seu IMC")
altura = input("Digite Sua Altura: ")
peso = input("Digite Seu Peso: ")

imc = float(peso)/(float(altura)* float(altura))

print(f"Seu IMC é: {imc:.2f}")


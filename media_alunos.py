nota = float(input("Digite sua nota: "))

nota2 = float(input("Digite sua nota: "))

nota3 = float(input("Digite sua nota: "))

nota4 = float(input("Digite sua nota: "))

nota5 = float(input("Digite sua nota: "))


media = (nota + nota2 + nota3 + nota4 + nota5 )/ 5

print(f"- A sua media é: {media}")

#Media Ponderada
# Definição das notas
A = 7.0
B = 5.1
C = 3.8

# Definição dos pesos
peso_A = 2
peso_B = 3
peso_C = 5

# Cálculo da média ponderada
media = (A * peso_A + B * peso_B + C * peso_C) / (peso_A + peso_B + peso_C)

# Impressão do resultado formatado
print(f"MEDIA = {media:.1f}")

#Area
pi = 3.14159
raio = 10
area = pi*pow(raio,2)
print(f"A= {area}")
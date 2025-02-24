# Crie um programa que peça ao usuário para digitar um número.
# O programa deve informar se o número é par ou ímpar. 
# Após exibir o resultado, o programa encerra.

n = int(input("Digite um número: "))
if n % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
#Funções - Recursividade
def soma(num1,num2):
    resul = num1 + num2
    return resul

def subtracao(num1,num2):
    resul = num1 - num2
    return resul

def multiplicacao(num1,num2):
    resul = num1 * num2
    return resul

def divisao(num1,num2):
    if num2 != 0:
        resul = num1 * num2
        return resul
    
def dupTripQaud(num):
    return num * 2, num * 3, num * 4
    
while True:
    print("Faça seu Cálculo!")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Duplicar, Triplicar, Quadruplicar")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Somar:")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(soma(num1,num2))
    if opcao == 2:
        print("Subtrair")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(subtracao(num1,num2))
    if opcao == 3:
        print("Multiplicar")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(multiplicacao(num1,num2))
    if opcao == 4:
        print("Dividir")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(divisao(num1,num2))
    if opcao == 5:
        print("Duplicar, Triplicar, Quadruplicar")
        num = float(input("Digite um número: "))
        print(dupTripQaud(num))
    if opcao == 6:
        print("Obrigado por usar o nosso programa!")
        break

print("Obrigado! Volte Sempre!")

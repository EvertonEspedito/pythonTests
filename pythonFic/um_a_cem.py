# Crie um programa que peça ao usuário para digitar um número entre 1 e 100. 
# Se o número estiver dentro do intervalo, exiba uma mensagem de sucesso. 
# Caso contrário, peça ao usuário para tentar novamente. 
# O programa deve continuar até que um número válido seja informado.

n = int(input("Digite um número: "))
while n < 1 or n > 100:
    n = int(input("Número inválido. Por favor, digite um número entre 1 a 100: "))
print("Dentro do Escopo, Parabéns!")    
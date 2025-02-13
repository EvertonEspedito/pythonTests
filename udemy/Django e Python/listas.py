"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista=[]

while True:
    print("Selecione uma opção para Lista")
    opc = input("[I] Inserir, [A] Apagar e [L]Listar:")
    if opc.upper() == "I" or opc.lower() == "i":
        valor = input("Digite o valor a ser inserido: ")
        lista.append(valor)
    elif opc.upper() == "A" or opc.lower() == "a":
        valor = input("Digite o valor a ser apagado: ")
        if valor in lista:
            lista.remove(valor)
        else:
            print("O valor não existe na lista")
    elif opc.upper() == "L" or opc.lower() == "l":
        print(lista)
    else:
        print("Opção inválida, tente novamente")
        cont = input("Deseja continuar? [S] Sim ou [N] Não")
        if cont.upper() == "N" or cont.lower() == "n":
            break


    
# Estudo de Caso: Gerenciador de Lista de Tarefas
# Contexto: Você foi contratado para desenvolver um programa simples em Python que permita aos usuários gerenciar uma lista de tarefas. As tarefas devem ser armazenadas em um arquivo de texto, e o programa deve permitir que o usuário adicione novas tarefas, visualize todas as tarefas existentes e limpe a lista de tarefas.
# Requisitos do Programa:
# Adicionar Tarefa:
# O usuário deve poder adicionar uma nova tarefa à lista.
# A tarefa deve ser salva em um arquivo chamado tarefas.txt.
# Visualizar Tarefas:
# O usuário deve poder visualizar todas as tarefas armazenadas no arquivo.
# Limpar Lista de Tarefas:
# O usuário deve poder apagar todas as tarefas do arquivo.
# Sair:
# O programa deve permitir que o usuário saia do sistema.

print("SEJA BEM VINDO")
print("Gerenciador de Lista de Tarefas")

while True:
    print("\n1 - Adicionar Tarefa")
    print("2 - Visualizar Tarefas")
    print("3 - Limpar Lista de Tarefas")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        with open('tarefas.txt', "a") as arquivo:
            arquivo.write(f'-> {tarefa}\n')
            print("Tarefa adicionada com sucesso!")
    if opcao == "2":
        with open('tarefas.txt', "r") as arquivo:
            print(arquivo.read())
    if opcao == "3":
        with open('tarefas.txt', "w") as arquivo:
            arquivo.write('')
            print("Lista de tarefas limpa com sucesso!")
    if opcao == "4":
        print("Obrigado por usar o Gerenciador de Lista de Tarefas!")
        break
print("Fim do programa")





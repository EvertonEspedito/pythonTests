# Exercício - Lista de tarefas com desfazer e refazer

# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

toDo = []
desfazer = []

while True:
    print('Lista de Tarefas')
    print(f'Tarefas: {toDo}')
    print('1 - Adicionar Tarefa')
    print('2 - Desfazer')
    print('3 - Refazer')
    print('4 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        tarefa = input('Digite a tarefa: ')
        toDo.append(tarefa)

    if opcao == '2':
        if len(toDo) > 0:
            desfazer.append(toDo.pop())
            print(f'Desfazendo: {desfazer[-1]}')
        else:
            print('Não há tarefas para desfazer')
    
    if opcao == '3':
        if len(desfazer) > 0:
            tarefa = desfazer.pop()
            toDo.append(tarefa)
            print(f'Refazendo: {toDo}')
        else:
            print('Não há tarefas para refazer')

    if opcao == '4':
        print('Saindo...')
        break
    
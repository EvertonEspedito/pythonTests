# Crie um programa que manipule uma lista de alunos. Inicialmente, a lista contém cinco nomes predefinidos. O programa deve
# solicitar ao usuário que adicione um novo nome à lista e, em seguida, que remova um nome de sua escolha. Após essas
# alterações, a lista deverá ser organizada em ordem alfabética e exibida na tela.

# As regras:
# O usuário deve inserir um nome para ser adicionado à lista.
# O usuário deve inserir um nome para ser removido. 
# Caso o nome não esteja na lista, o programa deve informar ao usuário.
# A lista final deve ser exibida em ordem alfabética.

listaAlunos = ["João", "Maria", "Pedro", "Ana", "Luiz"]

print("a lista inicial é")
for nomes in listaAlunos:
    print(f'-> {nomes}')

print("Adicione um novo nome à lista:")
nomeAdicionar = input()

listaAlunos.append(nomeAdicionar)

print("a lista após adicionar um novo nome é")
for nomes in listaAlunos:
    print(f'-> {nomes}')

print("Agora Remova um Nome da Lista")
removeName  = input()


while removeName not in listaAlunos:
    print("nome não encontrado, tente novamente")
    removeName = input()
else:
    listaAlunos.remove(removeName)

print("a lista após Remover um novo nome é")
for nomes in listaAlunos:
    print(f'-> {nomes}')

listaAlunos.sort()

print("a lista em ordem alfabética:")
for nomes in listaAlunos:
    print(f'-> {nomes}')
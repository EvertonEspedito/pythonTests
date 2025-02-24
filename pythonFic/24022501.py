dados = [0]

# print(dados[0])

# dados.append(60)

# print(dados[1])


for itens in dados:
    print(itens)
    num = itens
    num+=1
    dados.append(num)
    if num > 100:
        break

dados.reverse()
for itens in dados:
    print(itens)

aluno = {
    "Aluno" : "Ana",
    "Idade" : 30,
    "Curso" : "Engenharia"
}    

aluno["Idade"] = 22

print(aluno["Idade"])

for chave, valor in aluno.items():
    print(f'{chave}:{valor}')

    
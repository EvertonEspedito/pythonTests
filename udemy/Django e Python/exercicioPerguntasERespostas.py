# Exercicio de Perguntas e Respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1','3','4','8'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5 - 1?',
        'Opções': ['3','4','5','6'],
        'Resposta': '4',
    }, 

    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['3','4','5','6'],
        'Resposta': '5',
    },

    {
        'Pergunta': 'Quanto é 7 * 4?',
        'Opções': ['25','28','30','32'],
        'Resposta': '28',
    },
]

# Função para perguntar as perguntas
qtd_acert = 0
for pergunta in perguntas:
    print('Pergunta: ',pergunta['Pergunta'])
    print()
    opcoes = pergunta['Opções']
    for i,opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()
    escolha = input('Escolha a resposta: ')
    print()

    acertou = False
    escolha_int = None
    qtd_opc = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opc:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    if acertou:
        qtd_acert+=1
        print('Você acertou!')
    else:
        print('Você errou! A resposta correta era:',pergunta['Resposta'])
    print()

print(f'Você acertou,{qtd_acert},perguntas.')
print(f'de: {len(perguntas)}')
                
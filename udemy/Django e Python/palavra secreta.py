"""Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário."""
import os 

palavra_secreta = "carro"
letrasAcertadas = ''
tentativas = 0

while True:
    letraDigitada = input('Digite a Letra: ')
    tentativas+=1
    if len(letraDigitada) != 1:
        print('Você deve digitar apenas uma letra')
        continue
    if letraDigitada in palavra_secreta:
        letrasAcertadas+= letraDigitada

    palavra_formada = ''

    for letraDigitada in palavra_secreta:
        if letraDigitada in letrasAcertadas:
            palavra_formada+=letraDigitada
        else:
           palavra_formada += '*'

    print(f'Palavra Formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("PARABÉNS! VOCÊ GANHOUU!")
        print(f'Palavra Secreta era: {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        letrasAcertadas = ''
        tentativas = 0
        
    
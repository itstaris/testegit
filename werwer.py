import random

palavra_secreta = random.choice(['python', 'programacao', 'computador'])
letras_acertadas = ['_' for letra in palavra_secreta]
chutes = []

while '_' in letras_acertadas:
    print(' '.join(letras_acertadas))
    chute = input('Digite uma letra: ').lower()

    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_acertadas[i] = letra
        print('Boa tentativa!')
    else:
        print('Letra não encontrada.')
        chutes.append(chute)
        print('Chutes já feitos:', chutes)

print('Parabéns! Você acertou a palavra:', palavra_secreta)
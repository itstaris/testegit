import random
import sys

print("Vamos jogar jokempo!")

nova_tentativa = ()
while nova_tentativa == "sim" or "Sim" or "SIM":
    resposta = input('Escolha pedra, papel ou tesoura: ')

    possibilidades = ["pedra", "papel", "tesoura"]
    escolha_bot = random.choice(possibilidades)

    while resposta.lower() not in possibilidades:
        resposta = input('Não não não, faça uma escolha válida: ')


    while escolha_bot == resposta.lower():
        print(f"{escolha_bot}! puts, deu empate...")
        resposta = input('Vamos tentar de novo então. Dê outra resposta: ')
        escolha_bot = random.choice(possibilidades)

    if escolha_bot == "pedra" and resposta.lower() == "papel" or escolha_bot == "tesoura" and resposta.lower() == "pedra" or escolha_bot == "tesoura" and resposta.lower() == "pedra":
        print(f"{escolha_bot}! \n Olha! você ganhou!")
    else:
        print(f"{escolha_bot}! Hmmm dessa vez a vitória foi minha.")
    nova_tentativa = input('Gostaria de tentar novamente? ')
if nova_tentativa == "não" or "NÃO" or "Não":
    print("Ok! Deixamos para uma próxima.")
sys.exit()
import random
import sys

print("Vamos jogar jokempo!")

resposta = input('Escolha pedra, papel ou tesoura: ').lower()

possibilidades = ["pedra", "papel", "tesoura"]
escolha_bot = random.choice(possibilidades)

while resposta not in possibilidades:
    resposta = input('Não não não, faça uma escolha válida: ')


while escolha_bot == resposta:
    print(f"{escolha_bot}! puts, deu empate...")
    resposta = input('Vamos tentar de novo então. Dê outra resposta: ')
    escolha_bot = random.choice(possibilidades)

if escolha_bot == "pedra" and resposta == "papel" or escolha_bot == "tesoura" and resposta == "pedra" or escolha_bot == "tesoura" and resposta == "pedra":
    print(f"{escolha_bot}! \n Olha! você ganhou!")
else:
    print(f"{escolha_bot}! Hmmm dessa vez a vitória foi minha.")

print("Obrigada por jogar!")
sys.exit()
import random

print("Vamos jogar jokempo!")
resposta = input('Escolha pedra, papel ou tesoura: ')

possibilidades = ["pedra", "papel", "tesoura"]
escolha_bot = random.choice(possibilidades)

while resposta.lower() not in possibilidades:
    resposta = input('Não não não, faça uma escolha válida: ')

while escolha_bot == resposta.lower():
    print(f"{escolha_bot}! puts, deu empate...")
    resposta = input('Vamos tentar de novo. Dê outra resposta: ')
    escolha_bot = random.choice(possibilidades)
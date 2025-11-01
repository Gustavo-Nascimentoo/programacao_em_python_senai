import random

numero = random.randrange(1,10)
escolha = int(input("escolha um número de 1 à 5"))

if numero == escolha:
    print("Você ganhou o jogo 🥳")
    print("O número aleatório é", numero)
else:
    print("Errou feio!")
    print("O número aleatório é", numero)
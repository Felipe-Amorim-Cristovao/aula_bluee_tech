#   Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
#   palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6
#   números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

a = 0
palpites = int(input('Quantos palpites de jogo você deseja? '))

Lista_principal = []  

for x in range(palpites):
    Lista = []
    num = 0
    while num < 6:
        a = random.randint(1,60)
        if a not in Lista:        
            Lista.append(a)
            num += 1 

    Lista_principal.append(Lista)
    
print(Lista_principal)
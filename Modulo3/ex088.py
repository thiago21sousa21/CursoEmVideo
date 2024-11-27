# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para 
# cada jogo, cadastrando tudo em uma lista composta.

from random import randint

qnt_jogo = int(input('Digite a quantidade de jogos: '))

jogos = []

for j in range(qnt_jogo):
    jogo = []
    for n in range(6):
        num = randint(1, 60)
        jogo.append(num)
    jogos.append(jogo)

print(jogos)




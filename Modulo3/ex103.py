# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
#  que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#  O programa deverá ser capaz de mostrar a ficha do jogador,
#  mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='ninguem', gol=0):
    print(f'O jogador {jogador} marcou {gol} gols')

ficha()
# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python. No final,
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogadores = {
    'jogagor1': randint(1,6),
    'jogagor2': randint(1,6),
    'jogagor3': randint(1,6),
    'jogagor4': randint(1,6)
}

for k, v in jogadores.items():
    print(f'o {k}, tirou: {v}')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i,v in enumerate(ranking):
    print(f'o {i+1}º lugar {v[0]} pois tirou {v[1]}')

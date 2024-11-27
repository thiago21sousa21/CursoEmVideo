# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#  O programa vai ler o nome do jogador e quantas partidas ele jogou.
#  Depois vai ler a quantidade de gols feitos em cada partida.
#  No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante
#  o campeonato.

dados_jogador = {}
dados_jogador['total_gols'] = 0
dados_jogador['gol_partidas'] = []

dados_jogador['nome']= input('Digite o nome do jogador: ')
gol_partidas = int(input('Quantas partidas ele jogou? '))

for p in range(gol_partidas):
    qnt_gols = int(input(f'Quantos gols ele fez na {p+1}º partida: '))
    dados_jogador['gol_partidas'].append(qnt_gols)
    dados_jogador['total_gols']+= qnt_gols


print(f'O jogador {dados_jogador["nome"]} fez:')
for i,g in enumerate(dados_jogador['gol_partidas']):
    print(f'{g} gols na {i+1}º partida')
print(f'Foi um total de {dados_jogador["total_gols"]} gols')

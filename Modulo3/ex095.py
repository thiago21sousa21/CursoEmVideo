# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
#  incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.|


jogos = []

while True:
    dados_jogador = {}
    dados_jogador['total_gols'] = 0
    dados_jogador['gol_partidas'] = []

    dados_jogador['nome']= input('Digite o nome do jogador: ')
    gol_partidas = int(input('Quantas partidas ele jogou? '))

    for p in range(gol_partidas):
        qnt_gols = int(input(f'Quantos gols ele fez na {p+1}º partida: '))
        dados_jogador['gol_partidas'].append(qnt_gols)
        dados_jogador['total_gols']+= qnt_gols
    
    jogos.append(dados_jogador)

    while True:
        continuar = input('Continuar? [s/n]: ').strip()[0].lower()
        if continuar in 'ns':
            break
        print('Opção inválida, tente de novo')
    if continuar == 'n':
        break

print()
print('SELECIONE A OPÇÃO DESEJADA')
for i, jogo in enumerate(jogos):
    print(f'Opção: {i} ----- jogador: {jogo['nome']}')

while True:
    opçao = int(input('Digite a opção desejada: '))

    while len(jogos)-1 < opçao  or  opçao < 0:
        opçao = int(input('Opção inválida, tente do novo: '))

    jogador = jogos[opçao]

    print(f'O jogador {jogador["nome"]} fez:')
    for i,g in enumerate(jogador['gol_partidas']):
        print(f'{g} gols na {i+1}º partida')
    print(f'Foi um total de {jogador["total_gols"]} gols')

    while True:
        continuar = input('Continuar? [s/n]: ').strip()[0].lower()
        if continuar in 'ns':
            break
        print('Opção inválida, tente de novo')
    if continuar == 'n':
        break
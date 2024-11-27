#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
# Importante: use cores.

def ler_nome_comando(nome):
    print('\033[1;43m oioi')
    print(f'{help(nome)}\033[m')
    print('\033[1;43m oioi')


while True:
    comando = input('Digite o nome do comando( para sair digite fim): ').lower().strip()
    if comando == 'fim':
        break
    ler_nome_comando('len')

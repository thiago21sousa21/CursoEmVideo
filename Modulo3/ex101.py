# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
#  que vai receber como parâmetro o ano de nascimento de uma pessoa,
#  retornando um valor literal indicando se uma pessoa tem voto
#  NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano_nascimento):
    from datetime import datetime

    data_atual = datetime.now().year
    idade = data_atual - int(ano_nascimento)

    if idade < 16:
        return'NEGADO'
    elif idade < 18 or idade >= 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATORIO'

ano_nascimento = int(input('Digite o ano de nascimento: '))
print(voto(ano_nascimento))
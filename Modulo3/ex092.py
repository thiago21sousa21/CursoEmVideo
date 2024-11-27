# Exercício Python 092: Crie um programa que leia nome, 
# ano de nascimento e carteira de trabalho 
# e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa
#  vai se aposentar.

from datetime import date

print(date.today().year)

dados = dict()
dados['nome'] = input('Digite o nome: ')
dados['ano_nascimento'] = int(input('Digite o ano de nascimento: '))
dados['idade'] = int(date.today().year) - dados['ano_nascimento']
dados['carteira_trabalho'] = 0

while True:
    tem_carteira = input('Tem nummero de carteira de trabalho? [s/n]').strip()[0].lower()
    if tem_carteira == 's':
        dados['carteira_trabalho'] = input('Digite o número da carteira de trabalho: ')
        break
    elif tem_carteira == 'n':
        break
    else:
        print('Opção inválida tente novamente')        

if dados['carteira_trabalho'] != 0:
    dados['ano_contratação'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o salário: '))
    dados['ano_aposentadoria'] = dados['ano_contratação'] + 20

for k, v in dados.items():
    print(f'{k}: {v}')
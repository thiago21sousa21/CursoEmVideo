# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
#  guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

dados = dict()

dados['nome'] = input('Digite o nome do aluno: ')
dados['media'] = float(input('Digite a média do aluno: '))
dados['situação'] = 'reprovado' if dados['media'] < 7 else 'aprovado'

print()
print()
for k, d in dados.items():
    print(f'{k}: {d}')



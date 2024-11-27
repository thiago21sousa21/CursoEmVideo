# Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(valor):
    if type(valor) != int:
        print(f'valor inválido, tente usar um inteiro')
    else:
        print(f'você digitou o número: {valor}')

leiaInt('a')
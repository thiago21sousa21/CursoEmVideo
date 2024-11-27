# Exercício Python 113: Reescreva a função leiaInt() que fizemos
#  no desafio 104, incluindo agora a possibilidade da digitação de
#  um número de tipo inválido. Aproveite e crie também uma função
#  leiaFloat() com a mesma funcionalidade.

def leiaInt():
    v = input('Digite um valor  a ser convertido para inteiro: ')
    try:
        v = int(v)

    except ValueError:
        print(f'voce não um caractere que não pode ser convertido para inteiro: {v}')
    except Exception as err:
        print(err.__class__)
    else:
        print('convertido com sucesso')
        return v

leiaInt()

def leiaFloat():
    v = input('Digite um valor a ser convertido para decimal: ')

    try:
        v = float(v)
    except ValueError: 
        print('Você digitou um caractere que não pode ser convertido, para decimal')
    except Exception as err:
        print(err.__class__)
    else:
        print('convertido com sucesso')
        return v
# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla_palavras = ('thiago', 'sousa', 'santos', 'sara', 'sousa', 'barbosa')

for palavra in tupla_palavras:
    print(f'A palavra {palavra} tem as vogais: ')
    for c in palavra:
        if c.upper() in 'AEIOU':
            print(f' {c}', end=' ')
    print('\n')            


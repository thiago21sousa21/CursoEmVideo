# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
#  que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) 
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~      

def escreva(texto):
    tamanho_texto = len(texto)
    print('~'*tamanho_texto)
    print(texto)
    print('~'*tamanho_texto)

texto = input('Digite alguma coisa: ')

escreva(texto)
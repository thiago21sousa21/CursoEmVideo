# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções
#  chamadas sorteia() e somaPar().
#  A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda
#  função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import sample

lista = [1,2,3,4,5,6]

def apenas5(lista):
    return sample(lista, k=5)

def apenas_pares(lista):
    print(lista)
    soma_pares = 0
    for n in lista:
        if n % 2 == 0:
            soma_pares+= n
    print(soma_pares)

apenas_pares(apenas5(lista))




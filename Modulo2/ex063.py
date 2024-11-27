# Exercício Python 63: Escreva um programa que leia um número N inteiro
# qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8

ultimo = 1
penultimo = 0

n = int(input('Digite a quantidade de elementos da sequencia de fibonacci que será gerada: '))
cont = 2
sequencia = "0 1"

if n == 0 :
    print("sem lista")
elif n ==1:
    print(0)
elif n==2:
    print(sequencia)
elif n >2:
    while(cont <n):
        aux = ultimo
        ultimo += penultimo
        penultimo = aux
        sequencia+= f' {ultimo}'
        cont += 1        
    print(sequencia)
    


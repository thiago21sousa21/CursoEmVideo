# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores 
# e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


soma = cont = n = maior = menor = 0
prosseguir = True
while prosseguir:
    n = int(input("Digite um número: "))
    if cont ==0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont+=1
    soma+=n
    prosseguir = input("digitar mais um número [S/N]? ").strip().upper()[0]
    if prosseguir == 'N':
        prosseguir = False
media = soma/cont
print(f'A média dos números é {media}, o maior número foi {maior} e o menor número foi {menor}')
        
    


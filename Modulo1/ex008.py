#escreva um programa que leia um valor em metros e escreva ele convertido
#em centimetros e milimetros

n = float(input('Digite um valor em metros: '))

print('ele é igual a {}cm e {}mm'.format(n*100, n*1000))
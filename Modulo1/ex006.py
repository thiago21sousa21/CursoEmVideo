# crie um algoritmo que leia um número, dps mostre seu dobro, triplo e raiz quadrada

n = float(input('Digite um valor: '))

print('o número que voce digitou foi {} o dobro dele é {} '.format(n, n*2), end='')
print(', o triplo dele é {} e a sua raiz quadrada é {}'.format(n*3, n**(1/2)))
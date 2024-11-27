#um programa que leia as duas notas de uma aluno, calcule  e mostre a média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

print('a media é {:.2f}'.format(media))
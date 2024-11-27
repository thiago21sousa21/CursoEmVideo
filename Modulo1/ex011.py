#faça um programa que leia a largura e a altura de uma parede, calcule a sua área
#e a quantidade de tinta necessária pra pinta-la, sabendo que cada litro de tinta,
#pinta uma área de 2m**2

alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))

area = alt * larg

litros = area / 2

print('a area da parede é {}m² e a quantidade de tinta pra pinta é {:.2f}l'.format(area, litros))
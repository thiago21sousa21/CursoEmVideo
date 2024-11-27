#faça um programa que leia um angulo e retore o seno e o cosseno dele
import math

angulo = math.radians(float(input('digite um angulo qualquer: ')))

sin = math.sin(angulo)
cos = math.cos(angulo)


print('O valor do seno é {:.2f} e o valor do cosseno é {:.2f}'.format(sin, cos))
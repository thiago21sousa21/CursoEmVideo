#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo retângulo e calcule o comprimento da hipotenusa
import math

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

comprimento_hipotenusa = math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2))

print('O valor da hipotenusa é: {}'.format(comprimento_hipotenusa))
print('''outra forma de fazer:''')
comprimento_hipotenusa_outra_forma = math.hypot(cateto_oposto, cateto_adjacente)

print(comprimento_hipotenusa_outra_forma)
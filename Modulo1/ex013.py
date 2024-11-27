#faça um programa que leia o salário de um funcionário e mostre o seu novo valor
#com um aumento de 15%

salario = float(input('digite o valor do salário: '))

novo_salario = salario + salario*0.15

print('o valor do salario com 15% de aumento é : {}'.format(novo_salario))
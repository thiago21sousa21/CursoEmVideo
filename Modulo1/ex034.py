salario = float(input("Digite o valor do seu salario: "))
novo_salario = 0
if salario > 1250:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.15

print("Seu novo salário será: {}".format(novo_salario))
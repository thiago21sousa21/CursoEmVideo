#Exercício Python 108: Adapte o código do desafio 
# #107, criando uma função adicional chamada moeda() que 
# consiga mostrar os números como um valor monetário formatado. 

import modulos.ex108.moeda

valor = float(input('Digite o valor: '))
taxa = float(input('Digite a taxa: '))

print(modulos.ex108.moeda.aumentar(valor, taxa))
print(modulos.ex108.moeda.diminuir(valor, taxa))
print(modulos.ex108.moeda.dobro(valor))
print(modulos.ex108.moeda.metade(valor))

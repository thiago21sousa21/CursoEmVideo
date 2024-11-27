# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um
#  parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função
#  moeda(), desenvolvida no desafio 108.

import modulos.ex109.moeda as moeda

valor = float(input('Digite o valor: '))
taxa = float(input('Digite a taxa: '))

print(moeda.aumentar(valor, taxa, ))
print(moeda.diminuir(valor, taxa, ))
print(moeda.dobro(valor, True))
print(moeda.metade(valor, True))

help(moeda.aumentar)
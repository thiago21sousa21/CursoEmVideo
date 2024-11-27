# Crie um programa que leia vários números e coloca em uma lista
# Depois disso crie duas listas que vão conter apenas os valores pares e os valores impares digitados
# Ao final mostre o conteudo das tres listas geradas

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar [s/n]? ').strip().lower()[0]
    if(continuar=='n'):
        break

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'''A lista completa é:
      {lista}
      
      os sublista par dela é:
      {pares}
      
      a sublista ímpar é:
      {impares}''')

# Crie um programa que leia varios númeor e coloca em uma lista, depois disso mostre:

#quantos números foram digitados
#a lista de valores ordenada de forma crescente
# se o valor 5 foi digitado ou não está na lista

lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar [s/n]? ').strip().lower()[0]
    if(continuar=='n'):
        break

lista.sort()
print(f'''foram digitados {len(lista)} numeros
      a lista ordenada é {lista}
      o numero 5 esta na lista? {'sim' if 5 in lista else 'não'}''')
    
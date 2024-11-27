# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, ja
# na posição correta de inserção sem usar o método sort()
# no final mostre a lista ordenada na tela


# ficar lendo valores
    # verifiar se é o maior  inserir no último lugar
    # verificar se é o menor e inserir no primeiro lugar
    # verificar o primeiro caso que é maior que ele e inserir nesse lugar

lista = []
maior = menor = cont = 0

while True:
    n = int(input("Digite um número: "))
    if cont == 0:
        maior = n
        menor = n
        lista.append(n)
    else:
        ultimo = lista[len(lista)-1]
        primeiro = lista[0]
        if n > ultimo:
            lista.append(n)
            print(f'Inserido no ultimo lugar, posição {len(lista)-1}')
        elif n < primeiro:
            lista.insert(0,n)
            print('Inserido na posição 0')
        else:
            c = 0
            while n >= lista[c]:
                print(f'como {n} >= {lista[c]} vou somar mais um e continuar')
                c += 1
            lista.insert(c,n)
            print(f'inserido na posição {c}')
    
    cont+=1
    continuar = input('Deseja continuar [s/n]? ').strip().lower()[0]
    if(continuar=='n'):
        break

print(lista)
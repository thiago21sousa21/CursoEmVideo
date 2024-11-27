#faça um programa que leia 5 valore numéricos e os guarde em uma lista. No final
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = []
maiores = []
menores = []
str_maiores = str_menores = ''

maior = menor = 0
for c in range(5):
    lista.append(int(input(f"Digite o {c+1}º valor: ")))
    
    if c == 0:
        maior = c
        menor = c
    else:
        if lista[len(lista)-1] > maior:
            maior = c
        if lista[len(lista)-1] < menor:
            menor = c     
          
for i,v in enumerate(lista):
    if lista[maior] == v:
        maiores.append(i)
        str_maiores+= f'{i} '
    if lista[menor] == v:
        menores.append(i)
        str_menores+= f'{i} '
        

print(f'a str_maiores é : {str_maiores}')
    
print(f'''
A sua lista é {lista}

O maior valor é {lista[maior]} {f'na posição {maior}' if len(maiores)==1 else f'nas posições {str_maiores}'}
O menor valor é {lista[menor]} {f'na posição {menor}' if len(menores)==1 else f'nas posições {str_menores}'}
''')

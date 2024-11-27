n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior=''
menor = ''

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
else:
    if (n1 < n2 and n1 < n3):
        menor = n1
        if n2 > n3:
            maior = n2
        else:
            maior = n3

if not (n1 > n2 and n1 > n3) and not (n1 < n2 and n1 < n3):
    if n2 >n3:
        maior = n2
        menor = n3
    else:
        maior = n3
        menor = n2
print(f'maior: {maior}, menor: {menor}')

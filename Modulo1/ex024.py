"""Crie um programa que leia o nome de uma cidade e verifique se ela começa com
'SANTO' """

cidade = input('Digite o nome de uma cidade: ').strip()

result = cidade[:5].upper()
print(result == 'SANTO')


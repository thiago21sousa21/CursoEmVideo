# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
#  guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#  No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

dados_pessoa = dict()
lista_pessoas = list()
while True:
    dados_pessoa['nome'] = input('Nome: ')
    while True:
        dados_pessoa['sexo'] = input('Sexo [m/f]: ').strip()[0].lower()
        if dados_pessoa['sexo'] == 'm' or dados_pessoa['sexo'] =='f':
            break
        else:
            print('Opção inválida, tente novamente')
    dados_pessoa['idade'] = int(input('Idade: '))
    lista_pessoas.append(dados_pessoa.copy())
    dados_pessoa.clear()
    
    continuar = input('Cadastrar mai uma pessoa? [s/n]: ')
    while not(continuar == 'n' or continuar == 's'):
        continuar = input('opção inválida, tente novamente: ')        
    if continuar == 'n':
        break
    elif continuar == 's':
        print('proximo...')

print()
quantidade_pessoas = len(lista_pessoas)
soma_idades = 0
lista_mulheres = []
nome_mulheres = ''
nome_pessoas_acima_media = ''
for pessoa in lista_pessoas:
    soma_idades+=pessoa['idade']
    if pessoa['sexo'] == 'f':
        lista_mulheres.append(pessoa.copy())
        nome_mulheres+= f' [{pessoa['nome']}]'
media_idades = soma_idades/quantidade_pessoas

for pessoa in lista_pessoas:
    if pessoa['idade'] > media_idades:
        nome_pessoas_acima_media+= f' [{pessoa['nome']}]'



print(lista_pessoas)
print(f'A quantidade de pessoas cadastradas foi: {quantidade_pessoas}')
print(f'A media das idades cadastradas foi: {media_idades:.2f}')
print(f'Uma lista com o nome das mulheres: {nome_mulheres}')
print(f'Uma lista com as pessoas com idade acima da média: {nome_pessoas_acima_media}')







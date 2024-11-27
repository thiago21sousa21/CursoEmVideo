# Exercício Python 56: Desenvolva um programa que leia o nome, 
# idade e sexo de 4 pessoas. 
# No final do programa, mostre: 
# a média de idade do grupo, 
# qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.


#fazer um laço que caputora as informações
# somando todas as idades pra no final fazer  a média
# fazer ifs verificando o  sexo com a idade pra pegar o homem mais velho
# fazer ifs verificando o  sexo com a idade pra pegar as mulheres com menos de 20 anos

cont_mulheres = 0
mais_velho = 0
mais_velho_nome = ''
soma_idades = 0
for pessoa in range(4):
    nome = input("Qual seu nome? ")
    idade = int(input("Qual sua idade? "))
    sexo = input("Digite m se seu sexo for masculino e f se seu sexo for feminino: ")

    if mais_velho == 0 and sexo == 'm':
        mais_velho = idade
        mais_velho_nome = nome
    if idade > mais_velho and sexo == 'm':
        mais_velho = idade
        mais_velho_nome = nome
    
    soma_idades+=idade
    
    if sexo == 'f' and idade<20:
        cont_mulheres+=1
        
print(f"A média de idade do grupo é : {soma_idades/4}")
print(f'A quantidade de mulheres menores de 20 anos é: {cont_mulheres}')
print(f'O nome do homem mais velhor é {mais_velho_nome}, com {mais_velho} anos')
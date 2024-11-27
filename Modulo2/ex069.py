# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
 
mulheres_menos_de_20 = homens = mais_de_18 = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo[M/F]: ").strip().upper()[0]
    while not (sexo in 'MF'):
        sexo = input("Digite o sexo[M/F]: ").strip().upper()[0]
    
    if(sexo == 'M'):
        homens+=1
    if idade > 18:
        mais_de_18+=1
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20+=1
    continuar = input("Cadastrar mais uma pessoa[S/N]? ").strip().upper()[0]
    if continuar == 'N':
        break
    
print(f'''temos {mais_de_18} pessoas com mais de 18 anos
      temos {homens} homens
      e temos {mulheres_menos_de_20} mulheres com menos de 20 anos''')

    
    

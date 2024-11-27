# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#pegar a data de nascimento das pessoas em um laço
from datetime import date

cont_menores = 0
cont_maiores = 0
ano_atual = date.today().year
for p in range(7):
    ano = int(input("Digite o ano de nascimento: "))
    idade = ano_atual - ano
    if(idade < 18):
        cont_menores+=1
    else:
        cont_maiores+=1
print(f"Dessas datas de nascimento temos {cont_maiores} maiores de idade e {cont_menores} menores de idade")
        
#dentro do laço já verificar a idade dela
#com duas variaveis  contadoras contar os maiores e os menores de idadde




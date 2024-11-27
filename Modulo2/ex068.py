# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

cont = 0
while True:
    opc = input("Digite se quer par ou impar [P/I]: ").strip().upper()[0]
    n = int( input("Digite seu número: "))
    
    #preciso fazer  o computador jogar o número dele
    n_maquina = randint(1, 10)
    
    soma = n + n_maquina
    par_impar = soma % 2
    
    if(opc == 'P' and par_impar == 1 or opc == 'I' and par_impar == 0):
        print(f'''Você perdeu dessa vez,
              o você escolheu {'par' if opc == 'P' else 'impar'} e o computador escolheu {n_maquina}
              como {soma} é {'par' if par_impar == 0 else 'impar'} não foi dessa vez.
              Você acumulou {cont} vitorias consecutivas''')
        break   
    cont+=1
    print(f'''Você ganhou! vc escolheru {'par' if opc == 'P' else 'impar'}
          você jogou {n} e o pc jogou {n_maquina}''')


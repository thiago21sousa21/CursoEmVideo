# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.


from random import randint

n_aleatorio  = randint(0, 10)
cont_tentativas = 1
choice = int(input("Tente a sorte e veja se consegue acertar qual número eu pensei: "))

if n_aleatorio == choice:
    print(f"você acertou! o pc escolheu {n_aleatorio} e voce escolheu {choice}")
    print(f'você acertou na {cont_tentativas}ª tentativa')
else:
    while n_aleatorio != choice:
        cont_tentativas+=1
        choice = int(input("Não foi dessa vez, tente de novo: "))
    print(f"você acertou! o pc escolheu {n_aleatorio} e voce escolheu {choice}")
    print(f'você acertou na {cont_tentativas}ª tentativa')
    
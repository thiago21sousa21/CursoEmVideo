print('Este programa é uma tabuada onde você vai digitando um númeor e surge a tabuada dele')
while True:
    n = int(input('Digite um número a ser exibida a sua tabuada(para sair digite um numero negativo):'))
    if n < 0:
        print("Você saiu.")
        break
    for c in range(9):
        print(f'{n} x {c+1} == {n*(c+1)}')
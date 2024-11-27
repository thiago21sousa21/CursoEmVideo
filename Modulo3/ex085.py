# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
#  e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.


def main():
    pai = [[],[]]
    for n in range(7):
        num = int(input("Digite um número: "))
        if num % 2 == 1:
            pai[1].append(num)
        else:
            pai[0].append(num)
   
    print(f'Os pares são: {sorted(pai[0])}')
    print(f'Os impares são: {sorted(pai[1])}')


if __name__ == '__main__':
    main()
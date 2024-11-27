# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos
# digitados em ordem crescente.

lista = []

while True:
    n = int(input("Digite um número: "))
    
    if n in lista:
        print("Esse número já esta na lista e não pode ser repitido")
    else:
        lista.append(n)
        
    continuar = input("Gostaria de cadastrar outro[s/n]? ").strip().lower()[0]    
    if continuar == 'n':
        break
    
lista.sort()

print(lista)

    
    
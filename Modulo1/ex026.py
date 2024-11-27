"""Faça um programa que leia uma frase pelo teclado e mostre
* quantas vezes aparece a letra a
* em que posição ela aparee a primeira vez
* em que posição ela aparecea ultima vez"""

frase = input('Digite uma frase: ').strip().lower()
ultimo = frase.rfind('a')
primeiro = frase.find('a')
quantidade = frase.count('a')

print("a quantidade de 'a'  é: {}".format(quantidade))
print("a posição do primeiro 'a' é: {}".format(primeiro+1))
print("a posição do ultimo 'a' é: {}".format(ultimo+1))
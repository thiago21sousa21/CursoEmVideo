#faça um programa que leia algo pelo teclado, diga o seu tipo primitivo
#e diga todas as informações dele

algo = input('Digite algo: ')

print('tipo: {}'.format(type(algo)))

print(algo.isnumeric())
print(algo.isalpha())
print(algo.isalnum())
print(algo.isupper())
print(algo.islower())
print(algo.isspace())
print(algo.istitle())
print(algo.isprintable())
print(algo.isspace())
print(algo.isascii())
print(algo.isdecimal())
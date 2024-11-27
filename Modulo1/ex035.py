reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))

forma_triangulo ="é possivel sim formar um triangulo"
nao_forma_triangulo ="não é possivel formar um triangulo"

# if not (reta1 + reta2 > reta3):
#     print(nao_forma_triangulo)
# elif not (reta2 + reta3 > reta1):
#     print(nao_forma_triangulo)
# elif not (reta3 + reta1 > reta2):
#     print(nao_forma_triangulo)
# else:
#     print(forma_triangulo)

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print("forma sim um triangulo")
    if reta1 == reta2 == reta3:
        print(f"E esse triângulo é equiláreto pois todos os lados medem {reta3}")
    elif reta1 != reta2 != reta3 != reta1:
        print(f'E esse triângulo é escaleno pois todos os lados são diferentes: {reta1}, {reta2}, {reta3}')
    else:
        print("O triangulo é isosceles pois possui dois lados iguais")
else:
    print("não forma um triangulo")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1+n2)/2
print(f'A média foi {media:.2f}')
if media < 5:
    print("Reprovado")
elif media<7:
    print("Recuperação")
else:
    print("Aprovado")
    
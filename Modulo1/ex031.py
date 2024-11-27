distancia = float(input("Digite a quantidade de quilômetros que a viagem terá: "))
valor_passagem = 0
if distancia <= 200:
    valor_passagem = distancia * 0.50
else:
    valor_passagem = distancia * 0.45
print(f"O valor da passagem sera R${valor_passagem:.2f}")
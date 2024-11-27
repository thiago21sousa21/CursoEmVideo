velocidade = float(input('Qual a velocidade atual do carro: '))

if velocidade > 80:
    diferenca = velocidade - 80
    print("Voce foi multado")
    print(f'O valor da multa é R${round(float(diferenca * 7), 2)}')
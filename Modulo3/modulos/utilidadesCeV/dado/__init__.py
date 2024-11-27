
def leiaDinheiro():
    while True:
        texto = input('Digite um valor em formato moeda, ex: R$ 15,00: ')
        if 'R$' not in texto:
            print(f'Vocẽ não digitou no formato certo, tente novamente')
        else:
            copy_texto = texto
            copy_texto = copy_texto.replace(',','.').strip()
            copy_texto = copy_texto.replace('R$','')
            if copy_texto == '':
                print(f'o texto {texto} está no formato moeda, tente novamente')
            elif type(float(copy_texto)) == float:
                print(f'o texto {texto} está no formato moeda')
                return texto
            else:
                print(f'Vocẽ não digitou no formato certo, tente novamente')

        
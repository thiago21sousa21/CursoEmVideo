ano = int(input("Digite o ano: "))
e_bissesto = ''
if ano % 4 == 0:
    e_bissesto = 'sim'
    if ano % 100 == 0:
        e_bissesto = 'não'
        if ano % 400 == 0:
            e_bissesto = 'sim'
else:
    e_bissesto = 'nao'


print(f"O ano de {ano} é bissesto? {e_bissesto}")
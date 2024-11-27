# Exercício Python 084: Faça um programa que leia nome e
#  peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:  
# A) Quantas pessoas foram cadastradas.      
# B) Uma listagem com as pessoas mais pesadas.     
# C) Uma listagem com as pessoas mais leves.

def cadastrar():
    lista = list()
    while True:
        cadastro = [input("Digite seu nome: "), float(input("Digite seu peso: "))]
        lista.append(cadastro)
        sair = input("Encerrar cadstro? [s/n] : ").strip().lower()[0]
        if sair == 's':
            return lista

def listar_maior_menor(lista):
    print(lista)
    maior_peso = menor_peso = 0
    for i,c in enumerate(lista):
        if i == 0:
            maior_peso = c[1]
            menor_peso = c[1]
        else:
            peso_atual = c[1]
            if peso_atual > maior_peso:
                maior_peso = peso_atual
            if peso_atual < menor_peso:
                menor_peso = peso_atual
    return maior_peso, menor_peso

def buscar_maiores_menores(lista, maior_peso, menor_peso):
    maiores = []
    menores = []
    for c in lista:
        peso_atual = c[1]
        nome_atual = c[0]
        if maior_peso == peso_atual:
            maiores.append(nome_atual)
        if menor_peso == peso_atual:
            menores.append(nome_atual)
    return ', '.join(maiores), ', '.join(menores)



def main():
    lista = cadastrar()
    print(f'O número de pessoas cadastradas foi: {len(lista)}')
    maior, menor = listar_maior_menor(lista)
    maiores, menores = buscar_maiores_menores(lista, maior, menor)
    print(f'''O maior peso foi: {maior}
    {maiores} pesam {maior}''')
    print(f'''O menor peso foi: {menor}
    {menores} pesam {menor}''')
    

if __name__ == '__main__':
    main()
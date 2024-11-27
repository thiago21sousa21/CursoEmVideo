def formatar_monetario (valor):
    return f'R${valor:.2f}'

def aumentar(valor, aumento):
    n_valor =(valor *(1+ aumento/100))
    return formatar_monetario(n_valor)

def diminuir(valor, desconto):
    n_valor =(valor *(1+ desconto/100))
    return formatar_monetario(n_valor)

def metade(valor):
    n_valor =(valor * 0.5)
    return formatar_monetario(n_valor)


def dobro(valor):
    n_valor =(valor * 2)
    return formatar_monetario(n_valor)

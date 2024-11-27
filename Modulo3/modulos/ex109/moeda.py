def formatar_monetario (valor):
    return f'R${valor:.2f}'


def aumentar(valor, aumento, formatar = False):
    n_valor =(valor *(1+ aumento/100))
    if formatar:        
        return formatar_monetario(n_valor)
    return n_valor
    

def diminuir(valor, desconto, formatar = False):
    n_valor =(valor *(1+ desconto/100))
    if formatar:        
        return formatar_monetario(n_valor)
    return n_valor


def metade(valor, formatar = False):
    n_valor =(valor * 0.5)
    if formatar:        
        return formatar_monetario(n_valor)
    return n_valor


def dobro(valor, formatar = False):
    n_valor =(valor * 2)
    if formatar:        
        return formatar_monetario(n_valor)
    return n_valor
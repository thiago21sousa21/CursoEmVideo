def formatar_monetario (valor):
    """
    valor: recebe um inteiro ou um float e transforma em string formato moeda 
    """
    return f'R${valor:.2f}'


def aumentar(valor, aumento, formatar = True):
    """
    valor: recebe um inteiro ou um float
    aumento: recebe um intiro ou floa que representa uma porcentagem a aumentar
    formatar: recebe um Bool, que define se os resultado vão estar formatados
    """
    n_valor =(valor *(1+ aumento/100))
    if formatar:        
        return formatar_monetario(n_valor)
    return n_valor
    

def diminuir(valor, desconto, formatar = True):
    """
    valor: recebe um inteiro ou um float
    aumento: recebe um intiro ou floa que representa uma porcentagem a diminuir
    formatar: recebe um Bool, que define se os resultado vão estar formatados
    """
    n_valor =(valor *(1- desconto/100))
    if formatar:        
        return formatar_monetario(n_valor)
    return n_valor


def metade(valor, formatar = True):
    """
    valor: recebe um inteiro ou um float
    formatar: recebe um Bool, que define se os resultado vão estar formatados

    retorna a metade do valor
    """
    n_valor =(valor * 0.5)
    if formatar:        
        return formatar_monetario(n_valor)
    return n_valor


def dobro(valor, formatar = True):
    """
    valor: recebe um inteiro ou um float
    formatar: recebe um Bool, que define se os resultado vão estar formatados

    retorna o dobro do valor
    """
    n_valor =(valor * 2)
    if formatar:        
        return formatar_monetario(n_valor)
    return n_valor

def resumo(valor, acres, desc):
    '''
    valor: inteiro ou float
    acres: int ou float a representar uma porcentagem de acrescimo
    acres: int ou float a representar uma porcentagem de desconto
    '''

    print(aumentar(valor,acres))
    print(diminuir(valor, desc))
    print(metade(valor))
    print(dobro(valor))
    
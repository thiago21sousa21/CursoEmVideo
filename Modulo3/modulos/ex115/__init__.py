def transforma_int(n=''):
    while True:
        if n == '':
            n = input('Digite um número: ')
        try:
            n = int(n)
        except:
            print('Você precisa digitar um número, tente de novo')
            n = input('Digite um número: ')
        else:
            return n

def cadastrar_pessoa(arq, nome='ninguem', idade=0):
    try:
        arquivo_aberto =  open(arq, 'at')
    except Exception as erro:
        print(erro)
    else:
        arquivo_aberto.write(f'{nome};{idade}\n')
        print(f'{nome} foi cadastrado')

def decidir_menu(opc, arq):
    if opc == 2:
        print('VOCÊ SAIU')
        return True
    elif opc ==0:
        print('CADASTRANDO NOVA PESSOA:')
        nome = input('Digite o nome: ')
        idade = transforma_int(input('Digite a idade da pessoa: '))
        cadastrar_pessoa(arq,nome, idade)
    elif opc ==1:
        print('OPÇÃO LISTAR CADASTRADOS')
        ler_arquivo(arq)
    else:
        print('Essa opção não existe, tente de novo')

def cabeçalho(texto, largura = 80):
    print(f'\033[43m{' '*largura}\033[m')
    print(f'\033[1;30;43m{texto:^{largura}}\033[m')
    #print(f'\033[43m{' '*largura}\033[m')

def arquivo_existe(nome):
    try:
        arq = open(nome,'rt')
        arq.close()
    except Exception as err:
        print(err)
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq. close()
    except Exception as err:
        print(err)

def ler_arquivo(arq):
    try:
        arquivo_aberto = open(arq, 'rt')
    except Exception as erro:
        print(erro)
    else:
        for l in arquivo_aberto:
            dados = l.split(';')
            dados[1] = dados[1].replace('\n','')
            print(f'{dados[0]} {'-'*50} {dados[1]}')


def menu():
    opcs = ['cadastrar', 'listar', 'sair']
    stop_menu = False
    name_arquivo = './ex115_arquivo_bd.txt'

    if not arquivo_existe(name_arquivo) : criar_arquivo(name_arquivo)

    while not stop_menu:
        cabeçalho('Bem vindo ao appp')

        for i,o in enumerate(opcs):
            print(f'\033[1;33m{i} {'-'*55} {o}')

        opc = transforma_int(input('Digite a opção desejada: '))
        stop_menu = decidir_menu(opc, name_arquivo)



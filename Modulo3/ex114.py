# Exercício Python 114: Crie um código em Python que
#  teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

def pudim():
    try:
        site =  urllib.request.urlopen('http://www.pudim.com.br/')
    except Exception as err:
        print(err)
    else:
        print('Pudim esta acessivel')

pudim()
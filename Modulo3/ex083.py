# Crie um programa qualquer onde o usuario digita uma expressão qualquer que use parenteses
# Seu aplicativo deverá analizar se a expressão passada está com os parenteses abertos e fechados 
# ordem correta

expressao = input('Digite uma expressão: ').strip()

lista_expressao = list(expressao)
contagem_aberto = lista_expressao.count('(')
contagem_fechado = lista_expressao.count(')')

if contagem_aberto != contagem_fechado:
    print("expressão inválida")
elif lista_expressao[0] == ')':
        print('Lista inválida')
else:
        print('Lista válida')
    
    
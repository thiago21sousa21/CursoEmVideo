#Exercício Python 105: Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e vai retornar um dicionário com 
# as seguintes informações:
# – Quantidade de notas
# – A maior nota  
# – A menor nota       
# – A média da turma   
# – A situação (opcional)


def notas(* n, sit =False):
    dados_notas= dict()
    dados_notas['maior_nota'] = max(n)
    dados_notas['menor_nota'] = min(n)
    dados_notas['media_turma'] = sum(n)/len(n)

    if sit:
        dados_notas['situacao'] = 'boa' if dados_notas['media_turma'] >= 7 else 'ruim'

    print(dados_notas)

notas(1,2,3,4,5, sit=True)


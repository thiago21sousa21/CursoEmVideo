# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos 
# e guarde tudo em uma lista composta.
#  No final, mostre um boletim contendo a média de cada um e 
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

dados_alunos = []
while True:
    dados_aluno = [input("Nome do aluno: "), float(input("1ª nota: ")), float(input("2ª nota: "))]
    media = (dados_aluno[1] + dados_aluno[2])/2
    dados_aluno.append(media)
    dados_alunos.append(dados_aluno)
    continuar = input('Cadastrar mais um? [s/n]').strip().lower()[0]
    if continuar == 'n':
        break

for dados in dados_alunos:
    print(f'Aluno: {dados[0]}, 1ª nota: {dados[1]}, 2ª nota: {dados[2]}, média: {dados[3]}')

while True:
    nome_aluno = input('Digite o nome de um aluno a ser consultado: ').strip()
    achou = False
    for d in dados_alunos:
        if nome_aluno == d[0]:
            print(f'Aluno: {d[0]}, 1ª nota: {d[1]}, 2ª nota: {d[2]}, média: {d[3]}')
            achou = True
            break
    if not achou:
        print('aluno não cadastrado')
        
    continuar = input('pesquisar mais um? [s/n]').strip().lower()[0]
    if continuar == 'n':
        break
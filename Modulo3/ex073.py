# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ("um", "dois", "três", "quatro", "cinco",
         "seis", "sete", "oito", "nove", "dez",
         "onze", "doze", "treze", "catorze", "quinze",
         "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

print(f"Os cinco primeirot times são: {times[:5]}")
print(f"Os cinco primeirot times são: {times[16:]}")
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'em que posição está o time "quinze": {times.index('quinze')+1}')

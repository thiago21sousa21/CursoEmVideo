from random import randint

pc_choice = randint(1,3)
human_choice = int(input("""
1- pedra
2- papel
3- tesoura 
digite sua opção:                         
"""))

name_pc_choice = ''
name_human_choice = ''

if pc_choice == 1:
    name_pc_choice = 'pedra'
elif pc_choice == 2:
    name_pc_choice = 'papel'
elif pc_choice ==3:
    name_pc_choice = 'tesoura'
    
if human_choice == 1:
    name_human_choice = 'pedra'
elif human_choice == 2:
    name_human_choice = 'papel'
elif human_choice ==3:
    name_human_choice = 'tesoura'    

if pc_choice == human_choice:
    print(f"EMPATE - maquina: {name_pc_choice}, você: {name_human_choice}")
elif pc_choice ==1 and human_choice == 3 or pc_choice == 2 and human_choice == 1 or pc_choice==3 and human_choice == 2:
    print(f"Você perdeu - máquina: {name_pc_choice}, você: {name_human_choice}")
else:
    print(f"Você ganhou! - máquina: {name_pc_choice}, você: {name_human_choice}")
    
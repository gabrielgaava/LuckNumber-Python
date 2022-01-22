import os
import core

def PrintNumber( str ):
    if int(str) < 10:
        return "0"+str
    
    return str

# Limpa o Terminal
def Clear():
    if os.name == 'nt': 
        return 'cls'
    else:
        return 'clear'

# Mostra as opções possiveis no programa
def Options():
    os.system(Clear())
    print("\n=============== LOTOFÁCIL - MENU ===============\n")
    print("||> - Escolha uma opção e pressione ENTER: \n")
    print("[1] - TOP 10 números ")
    print("[2] - Procurar relação númerica ")
    print("[3] - Criar jogo aleatorio (15 número) ")
    print("[4] - Inserir novo jogo ")
    print("[0] - Sair ")
    print("\n================================================\n")
    print("Sua escolha: ", end=' ')
    choosedOption = input()
    return int(choosedOption)

# Espera por um Enter para Continuar
def Continue():
    print("Pressione ENTER para continuar ...")
    input()

# Executa a função correspondente a escolhida
def RunFunction( choosedOption ):

    os.system(Clear())

    if choosedOption == 3:
        core.RandomGame()

    elif choosedOption == 2:
        core.NumberRecurrence()

    elif choosedOption == 1:
        core.topNumbers()

    elif choosedOption == 4:
        core.InsertNewGame()

    elif choosedOption == 0:
        exit()

    else:
        print("Opção não encontrada")
    
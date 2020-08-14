import os
import core

# Limpa o Terminal
def Clear():
    if os.name == 'nt': 
        return 'cls'
    else:
        return 'clear'

# Mostra as opções possiveis no programa
def Options():
    os.system(Clear())
    print("\n=============== MENU ===============\n")
    print("Escolha uma opção e pressione ENTER: \n")
    print("[1] - Criar jogo aleatorio (6 número) ")
    print("[2] - Numero aleatorio ")
    print("[3] - Reincidência de número ")
    print("[4] - TOP 5 números ")
    print("[5] - Inserir novo jogo ")
    print("[0] - Sair ")
    print("\n====================================\n")
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

    if choosedOption == 1:
        core.RandomGame()

    elif choosedOption == 2:
        core.RandomNumber()

    elif choosedOption == 3:
        core.NumberRecurrence()

    elif choosedOption == 4:
        core.topFive()

    elif choosedOption == 5:
        core.InsertNewGame()

    elif choosedOption == 0:
        exit()

    else:
        print("Opção não encontrada")
    
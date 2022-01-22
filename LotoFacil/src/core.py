import array
import random
import csv
import ui
import os
import numpy as np
from structure import LotoFacil, Ball

# List the 5 most recurrent numbers
def topNumbers():

    # Console
    print("============ TOP 10 NÚMEROS =============")
    print("|> Lendo arquivo ... ")

    games = []
    recurrence = np.zeros((60,), dtype=int)

    # Read de file and store all games
    with open('../assets/lotofacil.csv', mode='r') as csvFile:

        csvReader = csv.DictReader(csvFile)
        lineCount = 0

        for row in csvReader:

            if lineCount == 0:
                lineCount += 1

            tempGame = LotoFacil(row["id"], row["date"], row["n1"], row["n2"], row["n3"], row["n4"], row["n5"], row["n6"], row["n7"], row["n8"], row["n9"], row["n10"], row["n11"], row["n12"], row["n13"], row["n14"], row["n15"])

            games.append(tempGame)
            lineCount += 1
    
    print("|> Analisando dados ...\n")

    for game in games:
        for num in game.numbers:
            number = int(num)
            recurrence[number - 1] += 1

    topBalls = recurrence.argsort()[-10:][::-1]

    for i, ball in enumerate(topBalls):
        print("|> " + ui.PrintNumber(str(i+1))+"º:\t[Bola (" + ui.PrintNumber(str(ball+1)) + ")]\tem " + str(recurrence[ball]) + " jogos\t ("+ RecurrencePercentage(len(games), recurrence[ball]) + ")")

    print("\n")

    ui.Continue()

# Faz a leitura do CSV
def NumberRecurrence():

    print("|> Qual número deseja analisar ?")
    print("|> Número:", end=" ")

    baseNumber = int(input())
    games = []
    recurrence = np.zeros((25,), dtype=int)

    # Console
    os.system(ui.Clear())
    print("========== RELAÇÃO NÚMERICA (BOLA "+ str(baseNumber) +") ===========\n")
    print("- Lendo arquivo ... ")

    # Read de file and store all games
    with open('../assets/lotofacil.csv', mode='r') as csvFile:

        csvReader = csv.DictReader(csvFile)
        lineCount = 0

        for row in csvReader:

            if lineCount == 0:
                lineCount += 1

            tempGame = LotoFacil(row["id"], row["date"], row["n1"], row["n2"], row["n3"], row["n4"], row["n5"], row["n6"], row["n7"], row["n8"], row["n9"], row["n10"], row["n11"], row["n12"], row["n13"], row["n14"], row["n15"])

            games.append(tempGame)
            lineCount += 1
    
    print("- Analisando dados ...")
    baseNumberCount = 0

    # Count every game to analyse number recurrence
    for game in games:
        for num in game.numbers:
            number = int(num)
            # This game have ne choosed number
            if(number == baseNumber):
                baseNumberCount += 1
                # Update de recurrence array
                for num in game.numbers:
                    number = int(num)
                    if(number != baseNumber):
                        recurrence[number-1] += 1

    print("- Ordenando resultado ...\n")

    topBalls = recurrence.argsort()[-5:][::-1]

    for i, ball in enumerate(topBalls):
        print("|> " + ui.PrintNumber(str(i+1))+"º:\t[Bola (" + ui.PrintNumber(str(ball+1)) + ")]\tem " + str(recurrence[ball]) + " jogos\t ("+ RecurrencePercentage(baseNumberCount, recurrence[ball]) + ")")

    print("\n")
    ui.Continue()

# Cria um jogo (de 6 numeros)
def RandomGame():

    sortNumbers = []

    while len(sortNumbers) < 15:
        n = random.randint(1,25)
        if n not in sortNumbers:
            sortNumbers.append(n)

    print("============== JOGO SORTEADO ==============\n")

    for i in range(len(sortNumbers)):
        print("("+ui.PrintNumber(str(sortNumbers[i]))+")", end=" ")
        if((i+1) % 5 == 0):
            print("\n")

    print("===========================================\n")

    
    print("\n")
    ui.Continue()


# Insert new game register in the csv
def InsertNewGame():
        print("============ CADASTRAR JOGO =============")
        

        # Collecting data
        print("> Concurso:", end=" ")
        gameId = input()

        print("> Data:", end=" ")
        date = input()
                
        print("> Bola 01:", end=" ")
        b1 = input()

        print("> Bola 02:", end=" ")
        b2 = input()

        print("> Bola 03:", end=" ")
        b3 = input()

        print("> Bola 04:", end=" ")
        b4 = input()

        print("> Bola 05:", end=" ")
        b5 = input()

        print("> Bola 06:", end=" ")
        b6 = input()

        print("> Bola 07:", end=" ")
        b7 = input()

        print("> Bola 08:", end=" ")
        b8 = input()

        print("> Bola 09:", end=" ")
        b9 = input()

        print("> Bola 10:", end=" ")
        b10 = input()

        print("> Bola 11:", end=" ")
        b11 = input()

        print("> Bola 12:", end=" ")
        b12 = input()

        print("> Bola 13:", end=" ")
        b13 = input()

        print("> Bola 14:", end=" ")
        b14 = input()

        print("> Bola 15:", end=" ")
        b15 = input()

        with open('../assets/lotofacil.csv','a') as csvFile:
            csvFile.write("\n" + gameId + "," + date + "," + b1 + "," + b2 + "," + b3 + "," + b4 + "," + b5 + "," + b6 + "," + b7 + "," + b8 + "," + b9 + "," + b10 + "," + b11 + "," + b12 + "," + b13 + "," + b14 + "," + b15)

        print("\n\n> CADASTRO FEITO COM SUCESSO!! ")

        ui.Continue()

# Calculates the percentage of aparission number in relation of all games
def RecurrencePercentage(totalGames, recurrence):
    percentage = (recurrence * 100) / totalGames; 
    formatted_float = "{:.2f}".format(percentage)
    return str(formatted_float) + "%"

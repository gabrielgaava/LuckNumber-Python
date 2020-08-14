import array
import random
import csv
import ui
import os
import numpy as np
from structure import Game

def topFive():

    # Console
    print("============ TOP 5 NÚMEROS =============")
    print("- Lendo arquivo ... ")

    games = []
    recurrence = np.zeros((60,), dtype=int)

    # Read de file and store all games
    with open('../assets/mega.csv', mode='r') as csvFile:

        csvReader = csv.DictReader(csvFile)
        lineCount = 0

        for row in csvReader:

            if lineCount == 0:
                lineCount += 1

            tempGame = Game(row["id"], row["date"], row["n1"], row["n2"], row["n3"], row["n4"], row["n5"], row["n6"])
            games.append(tempGame)
            
            lineCount += 1
    
    print("- Analisando dados ...\n")

    for game in games:
        for num in game.numbers:
            number = int(num)
            recurrence[number - 1] += 1

    topBalls = np.argpartition(recurrence, -5)[-5:]

    for i, ball in enumerate(topBalls):
        print("> " + str(i+1)+"º: [Bola " + str(ball+1) + "]\t apareceu em " + str(recurrence[ball]) + " jogos")

    print("\n")

    ui.Continue()

# Faz a leitura do CSV
def NumberRecurrence():

    print("Qual número deseja analisar ?")
    print("> Número:", end=" ")

    baseNumber = int(input())
    games = []
    recurrence = np.zeros((60,), dtype=int)

    # Console
    os.system(ui.Clear())
    print("========== REINCIDÊNCIA DE NÚMERO ===========\n")
    print("- Lendo arquivo ... ")

    # Read de file and store all games
    with open('../assets/mega.csv', mode='r') as csvFile:

        csvReader = csv.DictReader(csvFile)
        lineCount = 0

        for row in csvReader:

            if lineCount == 0:
                lineCount += 1

            tempGame = Game(row["id"], row["date"], row["n1"], row["n2"], row["n3"], row["n4"], row["n5"], row["n6"])
            games.append(tempGame)
            
            lineCount += 1
    
    print("- Analisando dados ...")

    # Count every game to analyse number recurrence
    for game in games:
        for num in game.numbers:
            number = int(num)
            # This game have ne choosed number
            if(number == baseNumber):
                # Update de recurrence array
                for num in game.numbers:
                    number = int(num)
                    recurrence[number-1] += 1

    print("- Ordenando resultado ...\n")

    maxValue = recurrence[0]
    lastMaxValue = recurrence[0]
    maxBallNumber = 0
    lastMaxBallNumber = 0

    for i, num in enumerate(recurrence):
        if num > maxValue:
            if(i+1 != baseNumber):
                lastMaxValue = maxValue
                lastMaxBallNumber = maxBallNumber
                maxValue = num
                maxBallNumber = i
    
    print("> 1º : [Bola " + str(maxBallNumber+1) + "] - " + str(maxValue) + " repetições com a Bola " + str(baseNumber))
    print("> 2º : [Bola " + str(lastMaxBallNumber+1) + "] - " + str(lastMaxValue) + " repetições com a Bola " + str(baseNumber))
    print("> Bola " + str(baseNumber) + " apareceu em " + str(recurrence[baseNumber-1]) + " jogos\n\n")

    ui.Continue()

# Cria um jogo (de 6 numeros)
def RandomGame():

    sortNumbers = []

    for i in range(6):
        n = random.randint(1,60)
        if n not in sortNumbers:
            sortNumbers.append(n)

    print("============== JOGO SORTEADO ==============\n")
    print("> Jogo sorteado: ", end=" ")
    print(sortNumbers, end="\n\n")
    ui.Continue()

# Cria UM número aleatorio
def RandomNumber():

    n = random.randint(1,60)

    print("============== NÚMERO SORTEADO ==============\n")
    if n < 10:
        print("> Número sorteado: 0", end=str(n)+"\n\n")

    else:
        print("> Número sorteado: ", end=str(n)+"\n\n")

    ui.Continue()

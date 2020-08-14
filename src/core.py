import array
import random
import csv
import ui

class Game:
    
    # Contructor
    def __init__(self, id, date, n1, n2, n3, n4, n5, n6):
        self.id = id
        self.date = date
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6


# Faz a leitura do CSV
def ReadFile():

    with open('../assets/mega.csv', mode='r') as csvFile:

        csvReader = csv.DictReader(csvFile)
        lineCount = 0

        for row in csvReader:

            if lineCount == 0:
                print(f'{" / ".join(row)}')
                lineCount += 1

            print(f'Encontrado: {row["n1"]} {row["n2"]} {row["n3"]} {row["n4"]} {row["n5"]} {row["n6"]}.')
            
            lineCount += 1

        print(f'Processed {lineCount} lines.')
    
    ui.Continue()

# Cria um jogo (de 6 numeros)
def RandomGame():

    sortNumbers = []

    for i in range(6):
        n = random.randint(1,60)
        if n not in sortNumbers:
            sortNumbers.append(n)

    print("============== JOGO SORTEADO ==============\n")
    print("> [B1, B2, B3, B4, B5, B6]")
    print(">", end=" ")
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

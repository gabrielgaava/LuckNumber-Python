import array
import os
import ui

# Variavies de Execução
games = []

## Main
while True:
        
    os.system(ui.Clear())
    choosedOption = ui.Options()
    if choosedOption == 0:
        break

    ui.RunFunction(choosedOption)


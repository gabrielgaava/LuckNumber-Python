class Game:
    
    # Contructor
    def __init__(self, id, date, n1, n2, n3, n4, n5, n6):
        self.id = id
        self.date = date
        self.numbers = [n1, n2, n3, n4, n5, n6]

    def printAllNumber(self):
        response = ""
        for i, number in enumerate(self.numbers):
            if i == 5:
                response += str(number)
            else:
                response += str(number) + ", "

        return response

    def toArray(self):
        return [self.id, self.date] + self.numbers


class Ball:

    #Contructor
    def __init__(self, number, recurrence):
        self.number = number
        self.recurrence = recurrence
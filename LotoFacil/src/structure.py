class LotoFacil:

  def __init__(self, id, date, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15):
        self.id = id
        self.date = date
        self.numbers = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15]

  def printNumbers(self):
    response = ""
    for i, number in enumerate(self.numbers):
        if i == 14:
            response += str(number)
        else:
            response += str(number) + ", "

    return response

  def toArray(self):
        return [self.id, self.date] + self.numbers

class Ball:

    def __init__(self, number, recurrence):
        self.number = number
        self.recurrence = recurrence
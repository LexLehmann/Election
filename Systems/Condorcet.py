from Copeland import Copeland

class Condorcet:

    def run(self, input):
        copeland = Copeland()
        table = input

        outcome = copeland.run(table)
        output = []
        amountAdded = 0

        alreadyAdded = []
        for i in range(0, len(table)):
            alreadyAdded.append(0)

        while (amountAdded < len(table)):
            startAt = -1
            for i in range(0, len(outcome)):
                if isinstance(outcome[i], int):
                    if alreadyAdded[outcome[i]] == 0 and startAt == -1:
                        startAt = outcome[i]
                else:
                    for j in range(0, len(outcome[i])):
                        if alreadyAdded[outcome[i][j]] == 0 and startAt == -1:
                            startAt = outcome[i][j]

            tie = []
            tie.append(startAt)
            amountAdded += 1
            alreadyAdded[startAt] = 1

            keepGoing = True
            i = 0
            while keepGoing:
                keepGoing = False
                for val in tie:
                    for i in range(0, len(table)):
                        if table[val][i] <= 0 and alreadyAdded[i] == 0:
                            tie.append(i)
                            keepGoing = True
                            amountAdded += 1
                            alreadyAdded[i] = 1

            if len(tie) == 1:
                output.append(tie[0])
            else:
                output.append(tie)

        return output
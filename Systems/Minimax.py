from Fraction import Fraction
from Vote import Vote
from Vote import Candidate
class Minimax:
    table =[]

    def compare(self, line1, line2):
        output = 0
        i = 0
        for item in line1:
            if item > line2[i] and output == 0:
                output = 1
                break
            elif item < line2[i] and output == 0:
                output = -1
                break
            i += 1
        return output

    def run(self, input):
        table = input
        sortedTable = []
        i = 0
        for line in table:
            toAdd = []
            j = 0
            for outcome in line:
                if (j != i):
                    toAdd.append(outcome)
                j += 1
            toAdd.sort()
            sortedTable.append([i, toAdd])
            i += 1

        for i in range(0, len(sortedTable)):
            place = i
            while(place > 0 and self.compare(sortedTable[place][1], sortedTable[place - 1][1]) > 0):
                temp = sortedTable[place]
                sortedTable[place] = sortedTable[place - 1]
                sortedTable[place - 1] = temp
                place -= 1

        output = []
        for i in sortedTable:
            output.append(i[0])

        return output


    def runWithRemoval(self, input):
        table = []
        for line in input:
            row = []
            for pair in line:
                row.append(pair)
            table.append(row)

        added = []
        for line in table:
            added.append(0)
        outputSize = 0
        output = []

        while(outputSize < len(table)):
            mins = []

            i = 0
            for line in table:
                if added[i] == 0:
                    j = 0
                    min = 1
                    for pair in line:
                        if added[j] == 0 and pair < min:
                            min = pair
                        j += 1

                    mins.append([min, i])
                i += 1

            max = mins[0][0]
            for min in mins:
                if min[0] > max:
                    max = min[0]

            winners = []
            for min in mins:
                if min[0] == max:
                    winners.append(min[1])

            for person in winners:
                added[person] = 1

            outputSize += len(winners)
            if len(winners) == 1:
                output.append(winners[0])
            else:
                output.append(winners)

        return output
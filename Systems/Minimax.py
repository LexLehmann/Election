from Fraction import Fraction
from Vote import Vote
from Vote import Candidate

class Minimax:

    def run(self, input):
        votes = input

        i = 0
        candidates = []
        for tie in input[0].list:
            for option in tie:
                candidates.append(Candidate(i))
                i += 1

        table = []
        for row in candidates:
            line = []
            for col in candidates:
                line.append(0)
            table.append(line)

        i = 1
        for person in candidates:
            j = i
            while(j < len(candidates)):
                count = 0
                for vote in votes:
                    counted = False
                    k = 0
                    while not counted:
                        for choice in vote.getList()[k]:
                            if choice == person.getIdent():
                                counted = True
                                count += 1
                            if choice == j:
                                counted = True
                                count -= 1
                        k += 1

                table[person.getIdent()][j] = count
                table[j][person.getIdent()] = -1 * count
                j += 1
            i += 1

        Sorted = []

        i = 0
        for line in table:
            largestLoss = 1
            j = 0
            for compare in line:
                if compare < largestLoss and  i != j:
                    largestLoss = compare
                j += 1
            pair = [i, largestLoss]
            i += 1

            if len(Sorted) > 0 and Sorted[0][1] > pair[1]:
                j = 0
                while j < len(Sorted) and Sorted[j][1] > pair[1]:
                    j += 1
                Sorted.insert(j, pair)
            else:
                Sorted.insert(0, pair)

        output = []

        for item in Sorted:
            output.append(item[0])

        print("Minimax: " + str(output))
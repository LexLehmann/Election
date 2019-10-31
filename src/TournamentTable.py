from Fraction import Fraction
from Vote import Vote
from Vote import Candidate

class TournamentTable:

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
            while (j < len(candidates)):
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

        return table

    def simplify(self, input):
        table = []
        for line in input:
            row = []
            for pair in line:
                if pair > 0:
                    row.append(1)
                elif pair < 0:
                    row.append(-1)
                else:
                    row.append(0)
            table.append(row)
        return table

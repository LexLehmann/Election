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

                if count > 0:
                    table[person.getIdent()][j] = 1
                    table[j][person.getIdent()] = -1
                elif count < 0:
                    table[person.getIdent()][j] = -1
                    table[j][person.getIdent()] = 1
                j += 1
            i += 1
        return table
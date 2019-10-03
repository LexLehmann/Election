from Fraction import Fraction
from Vote import Vote
from Borda import Borda
from Vote import Candidate

class Baldwin:
    votes = []
    key = []

    def removeLowest(self, lowestCandidate):
        for vote in self.votes:
            i = 0
            while i < len(vote.getList()):
                j = 0
                rank = vote.getList()[i]
                while j < len(rank):
                    if rank[j] == lowestCandidate:
                        rank.remove(lowestCandidate)
                        j -= 1
                        if len(rank) == 0:
                            vote.getList().pop(i)
                            i -= 1
                    elif rank[j] > lowestCandidate:
                        rank[j] -= 1
                    j += 1
                i += 1


    def run(self, input):
        self.votes = []

        for vote in input:
            self.votes.append(Vote(vote))

        i = 0
        candidates = []
        for tie in input[0].list:
            for option in tie:
                candidates.append(Candidate(i))
                self.key.append([i, i])
                i += 1

        borda = Borda()
        output = []

        for person in candidates:
            val = 0
            ranking = borda.run(self.votes)

            if isinstance(ranking[len(ranking) - 1], int):
                val = ranking[len(ranking) - 1]
            else:
                val = ranking[len(ranking) - 1][0]

            self.removeLowest(val)

            found = False
            for pair in self.key:
                if val == pair[1] and not found:
                    val = pair[0]
                    found = True

            for pair in self.key:
                if val < pair[0]:
                    pair[1] -= 1
                if val == pair[0]:
                    pair[1] = -1

            output.insert(0, val)

        return output

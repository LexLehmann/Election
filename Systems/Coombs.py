from Fraction import Fraction
from Vote import Vote
from Plurality import ReversePlurality
from Vote import Candidate

class Coombs:
    votes = []
    key = []

    def removeFirst(self, firstCandidate):
        for vote in self.votes:
            i = 0
            while i < len(vote.getList()):
                j = 0
                rank = vote.getList()[i]
                while j < len(rank):
                    if rank[j] == firstCandidate:
                        rank.remove(firstCandidate)
                        j -= 1
                        if len(rank) == 0:
                            vote.getList().pop(i)
                            i -= 1
                    elif rank[j] > firstCandidate:
                        rank[j] -= 1
                    j += 1
                i += 1

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

        Rplur = ReversePlurality()
        output = []

        for person in candidates:
            val = 0
            ranking = Rplur.run(self.votes)

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


    def runWithRemoval(self, input):
        self.votes = []
        key = []

        for vote in input:
            self.votes.append(Vote(vote))

        i = 0
        for tie in input[0].list:
            for option in tie:
                key.append(i)
                i += 1

        coombs = Coombs()
        outcome = coombs.run(self.votes)
        del(coombs)
        output = []

        if (isinstance(outcome[0], int)):
            self.removeFirst(outcome[0])
            output.append(outcome[0])
            for i in range(0, len(key)):
                if i > outcome[0]:
                    key[i] -= 1
                elif i == outcome[0]:
                    key[i] = -1

        else:
            for person in outcome[0]:
                self.removeFirst(person)
                for i in range(0, len(key)):
                    if i > person:
                        key[i] -= 1
                    elif i == person:
                        key[i] = -1
            output.append(outcome[0])

        while(len(outcome) > 1):
            coombs = Coombs()
            outcome = coombs.run(self.votes)
            del(coombs)

            if (isinstance(outcome[0], int)):
                self.removeFirst(outcome[0])
                for i in range(0, len(key)):
                    if (outcome[0] < key[i]):
                        key[i] -= 1
                    elif (outcome[0] == key[i]):
                        key[i] = -1
                        output.append(i)
            else:
                tie = []
                for person in outcome[0]:
                    for i in range(0, len(key)):
                        if (person == key[i]):
                            key[i] = -1
                            tie.append(i)
                for person in outcome[0]:
                    for i in range(0, len(key)):
                        if person < key[i]:
                            key[i] -= 1
                for person in outcome[0]:
                    self.removeFirst(person)
                output.append(tie)


        for i in range(0, len(key)):
            if key[i] != -1:
                output.append(i)

        return output
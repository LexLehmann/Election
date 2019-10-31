from Fraction import Fraction
from Vote import Vote
from Vote import Candidate

class Borda:
    votes = []

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

    def run(self, input):
        Thisvotes = input

        i = 0
        candidates = []
        for tie in input[0].list:
            for option in tie:
                candidates.append(Candidate(i))
                i += 1

        firstVote = len(candidates) - 1

        for vote in Thisvotes:
            curVote = firstVote
            for tie in vote.getList():
                toSplit = 0
                for vote in tie:
                    toSplit += curVote
                    curVote -= 1

                amountGiven = Fraction(toSplit, len(tie))

                for vote in tie:
                    candidates[vote].addCount(amountGiven)

        output = []
        prev = 100000000000000
        for i in candidates:
            max = -1
            maxPer = 0
            for candidate in candidates:
                if candidate.getCount() > max:
                    max = candidate.getCount()
                    maxPer = candidate.getIdent()

            candidates[maxPer].setCount(-1)
            if max < prev:
                output.append(maxPer)
            else:
                if isinstance(output[len(output)-1], int):
                    output[len(output)-1] = [output[len(output)-1], maxPer]
                else:
                    output[len(output)-1].append(maxPer)
            prev = max

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

        outcome = self.run(self.votes)
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
            outcome = self.run(self.votes)

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
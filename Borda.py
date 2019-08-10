from Fraction import Fraction
from Vote import Vote
from Vote import Candidate

class Borda:

    def run(self, input):
        votes = input

        i = 0
        candidates = []
        for tie in input[0].list:
            for option in tie:
                candidates.append(Candidate(i))
                i += 1

        firstVote = len(candidates) - 1

        for vote in votes:
            curVote = firstVote
            for tie in vote.getList():
                toSplit = 0
                for vote in tie:
                    toSplit += curVote
                    curVote -= 1

                amountGiven = toSplit / len(tie)

                for vote in tie:
                    candidates[vote].addCount(amountGiven)

        output = []
        for i in candidates:
            max = 0
            maxPer = 0
            for candidate in candidates:
                if candidate.getCount() > max:
                    max = candidate.getCount()
                    maxPer = candidate.getIdent()

            candidates[maxPer].setCount(0)
            output.append(maxPer)

        print("Borda: " + str(output))

from Fraction import Fraction
from Vote import Candidate

class Formula1:

    def run(self, input):
        votes = input

        i = 0
        candidates = []
        for tie in input[0].list:
            for option in tie:
                candidates.append(Candidate(i))
                i += 1

        voteCounts = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        while (len(voteCounts) < len(candidates)):
            voteCounts.append(0)

        for vote in votes:
            curVote = 0
            for tie in vote.getList():
                toSplit = 0
                for vote in tie:
                    toSplit += voteCounts[curVote]
                    curVote += 1

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

        print("Formula 1: " + str(output))

from Fraction import Fraction
from Vote import Vote
from Plurality import Plurality
from Vote import Candidate


class Contingent:

    def run(self, input):
        votes = input

        Plur = Plurality()

        count = len(votes[0].getList()) + 1
        winners = []
        output = []

        i = 0
        for tie in votes[0].getList():
            for item in tie:
                winners.append(i)
                i += 1

        first = True
        previousCount = count
        while(count > 2):
            pluralityScore = Plur.run(votes, winners)

            count = 0
            winners = []
            for tie in pluralityScore:
                if count < 2:
                    if isinstance(tie, int):
                        winners.append(tie)
                        count += 1
                    else:
                        for candidate in tie:
                            winners.append(candidate)
                            count += 1
                else:
                    if not tie in output and first:
                        output.insert(0, tie)

            first = False
            if previousCount == count:
                return "inconclusive"
            previousCount = count

        pluralityScore = Plur.run(votes, winners)

        if isinstance(pluralityScore[0], int):
            output.insert(0, pluralityScore[1])
            output.insert(0, pluralityScore[0])
        else:
            output.insert(0, pluralityScore[0])

        return output
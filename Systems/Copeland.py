from Fraction import Fraction
from Vote import Vote
from Vote import Candidate

class Copeland:

    def run(self, input):
        count = 0
        Scores = []
        for line in input:
            i = 0
            for outcome in line:
                if outcome == 1:
                    i += 1
            pair = [count, i]
            Scores.append(pair)
            count += 1

        sorted = []
        for item in Scores:
            i = 0
            while(i < len(sorted) and item[1] < sorted[i][1]):
                i += 1
            if i < len(sorted) and item[1] == sorted[i][1]:
                if isinstance(sorted[i][0], int):
                    sorted[i][0] = [item[0], sorted[i][0]]
                else:
                    sorted[i][0].append(item[i])
            else:
                sorted.insert(i, item)

        output = []
        for pair in sorted:
            output.append(pair[0])


        print("Copeland: " + str(output))
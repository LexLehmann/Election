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

        return output

    def runWithRemoval(self, input):
        table = []
        for line in input:
            new = []
            for pairwise in line:
                new.append(pairwise)
            table.append(new)

        output = []
        outSize = 0

        last = []
        for i in table:
            last.append(0)

        while(outSize < len(table)):
            count = 0
            Scores = []
            for line in table:
                i = 0
                for outcome in line:
                    if outcome == 1:
                        i += 1
                pair = [count, i]
                Scores.append(pair)
                count += 1

            winner = [[-1, -1]]
            for pair in Scores:
                if winner[0][1] < pair[1]:
                    winner = []
                    winner.append(pair)
                elif winner[0][1] == pair[1]:
                    winner.append(pair)

            won = []
            for person in winner:
                if last[person[0]] == 0:
                    won.append(person[0])
                    last[person[0]] = 1

            if len(won) == 1:
                output.append(won[0])
                outSize += 1
            else:
                output.append(won)
                outSize += len(won)

            for person in won:
                i = 0
                for election in table[person]:
                    if election != 0:
                        table[person][i] = 0
                        table[i][person] = 0

                    i += 1


        return output
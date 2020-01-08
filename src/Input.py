from Vote import Vote

class Input:
    def readMy(self):
        inputFile = open("test.txt", "r")
        input = []
        for line in inputFile:
            next = line.strip('\n').split(" ")
            input.append(next)

        votes = []
        for voter in input:
            thisRank = []
            added = 0
            previous = 0
            while added < len(input[0]):
                minChoice = 10000
                for vote in voter:
                    if int(vote) < minChoice and int(vote) > previous:
                        minChoice = int(vote)
                tied = []
                i = 0
                for vote in voter:
                    if int(vote) == minChoice:
                        tied.append(i)
                    i += 1
                thisRank.append(tied)
                previous = minChoice
                added += len(tied)
            thisVote = Vote(thisRank)
            votes.append(thisVote)

        return votes

    def findOverVote(self):
        inputFile = open("BallotImage11315.txt", "r")
        input = []
        for line in inputFile:
            next = line.strip('\n')
            input.append(next)

        for line in input:
            if line[43] == '1':
                print(line)

    def readBallotImage(self, contestRequest):
        inputFile = open("BallotImage11315.txt", "r")
        input = []
        for line in inputFile:
            next = line.strip('\n')
            input.append(next)

        i = 0
        candidateArrayKey = []
        candidateCount = 0
        output = []

        for j in range(0,100):
            candidateArrayKey.append(-1)

        while(i < len(input)):
#            if i % 30000 == 0:
#                print(i)
            firstPick = input[i]
            secondPick = input[i+1]
            thirdPick = input[i+2]

#            print(firstPick)
#            print(secondPick)
#            print(thirdPick)

            contest = int(firstPick[0:7])
            voter = int(firstPick[7:16])
            precinct = int(firstPick[26:33])

            if contest != contestRequest:
                i += 3
                continue

            firstRank = int(firstPick[33:36])
            firstCand = int(firstPick[36:43])
            firstOver = int(firstPick[43])
            firstUnder= int(firstPick[44])

            secondRank = int(secondPick[33:36])
            secondCand = int(secondPick[36:43])
            secondOver = int(secondPick[43])
            secondUnder= int(secondPick[44])

            thirdRank = int(thirdPick[33:36])
            thirdCand = int(thirdPick[36:43])
            thirdOver = int(thirdPick[43])
            thirdUnder= int(thirdPick[44])

            if firstOver == 1 or secondOver == 1 or thirdOver == 1:
                i += 3
                continue

            vote = []

            placedInVote = []
            for j in range(0, candidateCount):
                placedInVote.append(False)

            if firstUnder != 1:
                if candidateArrayKey[firstCand] == -1:
                    candidateArrayKey[firstCand] = candidateCount
                    placedInVote.append(False)
                    for prevVote in output:
                        prevVote.getList()[len(prevVote.getList()) - 1].append(candidateCount)
                    candidateCount += 1

                if not placedInVote[candidateArrayKey[firstCand]]:
                    vote.append([candidateArrayKey[firstCand]])
                    placedInVote[candidateArrayKey[firstCand]] = True

            if secondUnder != 1:
                if candidateArrayKey[secondCand] == -1:
                    candidateArrayKey[secondCand] = candidateCount
                    placedInVote.append(False)
                    for prevVote in output:
                        prevVote.getList()[len(prevVote.getList()) - 1].append(candidateCount)
                    candidateCount += 1

                if not placedInVote[candidateArrayKey[secondCand]]:
                    vote.append([candidateArrayKey[secondCand]])
                    placedInVote[candidateArrayKey[secondCand]] = True

            if thirdUnder != 1:
                if candidateArrayKey[thirdCand] == -1:
                    candidateArrayKey[thirdCand] = candidateCount
                    placedInVote.append(False)
                    for prevVote in output:
                        prevVote.getList()[len(prevVote.getList()) - 1].append(candidateCount)
                    candidateCount += 1

                if not placedInVote[candidateArrayKey[thirdCand]]:
                    vote.append([candidateArrayKey[thirdCand]])
                    placedInVote[candidateArrayKey[thirdCand]] = True

            end = []
            j = 0
            for placed in placedInVote:
                if not placed:
                    end.append(j)
                j += 1

            vote.append(end)
            output.append(Vote(vote))
            i += 3

        for vote in output:
            if len(vote.getList()[len(vote.getList()) - 1]) == 0:
                pop(vote.getList()[len(vote.getList()) - 1])

        print(candidateArrayKey)
        return output




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


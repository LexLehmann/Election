from Vote import Vote

class Tests:

    def removeCandidate(self, input, person):
        retVotes = []

        for vote in input:
            retVotes.append(Vote(vote))

        for vote in retVotes:
            i = 0
            while i < len(vote.getList()):
                j = 0
                rank = vote.getList()[i]
                while j < len(rank):
                    if rank[j] == person:
                        rank.remove(person)
                        j -= 1
                        if len(rank) == 0:
                            vote.getList().pop(i)
                            i -= 1
                    elif rank[j] > person:
                        rank[j] -= 1
                    j += 1
                i += 1

        return retVotes

    def Conspiracy(self, input, toBeat, toWin):
        retVotes = []

        for vote in input:
            retVotes.append(Vote(vote))

        for vote in retVotes:
            foundFirst = False
            i = 0
            while i < len(vote.getList()):
                j = 0
                toWinFound = False
                toBeatFound = False
                rank = vote.getList()[i]
                while j < len(rank):
                    if toWin == rank[j]:
                        toWinFound = True
                    if toBeat == rank[j]:
                        toBeatFound = True
                    j += 1
                if not foundFirst and toWinFound:
                    break
                if toBeatFound:
                    foundFirst = True
                    rank.remove(toBeat)
                if toWinFound:
                    rank.remove(toWin)
                    break
                i += 1
            if foundFirst == True:
                vote.getList().insert(0, [toWin])
                vote.getList().append([toBeat])

        return retVotes





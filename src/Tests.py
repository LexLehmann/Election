from Vote import Vote
from STV import STV
import random

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

    def ReinforcingTest(self, votes, split):
        groups = []
        thisCopy = []
        #Change system here and lower down
        system = STV()

        for i in range(0, split):
            groups.append([])

        for vote in votes:
            thisCopy.append(Vote(vote))

        for vote in thisCopy:
            groups[random.randint(0, split - 1)].append(vote)

        groupsOutcomes = []

        for list in groups:
            ## To change system also have to check this line and lower down
            result = system.runWithRemoval(list)
            if isinstance(result[0], int):
                groupsOutcomes.append(result[0])
            else:
                groupsOutcomes.append(-1)

        totalPairs = 0
        totalMatches = 0
        for i in range(0, len(groups)):
            for j in range(0, len(groups)):
                if i != j:
                    if groupsOutcomes[i] == groupsOutcomes[j]:
                        totalPairs += 1
                        combinedList = []
                        for vote in groups[i]:
                            combinedList.append(vote)
                        for vote in groups[j]:
                            combinedList.append(vote)

                        #This is the last line to change
                        result = system.runWithRemoval(combinedList)
                        if isinstance(result[0], int):
                            if result[0] == groupsOutcomes[i]:
                                totalMatches += 1
        print("Number of same pairs : " + str(totalPairs))
        print("Number that failed reinforcement : " + str(totalPairs- totalMatches))



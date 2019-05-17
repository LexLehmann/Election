from Fraction import Fraction
from Vote import Vote
from Vote import Candidate
##from Vote import Tree

def distributeNewVotes(voter):
    for vote in voter.getList()[0]:
        newVote = voter.makeCopy()
        divs = len(newVote.getList()[0])
        newVote.getList()[0].pop(newVote.getList()[0].index(vote))

        if len(newVote.getList()[0]) == 0:
            newVote.getList().pop(0)

        newVote.cutWeight(Fraction(1, divs))

        if candidates[vote].getAccp() < 1:
            nextIter = newVote.makeCopy()
            newVote.cutWeight(candidates[vote].getAccp())
            nextIter.setWeight(voter.getWeight()- newVote.getWeight())
            distributeNewVotes(nextIter)

        if newVote.getWeight() > 0:
            candidates[vote].addNewVoter(newVote)


def removeLowest():
    minVotes = -1
    for person in candidates:
        if (minVotes == -1 or person.getCount() < candidates[minVotes].getCount()) and person.getAccp() != 0:
            minVotes = candidates.index(person)

    toTransfer = candidates[minVotes].removeCandidate()

    for vote in toTransfer:
        copy = vote.makeCopy()
        distributeNewVotes(copy)

def cutTop(threshold):
    toDistribute = []
    for person in candidates:
        if person.getCount() > threshold:
            amount = person.getCount() - threshold
            toAdd = person.getPart(amount)
            for item in toAdd:
                toDistribute.append(item)

    for vote in toDistribute:
        distributeNewVotes(vote)

def election():
    Seats = 3
    threshold = Fraction(len(votes), Seats + 1) + Fraction(1,1000)
    candidatesLeft = len(candidates)

    while candidatesLeft > Seats + 1:
        cutTopAgain = True
        while cutTopAgain:
            cutTopAgain = False
            for person in candidates:
                if person.getCount() > threshold:
                    cutTopAgain = True
            if cutTopAgain:
                cutTop(threshold)

        removeLowest()
        candidatesLeft -= 1

    lastRemoval = 0
    for person in candidates:
        if lastRemoval == 0 or (person.getCount() < lastRemoval.getCount() and person.getAccp() > 0):
            lastRemoval = person

    lastRemoval.finalRemoval()



## START ##
inputFile = open("votes.txt", "r")
input = []
for line in inputFile:
    next = line.strip('\n').split(" ")
    input.append(next)

i = 0
candidates = []
for vote in input[0]:
    candidates.append(Candidate(i))
    i += 1

votes = []
for voter in input:
    thisRank = []
    added = 0
    previous = 0
    while added < len(candidates):
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


for rank in votes:
    distributeNewVotes(rank)

election()

for candidate in candidates:
    print(candidate.getCount())

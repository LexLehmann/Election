from Fraction import Fraction
from Vote import Vote
from Vote import Candidate
##from Vote import Tree

## Takes a vote and sends it to its next choice.
# If there is a tie for first place it splits the vote into
# several fraction of votes. then puts those votes in their
# respective candidates
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
            nextIter.setWeight(nextIter.getWeight()- newVote.getWeight())
            distributeNewVotes(nextIter)

        if newVote.getWeight() > 0:
            candidates[vote].addNewVoter(newVote)

## Removes the last place candidate from the running and
# sends their votes to the next choice
def removeLowest():
    minVotes = -1
    for person in candidates:
        if (minVotes == -1 or person.getCount() < candidates[minVotes].getCount()) and person.getAccp() != 0:
            minVotes = candidates.index(person)

    toTransfer = candidates[minVotes].removeCandidate()

    for vote in toTransfer:
        copy = vote.makeCopy()
        distributeNewVotes(copy)

## Given a level to cut it down to, this will remove the fraction
# needed to get the total count down to that amount from all of the votes
# of all of the candidates over that amount. Then sends those fraction of
# votes to their next choice
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

## This is the main method that runs the election.
# The seats variable is how you set how many options can win the election
# additionalQuota is how much the threshold should be above the minimum amount
def election():
    seats = 5
    additionalQuota = Fraction(0,1000)
    accuracy = Fraction(1,100)
    threshold = Fraction(len(votes), seats + 1) + additionalQuota
    candidatesLeft = len(candidates)

    while candidatesLeft > seats + 1:
        cutTopAgain = True
        while cutTopAgain:
            cutTopAgain = False
            for person in candidates:
                if person.getCount() > threshold + accuracy:
                    cutTopAgain = True
            if cutTopAgain:
                cutTop(threshold)

        removeLowest()
        candidatesLeft -= 1
        print("one down")

    lastRemoval = 0
    for person in candidates:
        if person.getAccp() > 0 and (lastRemoval == 0 or person.getCount() < lastRemoval.getCount()):
            lastRemoval = person

    lastRemoval.finalRemoval()



## START ##
## reads in a txt file with v lines of c integers
# where v is the number of voters and c is the number of candidates
# The lowest integer is considered the most preferred choice.
# Ties are allowed. All integers over 10000 will be considered a tie for last place
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

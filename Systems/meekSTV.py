from Fraction import Fraction
from Vote import Candidate
from Vote import Vote

class Meek:
    candidates = []
    votes = []
    output = []

    ## Takes a vote and sends it to its next choice.
    # If there is a tie for first place it splits the vote into
    # several fraction of votes. then puts those votes in their
    # respective candidates. If the candidate has already won/lost
    # the amount they accept goes in and the rest moves on.
    def distributeNewVotes(self, voter):
        for vote in voter.getList()[0]:
            newVote = voter.makeCopy()
            divs = len(newVote.getList()[0])
            newVote.getList()[0].pop(newVote.getList()[0].index(vote))

            if len(newVote.getList()[0]) == 0:
                newVote.getList().pop(0)

            newVote.cutWeight(Fraction(1, divs))

            if self.candidates[vote].getAccp() < 1:
                nextIter = newVote.makeCopy()
                newVote.cutWeight(self.candidates[vote].getAccp())
                nextIter.setWeight(nextIter.getWeight()- newVote.getWeight())
                self.distributeNewVotes(nextIter)

            if newVote.getWeight() > 0:
                self.candidates[vote].addNewVoter(newVote)

    ## Removes the last place candidate from the running and
    # sends their votes to the next choice
    def removeLowest(self):
        minVotes = -1
        for person in self.candidates:
            if (minVotes == -1 or person.getCount() < self.candidates[minVotes].getCount()) and person.getAccp() != 0:
                minVotes = self.candidates.index(person)

        self.output.insert(0, minVotes)

        toTransfer = self.candidates[minVotes].removeCandidate()

        for vote in toTransfer:
            copy = vote.makeCopy()
            self.distributeNewVotes(copy)

    ## Given a level to cut it down to, this will remove the fraction
    # needed to get the total count down to that amount from all of the votes
    # of all of the candidates over that amount. Then sends those fraction of
    # votes to their next choice. Also sets the amount that candidate will accept
    # of new votes
    def cutTop(self, threshold):
        toDistribute = []
        for person in self.candidates:
            if person.getCount() > threshold:
                amount = person.getCount() - threshold
                toAdd = person.getPart(amount)
                for item in toAdd:
                    toDistribute.append(item)

        for vote in toDistribute:
            self.distributeNewVotes(vote)

    ## This is the main method that runs the election.
    # The seats variable is how you set how many options can win the election
    # additionalQuota is how much the threshold should be above the minimum amount
    #This is needed to be above 0 when there is no back and forth between two candidates
    def meekSTV(self, numOfSeats):
        seats = numOfSeats
        additionalQuota = Fraction(1, 1000)
        accuracy = Fraction(1, 100)
        threshold = Fraction(len(self.votes), seats + 1) + additionalQuota
        candidatesLeft = len(self.candidates)

        while candidatesLeft > seats + 1:
            cutTopAgain = True
            while cutTopAgain:
                cutTopAgain = False
                for person in self.candidates:
                    if person.getCount() > threshold + accuracy:
                        cutTopAgain = True
                if cutTopAgain:
                    self.cutTop(threshold)

            self.removeLowest()
            candidatesLeft -= 1
#           print("one down")

        lastRemoval = -1
        for person in self.candidates:
            if person.getAccp() > 0 and (lastRemoval == -1 or person.getCount() < lastRemoval.getCount()):
                lastRemoval = person

        self.output.insert(0, lastRemoval.getIdent())

        top = 0
        val = 0
        selected = []
        for person in self.candidates:
            if person.getCount() >= top and person != lastRemoval:
                top = person.getCount()
                val = person
                selected.append(val.getIdent())
                val.finalRemoval()

        lastRemoval.finalRemoval()

        if len(selected) == 1:
            self.output.insert(0, selected[0])
        else:
            self.output.insert(0, selected)


    ## START ##
    ## reads in a txt file with v lines of c integers
    # where v is the number of voters and c is the number of candidates
    # The lowest integer is considered the most preferred choice.
    # Ties are allowed. All integers over 10000 will be considered a tie for last place
    def run(self, input, seats):

        self.votes = []
        for ballot in input:
            self.votes.append(Vote(ballot))

        i = 0
        for tie in input[0].list:
            for option in tie:
                self.candidates.append(Candidate(i))
                i += 1

        for rank in self.votes:
            self.distributeNewVotes(rank)

        self.meekSTV(seats)

        return self.output
#       for candidate in self.candidates:
#           print(candidate.getCount())
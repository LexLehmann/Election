from meekSTV import Meek
from Borda import Borda
from Vote import Vote
from Copeland import Copeland
from Condorcet import Condorcet
from TournamentTable import TournamentTable
from F1 import Formula1
from Plurality import Plurality
from Plurality import ReversePlurality
from Minimax import Minimax
from Baldwin import Baldwin
from Bucklin import Bucklin
from Contingent import Contingent

inputFile = open("votes.txt", "r")
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

TournamentTable = TournamentTable()
pairTable = TournamentTable.run(votes)
tourtable = TournamentTable.simplify(pairTable)
del(TournamentTable)

Plur = Plurality()
print("Plurality: " + str(Plur.run(votes)))

print("Plurality with Removal: " + str(Plur.runWithRemoval(votes)))
del(Plur)

Borda = Borda()
print("Borda: " + str(Borda.run(votes)))

print("Borda with Removal: " + str(Borda.runWithRemoval(votes)))
del(Borda)

f1 = Formula1()
print("Formula 1: " + str(f1.run(votes)))
del(f1)

RPlur = ReversePlurality()
print("Reverse Plurality: " + str(RPlur.run(votes)))

print("Reverse Plurality with Removal: " + str(RPlur.runWithRemoval(votes)))
del(RPlur)

condorcet = Condorcet()
print("Condorcet: " + str(condorcet.run(tourtable)))
del(condorcet)

cope = Copeland()
print("Copeland: " + str(cope.run(tourtable)))

print("Copeland with Removal: " + str(cope.runWithRemoval(tourtable)))
del(cope)

mm = Minimax()
print("Minimax: " + str(mm.run(pairTable)))

print("Minimax with Removal: " + str(mm.runWithRemoval(pairTable)))
del(mm)

baldwin = Baldwin()
print("Baldwin: " + str(baldwin.run(votes)))

print("Baldwin With Removal: " + str(baldwin.runWithRemoval(votes)))
del(baldwin)

contingent = Contingent()
print("Contingent: " + str(contingent.run(votes)))

meek = Meek()
print("Meek STV: " + str(meek.run(votes, 2)))

bucklin = Bucklin()
print("Bucklin with 50% threshold: " + str(bucklin.run(votes, 1)))

print("---- requires number of seats ----")
seats = 2

#meek = Meek()
#print("Meek STV: " + str(meek.run(votes, seats)))

bucklin = Bucklin()
print("Bucklin: " + str(bucklin.run(votes, seats)))

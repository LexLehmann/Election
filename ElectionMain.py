from meekSTV import Meek
from Borda import Borda
from Vote import Vote
from Copeland import Copeland
from TournamentTable import TournamentTable
from F1 import Formula1
from Plurality import Plurality
from Minimax import Minimax
from Baldwin import Baldwin
from Bucklin import Bucklin

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

Pur = Plurality()
Pur.run(votes)

meek = Meek()
meek.run(votes)

borda = Borda()
print("Borda: " + str(borda.run(votes)))

f1 = Formula1()
f1.run(votes)

TournamentTable = TournamentTable()
table = TournamentTable.run(votes)

cope = Copeland()
cope.run(table)

mm = Minimax()
mm.run(votes)

bucklin = Bucklin()
print("Bucklin: " + str(bucklin.run(votes)))

baldwin = Baldwin()
print("Baldwin: " + str(baldwin.run(votes)))

print(table)

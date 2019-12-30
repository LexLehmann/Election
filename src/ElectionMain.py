from meekSTV import Meek
from Borda import Borda
from Input import Input
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
from STV import STV
from Coombs import Coombs
from Tests import Tests

input = Input()
votes = input.readMy()

tests = Tests()
votes = tests.Conspiracy(votes, 0, 1)

TournamentTable = TournamentTable()
pairTable = TournamentTable.run(votes)
tourtable = TournamentTable.simplify(pairTable)
del(TournamentTable)

Plur = Plurality()
print("Plurality:                      " + str(Plur.run(votes)))

print("Plurality with Removal:         " + str(Plur.runWithRemoval(votes)))
del(Plur)

Borda = Borda()
print("Borda:                          " + str(Borda.run(votes)))

print("Borda with Removal:             " + str(Borda.runWithRemoval(votes)))
del(Borda)

f1 = Formula1()
print("Formula 1:                      " + str(f1.run(votes)))
del(f1)

RPlur = ReversePlurality()
print("Reverse Plurality:              " + str(RPlur.run(votes)))

print("Reverse Plurality with Removal: " + str(RPlur.runWithRemoval(votes)))
del(RPlur)

condorcet = Condorcet()
print("Condorcet:                      " + str(condorcet.run(tourtable)))
del(condorcet)

cope = Copeland()
print("Copeland:                       " + str(cope.run(tourtable)))

print("Copeland with Removal:          " + str(cope.runWithRemoval(tourtable)))
del(cope)

mm = Minimax()
print("Minimax:                        " + str(mm.run(pairTable)))

print("Minimax with Removal:           " + str(mm.runWithRemoval(pairTable)))
del(mm)

baldwin = Baldwin()
print("Baldwin:                        " + str(baldwin.run(votes)))

print("Baldwin With Removal:           " + str(baldwin.runWithRemoval(votes)))
del(baldwin)

contingent = Contingent()
print("Contingent:                     " + str(contingent.run(votes)))

stv = STV()
print("STV with Removal :              "  + str(stv.runWithRemoval(votes)))

coombs = Coombs()
print("Coombs with Removal :           "  + str(coombs.runWithRemoval(votes)))

bucklin = Bucklin()
print("Bucklin with 50% threshold:     " + str(bucklin.run(votes, 1)))

#print("---- requires number of seats ----")
#seats = 2

meek = Meek()
print("Meek STV:                       " + str(meek.run(votes, 1)))


#bucklin = Bucklin()
#print("Bucklin: " + str(bucklin.run(votes, seats)))
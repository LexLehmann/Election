from Fraction import Fraction
from Vote import Vote
from Borda import Borda
from Vote import Candidate

class Bucklin:
    def run(self, input):
        votes = input

        i = 0
        output = []
        candidates = []
        for tie in input[0].list:
            for option in tie:
                candidates.append(Candidate(i))
                i += 1

        for time in candidates:
            for voter in votes:
                count = 0
                i = 0
                while(count+len(voter.list[i]) <= time.getIdent()):
                    count += len(voter.getList()[i])
                    i += 1

                amount = 1/len(voter.list[i])
                for choice in voter.list[i]:
                    candidates[choice].addCount(amount)

            majority = len(votes)/2
            nextChoice = -1

            for person in candidates:
                if person.getCount() >= majority and person.getAccp() == 1:
                    nextChoice = person.getIdent()
                    person.setAccp(0)
                    majority = person.getCount()

            if nextChoice != -1:
                output.append(nextChoice)
                     
            while(nextChoice != -1):
                nextChoice = -1
                majority = Fraction(len(votes), 2)
                for person in candidates:
                    if person.getCount() >= majority and person.getAccp() == 1:
                        nextChoice = person.getIdent()
                        person.setAccp(0)
                        majority = person.getCount()

                if nextChoice != -1:
                    output.append(nextChoice)

        return output

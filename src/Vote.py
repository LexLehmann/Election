from Fraction import Fraction

#the class that holds a vote and the choices the vote made and
# hw much power this vote has
class Vote:
    #Vote initializer if no weight sent sets it to 1
    def __init__(self, voteData, w = None):
        if isinstance(voteData, list):
            self.list = voteData
            if w != None:
                self.weight = w
            else:
                self.weight = Fraction(1,1)
        else:
            self.list = []
            for tie in voteData.getList():
                newTie = []
                for item in tie:
                    newTie.append(item)
                self.list.append(newTie)
            self.weight = voteData.weight


    #returns the vote's choices
    def getList(self):
        return self.list

    #adds the second votes weight to the current's weight
    #this should only happen when votes' choices are identical
    def __add__(self, other):
        self.weight += other.weight
        return self

    #returns the weight of this vote
    def getWeight(self):
        return self.weight

    #gives a vote a total weight
    def setWeight(self, val):
        self.weight = val

    #given a fraction this multiplies the vote value by that fraction
    #used for taking a part from a vote
    def cutWeight(self, amount):
        self.weight = self.weight * amount

    #given a choice in the vote it removes that choice from the vote
    def removeChoice(self, toRemove):
        for rank in self.list:
            for choice in rank:
                if toRemove == choice:
                    rank.pop(choice)
                    if len(rank) == 0:
                        self.list.pop(rank)

    #returns a copy of the current vote.
    #needed when votes split into parts that can
    #have choices removed in different orders
    def makeCopy(self):
        copyList = []
        for rank in self.list:
            copyRank = []
            for choice in rank:
                copyRank.append(choice)
            copyList.append(copyRank)
        return Vote(copyList, self.weight)

    #gives the sense if two votes have the same chioices
    def __eq__(self, other):
        returnVal = True
        i = 0
        if len(self.list) != len(other.list):
            returnVal = False
        else:
            for rank in self.list:
                if len(rank) != len(other.list[i]):
                    returnVal = False
                elif returnVal:
                    j = 0
                    for choice in rank:
                        if choice != other.list[i][j]:
                            returnVal = False
                        j += 1
                i += 1
        return returnVal

    #Gives a concept of order to  the votes to allow
    #binary searching
    #first gives order based on the length of the vote
    #then on each set of ranks it first checks length, then
    #if a larger vote comes first
    #since votes will be added such that each rank is sorted
    # this will never make mistakes
    def __lt__(self, other):
        returnVal = False

        if len(self.list) > len(other.list):
            returnVal = False
        elif len(other.list) > len(self.list):
            returnVal = True
        else:
            lockedIn = False
            i = 0
            for rank in self.list:
                if not lockedIn and len(rank) > len(other.list[i]):
                    returnVal = False
                    lockedIn = True
                elif not lockedIn and len(rank) < len(other.list[i]):
                    returnVal = True
                    lockedIn = True
                elif not lockedIn:
                    j = 0
                    for choice in rank:
                        if not lockedIn and choice > other.list[i][j]:
                            returnVal = False
                            lockedIn = True
                        elif not lockedIn and choice < other.list[i][j]:
                            returnVal = True
                            lockedIn = True
                        j += 1
                i += 1
        return returnVal

# A node for the tree has a vote as the data and other data
# to make the tree work
class Node:
    #defines a node everything that needs to be changed is changed in the tree
    def __init__(self, Vote):
        self.vote = Vote
        self.parent = 0
        self.left = 0
        self.right = 0
        self.avl = 0

#the tree that holds the votes so that if a vote is a copy can be
# quickly determined
class Tree:
    #tree starts non existant
    def __init__(self):
        self.root = 0

    #returns root of the tree. Will return 0 if the tree doesn't have any nodes
    def getRoot(self):
        return self.root

    #given a vote it adds it to the tree
    #if the tree is empty makes the root node for the vote
    #if an idenical vote is already in the tree it combines their power
    #otherwise puts the vote in the correct spot and makes a node for it
    #then it rebalances the tree using the avl method
    def insert(self, vote):
        if self.root == 0:
            newRoot = Node(vote)
            self.root = newRoot
        else:
            cur = self.root
            while(cur != 0 and cur.vote != vote):
                prev = cur
                if(cur.vote < vote):
                    cur = cur.left
                else:
                    cur = cur.right

            if cur != 0:
                cur.vote = cur.vote + vote

            else:
                newNode = Node(vote)
                newNode.parent = prev
                if prev.vote < vote:
                    prev.left = newNode
                else:
                    prev.right = newNode

                cur = prev
                prev = newNode

                while cur != 0 and (prev.avl != 0 and prev != newNode):
                    if cur.left == prev:
                        cur.avl -= 1
                    else:
                        cur.avl += 1

                    if cur.avl == 2:
                        if prev.avl < 0:
                            self.rightLeftRot(cur)
                            print("RL")
                        else:
                            self.leftRot(cur)
                            print("L")
                    elif cur.avl == -2:
                        if prev.avl < 0:
                            self.rightRot(cur)
                            print("R")
                        else:
                            self.leftRightRot(cur)
                            print("LR")

                    prev = cur
                    cur = cur.parent

    #roates the tree to the right moving top down to the right
    def rightRot(self, top):
        par = top
        v = top.left

        v.parent = par.parent
        par.left = v.right
        v.right = par
        par.parent = v

        v.avl = 0
        par.avl = 0

        if self.root == par:
            self.root = v

    #roates the tree to the left moving top down to the left
    def leftRot(self, top):
        par = top
        v = top.right

        v.parent = par.parent
        par.right = v.left
        v.left = par
        par.parent = v

        v.avl = 0
        par.avl = 0

        if self.root == par:
            self.root = v

    #handles the other rotates
    def leftRightRot(self, top):
        case = 0
        if top.left.right.avl == -1:
            case = 1
        elif top.left.right.avl == -1:
            if top.left.right.right.avl == -1:
                case = 2
            else:
                case = 3

        self.leftRot(top.left)
        self. rightRot(top)

        if case == 1:
            top.avl = -1
        elif case == 2:
            top.parent.left.avl = 1
        elif case == 3:
            top.parent.left.avl = -1


    def rightLeftRot(self, top):
        case = 0
        if top.right.left.avl == 1:
            case = 1
        elif top.right.left.avl ==  -1:
            if top.right.left.left.avl == 1:
                case = 2
            else:
                case = 3

        self.rightRot(top.right)
        self.leftRot(top)

        if case == 1:
            top.avl = -1
        elif case == 2:
            top.parent.right.avl = 1
        elif case == 3:
            top.parent.right.avl = -1

    #returns an inorder list of all of the votes from cur down
    def inOrder(self, cur):
        list = []
        if cur != 0:
            if cur.left != 0:
                left = self.inOrder(cur.left)
                for item in left:
                    list.append(item)
            list.append(cur.vote)
            if cur.right != 0:
                right = self.inOrder(cur.right)
                for item in right:
                    list.append(item)
        return list

    #returns an inorder list of all of the votes from cur down but the votes it returns
    #are all the fraction amount that was passed in of the orginal vote.
    #it also reduces the wieght of each vote by the amount it took out
    def inOrderTakePart(self, cur, amount):
        list = []
        if cur.left != 0:
            left = self.inOrderTakePart(cur.left, amount)
            for item in left:
                list.append(item)
        sendBack = cur.vote.makeCopy()
        sendBack.cutWeight(amount)
        cur.vote.setWeight(cur.vote.getWeight() - sendBack.getWeight())
        list.append(sendBack)
        if cur.right != 0:
            right = self.inOrderTakePart(cur.right, amount)
            for item in right:
                list.append(item)
        return list

#this holds the dara for each candidate
#each candidate has a tree that holds all of their votes
#an idenitfying number, a total votes so far and the amount they are accepting
#accpeting will be 1 if they are still trying to win 0 if they have lost and inbetween if thay have won
class Candidate:
    #gives the candidate no votes and a 1 accepting along with a number
    def __init__(self, i):
        self.idenifier = i
        self.count = 0
        self.partyVoters = Tree()
        self.accepting = Fraction(1,1)

    def getIdent(self):
        return self.idenifier

    def addCount(self, val):
        self.count += val

    def setCount(self, val):
        self.count = val

    #given a voter it adds that vote to the candidates count
    def addNewVoter(self, vote):
        self.partyVoters.insert(vote)
        self.count += vote.weight

    #cuts a candidate from the running makes them no longer accept votes
    # and returns all of their voters to be redistributed
    # also deletes their votes
    def removeCandidate(self):
        list = self.partyVoters.inOrder(self.partyVoters.getRoot())
        self.partyVoters = 0
        self.accepting = Fraction(0,1)
        self.count = 0
        return list

    #the last removal. Since the election is ending these voters don't need
    #to be returned and redistributed
    #helps with votes that have run out of options breaking the distribution method
    def finalRemoval(self):
        self.partyVoters = 0
        self.accepting = 0
        self.count = 0

    #takes a fraction, amount, from every voter in a candidate and returns them
    #also cuts the amount they accept and their count by the same amount
    def getPart(self, amount):
        self.cutAccepting((self.count-amount)/self.count)
        self.count = self.count - amount
        return self.partyVoters.inOrderTakePart(self.partyVoters.getRoot(), amount/(self.count + amount))

    def getAccp(self):
        return self.accepting

    def getCount(self):
        return self.count

    def setAccp(self, val):
        self.accepting = val

    #cuts the current amount the candidate accepts by the passed in fraction
    def cutAccepting(self, amount):
        self.accepting = self.accepting * amount
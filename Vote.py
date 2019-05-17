from Fraction import Fraction

class Vote:
    def __init__(self, voteData, w = None):
        self.list = voteData
        if w != None:
            self.weight = w
        else:
            self.weight = Fraction(1,1)

    def getList(self):
        return self.list

    def __add__(self, other):
        self.weight += other.weight
        return self

    def getWeight(self):
        return self.weight

    def setWeight(self, val):
        self.weight = val

    def cutWeight(self, amount):
        self.weight = self.weight * amount

    def removeChoice(self, toRemove):
        for rank in self.list:
            for choice in rank:
                if toRemove == choice:
                    rank.pop(choice)
                    if len(rank) == 0:
                        self.list.pop(rank)

    def makeCopy(self):
        copyList = []
        for rank in self.list:
            copyRank = []
            for choice in rank:
                copyRank.append(choice)
            copyList.append(copyRank)
        return Vote(copyList, self.weight)



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


class Node:
    def __init__(self, Vote):
        self.vote = Vote
        self.parent = 0
        self.left = 0
        self.right = 0
        self.avl = 0

class Tree:
    def __init__(self):
        self.root = 0

    def getRoot(self):
        return self.root

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

    def inOrder(self, cur):
        list = []
        if cur != 0:
            if cur.left != 0:
                self.inOrder(cur.left)
            list.append(cur.vote)
            if cur.right != 0:
                self.inOrder(cur.right)
        return list

    def inOrderTakePart(self, cur, amount):
        list = []
        if cur.left != 0:
            self.inOrderTakePart(cur.left, amount)
        sendBack = cur.vote.makeCopy()
        sendBack.cutWeight(amount)
        cur.vote.setWeight(cur.vote.getWeight() - sendBack.getWeight())
        list.append(sendBack)
        if cur.right != 0:
            self.inOrderTakePart(cur.right, amount)
        return list


class Candidate:
    def __init__(self, i):
        self.idenifier = i
        self.count = 0
        self.partyVoters = Tree()
        self.accepting = Fraction(1,1)

    def addNewVoter(self, vote):
        self.partyVoters.insert(vote)
        self.count += vote.weight

    def removeCandidate(self):
        list = self.partyVoters.inOrder(self.partyVoters.getRoot())
        self.partyVoters = 0
        self.accepting = Fraction(0,1)
        self.count = 0
        return list

    def finalRemoval(self):
        self.partyVoters = 0
        self.accepting = 0
        self.count = 0

    def getPart(self, amount):
        self.count = self.count - amount
        return self.partyVoters.inOrderTakePart(self.partyVoters.getRoot(), amount/(self.count + amount))

    def getI(self):
        return self.idenifier

    def getAccp(self):
        return self.accepting

    def getCount(self):
        return self.count

    def setAccp(self, val):
        self.accepting = val
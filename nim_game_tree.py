"""
This programs creates and prints out
a minimax tree for the game of Nim
"""

def main():
    
    validInput = False
    while validInput == False:  # only break if input is valid
        pile = input("Choose your initial size of the pile. Should be more than 2: ")
        try:    # check if input is int
            pile = int(pile)
        except:
            pass
        else:
            if pile > 2:    # check if input larger than 2
                validInput = True   # break the loop
            else:
                pass
            
    root = Minimax([pile], "MAX")   # initiate root
    root.build(root.state)  # build tree
    root.printTree("", True)    #(indentation, check if last child of node)
                    


class Minimax:
    # represents a single node of the tree
    def __init__(self, nimState, minMaxLevel):
        # construcor for Minimax
        self.state = nimState   # list
        self.level = minMaxLevel    # string (Max/Min)
        self.child = [] # list of child nodes
        
    def addChild(self, state, level):
        # create child node and addd to child list
        # state is current stae of child
        # level is MAX/MIN
        node = Minimax(state, level)
        self.child.append(node)
    
    def split(self, toSplit):
        # splits given list
        lst = []
        for num in toSplit:
            if num>2:   # smaller than 2 if left as original 
                subList = self.subSplit(num)    #split individual int
                for lists in subList:
                    newList = list(toSplit) # copy of original list
                    index = newList.index(num)  # index of int that split
                    newList.pop(index) # remove int from original(copy)
                    # replace with split state of int
                    for item in lists:
                        newList.append(item)
                    newList.sort()
                    if newList not in lst:  # avoid repeat 
                        lst.append(newList)
        return sorted(lst)
        
    def subSplit(self, num):
        # splits individual integers 
        # cannot split in half
        subList = []
        if num<=2:
            # don't split if not more than 2
            subList.append(num)
        else:
            counter = 1 # tracks number of times split
            if num%2 == 0:  # for even int
                half = num/2
            else:   # for odd int
                half = (num//2)+1
            while counter < half:  # can also use for loop
                difference = num - counter
                subList.append([counter, difference])   # possible states
                counter += 1
        return sorted(subList)
    
    def printTree(self, indentation, last):
        # prints tree in folder format 
        # recursive function 
        print(indentation, end="")
        if last:
            print(" \-", end="")    # marks last child of node
            indentation += "   "
        else:   # if not last child
            print(" + ", end="") 
            indentation += " | "    # level of tree
        print(self.state, end=" ")  # possible split.
        # no new line as might need to print level if last child
        if last:
            print(self.level)   # print level for last child
        else:
            print()
        for child in self.child:
            last = False
            # check if last child
            if child==self.child[-1]:
                last = True
            child.printTree(indentation, last)  # recursion 
       
    def build(self, lst):
        # build tree recusively 
        if self.canSplit(lst):    # check if list can split more
            possibilities = self.split(lst)   # list       
            # decide level of child
            if self.level == "MAX":
                childLevel = "MIN"
            else:
                childLevel = "MAX"     
            for state in possibilities:
                # add child for every possible state
                self.addChild(state, childLevel)
            for child in self.child:
                # continue building for every child
                child.build(child.state)    # recursion           
        else:   # if can't split more
            return               
            
    def canSplit(self, lst):
        # check if list can be split
        # need alteast a singe int
        # more than 2 to split
        can = False
        for num in lst:
            if num>2:
                can = True
        return can
            

main()
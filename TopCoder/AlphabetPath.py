# Given a array of lists find consequtive alphabetical letters either
# horizontally, vertically or diagonally

'''
Example 1: 4
ABE         AB*
CFG         C**
BDH         *D*
ABC         ***

Example 2: 1
A

Example 3: 0 (No A)
BCDEFGHIJKLMNOP

Example 4: 2
CDBA    **BA

Example 5: 3
EDCCBA      ****BA
EDCCBA      ***C**

Example 6: 26
AMNOPA      *MNOP*
ALEFQR      *LEFQR
KDABGS      KDABGS
AJCHUT      *JCHUT
AAIWVA      **IWV*
AZYXAA      *ZYX**

'''

class Stack:
    def __init__(self):
        self.items = []
        self.numItems = 0

    def pop(self):
        self.numItems -= 1
        return self.items.pop()


    def push(self, elem):
        self.numItems += 1
        self.items.append(elem)

    def peek(self):
        return self.items[self.numItems-1]

class Graph:

    def __init__(self):





class Vertex:


def alphaPath(pathList):

    AlphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    alphaStack = Stack()

    for letter in reversed(AlphabetList):
        # print(letter)
        alphaStack.push(letter)

    currLetter = alphaStack.peek()

    # Assign index to each element
    concatPathList = list(''.join(pathList))

    numLetters = 6

    alphaPaths = []

    for lineStrIndex in range(0, len(pathList)):

        lineList = pathList[lineStrIndex]

        for letterIndex in range(0, len(lineList)):

            if currLetter == lineList[letterIndex]:

                print(str(currLetter) + " : " + str(lineStrIndex*numLetters + letterIndex) + "\n")

                # Create a Graph and add Neighbors
                newAlphaPath = []




            else:
                print("")
    return



pathList = ["AMNOPA", "ALEFQR", "KDABGS", "AJCHUT", "AAIWVA", "AZYXAA"]
alphaPath(pathList)
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

class Vertex:
    def __init__(self, gridNum):
        self.id = gridNum
        self.connectedTo = []
        self.alphaValue = ''

    def addNeighbor(self, nbrVert):
        self.connectedTo.append(nbrVert)

    def getId(self):
        return self.id

    def getGridNum(self):
        return self.gridNum

class Graph:

    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0

    def getAllVertices(self):
        return self.vertexList.keys()

    def getVertex(self, getVert):

        if getVert in self.vertexList:
            return self.vertexList[getVert]

        else:
            return None

    def getNumVertices(self):
        return self.numVertices

    def addVertex(self, gridNum):

        self.numVertices += 1

        newVertex = Vertex(gridNum)

        self.vertexList[gridNum] = newVertex

        return newVertex

    # Only add Edge if neighbors are a consecutive alphabetical key
    def addEdge(self, vert1Key, vert2Key):

        if vert1Key not in self.vertexList:
            newVertex = self.addVertex(vert1Key)

        if vert2Key not in self.vertexList:
            newVertex = self.addVertex(vert2Key)

        self.vertexList[vert1Key].addNeighbor(self.vertexList[vert2Key])

def alphaPath(pathList):

    AlphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    alphaStack = Stack()

    alphaDict = {"A":"B", "B":"C", 'C':'D', 'D':'E', 'E':'F', 'F':'G', 'G':'H', 'H':'I', 'I':'J', 'J':'K', 'K':'L', 'L':'M', 'M':'N', 'N':'O', 'O':'P', 'P':'Q', 'Q':'R', 'R':'S', 'S':'T', 'T':'U', 'U':'V', 'V':'W', 'W':'X', 'X':'Y', 'Y':'Z'}

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
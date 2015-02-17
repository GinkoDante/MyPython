'''
We will follow the rules defined below:

Using the information from above we can define four rules as follows:

1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
2. If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
3. If the current token is a number, set the root value of the current node to the number and return to the parent.
4. If the current token is a ')', go to the parent of the current node.
'''

import operator

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == None

    def size(self):
        count = 0

        for item in self.items:
            count += 1

        return count

    def peek(self):

        size = len(self.items)

        return self.items[size - 1]

class BinaryTreeNode():

    def __init__(self, val):
        self.key = val
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, leftValue):

        if self.leftChild == None:

            self.leftChild = BinaryTreeNode(leftValue)

        else:
            newLeftChild = BinaryTreeNode(leftValue)
            newLeftChild.LeftChild = self.leftChild
            self.leftChild = newLeftChild


    def insertRightChild(self, rightValue):

        if self.rightChild == None:

            self.rightChild = BinaryTreeNode(rightValue)

        else:
            newRightChild = BinaryTreeNode(rightValue)
            newRightChild.rightChild = self.rightChild
            self.rightChild = newRightChild


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getValue(self):
        return self.key

    def setRootVal(self, newValue):
        self.key = newValue

    def getRootVal(self):
        return self.key



def buildParseTree(exprString):

    exprList = exprString.split()

    # Collection of Nodes
    exprTree = BinaryTreeNode('')

    # Use a Stack to keep record of Nodes visited
    nodeStack = Stack()
    # Add rootNode to Stack
    nodeStack.push(exprTree)

    currNode = exprTree

    for token in exprList:

        if token == "(":

            currNode.insertLeftChild('')

            nodeStack.push(currNode)

            # Point reference to the left child
            currNode = currNode.getLeftChild()

        elif token in ['+', '*', '-', '/']:

            # Set value of current node as operator
            currNode.setRootVal(token)

            # Create a right Child
            currNode.insertRightChild('')

            # Push Node to Stack
            nodeStack.push(currNode)

            # Point reference to the right child
            currNode = currNode.getRightChild()

        elif token == ")":
            # Go to root Node
            currNode = nodeStack.pop()

        # Operands
        else:
            # Set value of current nodes value to the operand
            currNode.setRootVal(token)

            # return to parent Node
            currNode = nodeStack.pop()

    return exprTree

def printTree(parseTree, levelNum):

    currNode = parseTree

    # print(currNode.getRootVal())

    leftNode = currNode.getLeftChild()
    rightNode = currNode.getRightChild()

    levelNum += 1

    if leftNode and rightNode:
        print(currNode.getRootVal())
        return print(printTree(leftNode, levelNum), printTree(rightNode, levelNum))

    else:
        newLine = levelNum*"\n"
        return currNode.getRootVal() + newLine


def evaluateParseTree(parseTree):

    operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}


    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()


    if rightChild and leftChild:

        fn = operators[parseTree.getRootVal()]
        return fn(evaluateParseTree(leftChild), evaluateParseTree(rightChild))

    else:
        return int(parseTree.getRootVal())

# Use an inorder Traversal to print
def printEvalString(parseTree):

    if parseTree:
        # Print left subtree
        strVal = "(" + printEvalString(parseTree.getLeftChild())

        # Print the parent Node
        strVal = strVal + str(parseTree.getRootVal())

        # Print right subtree
        strVal = strVal + printEvalString(parseTree.getRightChild())

    return strVal

expr = "( ( 10 + 5 ) * 3 )"

parseTree = buildParseTree(expr)

printTree(parseTree, 0)

print("Result of expression " + str(expr) + " is " + str(evaluateParseTree(parseTree)))




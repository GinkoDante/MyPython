__author__ = 'Bill Lee'

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

    def preorderTraverse(self):

        print(self.key)

        if self.leftChild:
            self.leftChild.preorderTraverse()

        if self.rightChild:
            self.rightChild.preorderTraverse()

    def postorderTraverse(self):

        if self.leftChild:
            self.leftChild.postorderTraverse()

        if self.rightChild:
            self.rightChild.postorderTraverse()

        print(self.key)


# Traverse tree by going from root and
# recursively checking left subtree followed by right subtree

def preorder_Traversal(parseTree):

    if parseTree:
        print(parseTree.getRootVal())
        return preorder_Traversal(parseTree.getLeftChild())
        return preorder_Traversal(parseTree.getRightChild())


def postorder_Traversal(parseTree):

    if parseTree != None:
        return preorder_Traversal(parseTree.getLeftChild())
        return preorder_Traversal(parseTree.getRightChild())
        print(parseTree.getRootVal())
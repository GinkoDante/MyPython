# BinarySearchTree: Way to map a key to a value
# Provides efficient searching by
#   categorizing values as larger or smaller without
#   knowing where the value is precisely placed
# Build Time: O(n)
# Search Time: O(log n)

# BST Methods:
'''
    Map(): Create a new, empty map
    put(key,val): Add a new key, value pair to the map.
        If already in place then replace old values

    get(key): Find the key in search tree and return value
    del: remove key-value in map using del map[key]
    len():Return the number of key-value pairs in the map
    in: return True/False if key found in map

'''

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

class TreeNode:
    # Python optional parameters: Use these values if none passed on initialization
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    # Is this Node a left or right child to its parent?
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # Rott Node only node without a parent Node
    def isRoot(self):
        return not self.parent

    # Leaf Nodes: No children Nodes
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        # Update parent reference of this node's children
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
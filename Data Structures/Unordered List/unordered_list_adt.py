# Lists can best be expressed using Linked Lists
# Each element is a node with a reference to the next element in the List

class Node:

    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, nextNode):
        self.next = nextNode


# The Unordered List contains the head of the list which points the the initial Node
# List class itself does not contain any node objects
class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # Additions to the List ensures he last element added is the first in the List
    def add(self, item):
        # Create a new Node object
        temp = Node(item)
        # Point this Node to what the head points to
        temp.setNext(self.head)
        # Set the head to point to this new Node
        self.head = temp

    # Return the number of Nodes in list
    def size(self):

        count = 0

        # Create a node to iterate List of Nodes
        currNode = self.head

        while currNode != None:
            count += 1
            currNode = currNode.getNext()

        return count

    # Continue looking at values until it is found or we run out of Nodes to check
    def search(self, item):

        currNode = self.head

        found = False

        while currNode != None and not found:

            if currNode.getData() == item:
                found = True

            else:
                currNode = currNode.getNext()

        return found

    # Remove needs to find the Node in the List just as search does but also
    # edit the Node prior to the Node to be deleted to point to The Nodes to
    # removes Next reference
    def remove(self, item):

        priorNode = None

        currNode = self.head

        found = False

        while currNode != None and not found:

            if currNode.getData() == item:
                found = True

            else:
                priorNode = currNode
                currNode = currNode.getNext()

        # If the first Node after the head is to be deleted then set the head to pint
        # to next Node
        if found:
            if priorNode == None:
                self.head = currNode.getNext()

            else:
                priorNode.setNext(currNode.getNext())

    # Add a node to the end of the List
    def append(self, item):
        # Add puts the most current node at the head
        appendNode = Node(item)

        # Create a node to iterate List of Nodes
        currNode = self.head

        while currNode.getNext() != None:
            currNode = currNode.getNext()

        currNode.setNext(appendNode)


    # Return the value at the specified position
    def index(self, index):
        # Create a node to iterate List of Nodes
        currNode = self.head

        while index > 0:
            currNode = currNode.getNext()
            index -= 1

        return currNode.getData()

    def insert(self, item, index):
        # Put an element at the specified index
        # Create a node to iterate List of Nodes
        insertNode = Node(item)

        # Automatically point to the first Node
        currNode = self.head

        index -= 1

        while index > 0:
            currNode = currNode.getNext()
            print("CurNode : " + str(currNode.getData()))
            index -= 1


        saveRef = currNode.getNext()

        print("SaveRef: " + str(saveRef.getData()))
        currNode.setNext(insertNode)
        insertNode.setNext(saveRef)

    # Remove and return the last Node
    def pop(self):

        # Create a node to iterate List of Nodes
        currNode = self.head

        while currNode.getNext() != None:
            currNode = currNode.getNext()

        return currNode

mylist = UnorderedList()
# Add: places the item at the head of the list
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
# Append: places the item at the tail of the list
mylist.append(89)
mylist.append(11)
mylist.insert(99, 2)
mylist.insert(3, 4)

i = 0
while i < mylist.size():
    print("%d " %mylist.index(i))
    i += 1

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
mylist.remove(9)
print(mylist.size())
print(mylist.search(93))
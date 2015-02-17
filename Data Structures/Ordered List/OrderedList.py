class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, nextNode):
        self.next = nextNode


class OrderedList():

    def __init__(self):
        # Create a variable which points to a Node
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):

        count = 0
        currNode = self.head

        while currNode != None:
            count += 1
            currNode = currNode.getNext()

        return count

    # We can stop search in ordered list as soon as value which is greater is found
    def search(self, searchVal):

        currNode = self.head

        found = False

        stopSearch = False

        while not found and not stopSearch and currNode != None:

            if currNode.getData() == searchVal:
                found = True

            else:

                if currNode.getData() > searchVal:
                    stopSearch = True

                else:
                    currNode = currNode.getNext()

        return found

    def remove(self, remVal):
        # Find the item to remove in list
        priorNode = None
        currNode = self.head

        found = False
        stopSearch = False

        while currNode != None and not found and not stopSearch:

            if currNode.getData() == remVal:
                found = True

            else:
                if currNode.getData() > remVal:
                    stopSearch = True

                else:
                    priorNode = currNode
                    currNode = currNode.getNext()


        if found:
            if priorNode == None:
                # First currNode is to be removed
                self.head = currNode.getNext()

            else:
                # Point prior Node to the next Node after current Node
                priorNode.setNext(currNode.getNext())

        else:
            pass

    # We must add values to list in correct order
    def add(self, addVal):

        # Point prior Node to the next Node after current Node
        addNode = Node(addVal)

        # Find where new value to be add should be placed
        priorNode = None
        currNode = self.head

        stopSearch = False

        # If we find a larger node then we can place add Node between
        # previous and current
        while currNode != None and not stopSearch:

            if currNode.getData() > addVal:
                # Insert the new Node here
                stopSearch = True


            else:
                priorNode = currNode
                currNode = currNode.getNext()

        # The add Node should be the head Node
        if priorNode == None:
            addNode.setNext(currNode)
            self.head = addNode

        # Otherwise addNode to stopSearch position
        else:
            priorNode.setNext(addNode)
            addNode.setNext(currNode)

    def index(self, index):

        currNode = self.head

        # Get value at the index
        while index > 0:
            currNode = currNode.getNext()
            index -= 1

        return currNode.getData()


mylist = OrderedList()
# Add: places the item at the head of the list
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
# Append: places the item at the tail of the list
#mylist.append(89)
#mylist.append(11)
#mylist.insert(99, 2)
#mylist.insert(3, 4)

i = 0
while i < mylist.size():
    print("%d " %mylist.index(i))
    i += 1
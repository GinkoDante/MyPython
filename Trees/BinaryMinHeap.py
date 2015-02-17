__author__ = 'Bill Lee'

# Binary Min Heap keeps the smallest value as the root of the tree
# We must check if nw children are less than parent and percolate up if so

class BinMinHeap():

    def __init__(self):
        self.heapList = [0]
        self.size = 0

    #                                         0 1 2 3 4
    # We build heap by taking a list such as [9,6,5,2,3]
    def buildHeap(self, valList):

        # Set initial index to middle item
        index = len(valList) // 2

        self.size = len(valList)

        # Make 0 the first element of heapList
        self.heapList = [0] + valList[:]

        # Put smallest node from child position into root position
        while index > 0:
            self.percolateDown(index)
            index -= 1

    # O(log n)
    def insert(self, newNode):
        self.heapList.append(newNode)
        self.size += 1
        self.percolateUp()

    def percolateUp(self):

        # Percolate most recent addition up the tree
        recentInsertIndex = self.size - 1

         # Check recent node against parent
        while recentInsertIndex // 2 > 0:

            # Check if recent Node value is less than parent Node
            if self.heapList[recentInsertIndex] < self.heapList[recentInsertIndex // 2]:

                #  Swap these heapList values in list
                temp = self.heapList[recentInsertIndex]
                self.heapList[recentInsertIndex] = self.heapList[recentInsertIndex // 2]
                self.heapList[recentInsertIndex // 2] = temp

            recentInsertIndex = recentInsertIndex // 2

    # To remove the minimum value we just need to delete the root value
    # at index 1
    # To restore our heap we will start by pushing last Node to the root position
    # and then percolating that value down the heap into the correct position
    def delMin(self):

        minVal = self.heapList[1]

        # Copy last node's value to root position
        self.heapList[1] = self.heapList[self.size]

        # Reduce size of minHeap
        self.size = self.size - 1

        # Pop last value off of heapList
        self.heapList.pop()

        # Percolate new root down to its correct position
        self.percolateDown(1)

        return minVal

    def percolateDown(self, index):

        # While we are not at the bottom of the list then
        while (index*2) <= self.size:

            # Get the child index whose values is currently the smallest
            minChildIndex = self.minChild(index)

            if self.heapList[index] > self.heapList[minChildIndex]:
                # Swap these values
                temp = self.heapList[index]
                self.heapList[index] = self.heapList[minChildIndex]
                self.heapList[minChildIndex] = temp

            # Set index to the smallest child even if no swap occurred
            index = minChildIndex

    # Look at both children and return the index of whichever is smaller
    def minChild(self, index):

        # If we are at the end of the heaplist and no right child
        if index*2+1 > self.size:
            # return left Child index
            return index * 2

        else:
            # Compare value at each of these child indexes
            if self.heapList[index*2] < self.heapList[index*2+1]:
                return index*2

            else:
                return index*2+1


bh = BinMinHeap()
bh.buildHeap([9,5,6,2,3])
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
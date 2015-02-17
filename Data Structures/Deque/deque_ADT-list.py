
# Deque Data Structure
# We can add and remove elements from both the rear and front

class Deque:
    def __init__(self):
        self.items = []

    # O(1) Operation
    def addFront(self, item):
        self.items.append(item)

    # O(n) operation to shift other elements to the right
    def addRear(self, item):
        self.items.insert(0, item)

    # O(1) Operation
    def removeFront(self):
        return self.items.pop()

    # O(n) operation to shift other elements to the left
    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


d=Deque()
print(d.isEmpty())
d.addRear(4)
print(d.items)
d.addRear('dog')
print(d.items)
d.addFront('cat')
print(d.items)
d.addFront(True)
print(d.items)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removeRear())
print(d.items)
print(d.removeFront())
print(d.items)
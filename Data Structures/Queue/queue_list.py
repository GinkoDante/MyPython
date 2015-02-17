# Queue Abstract Dta Type Implementation using Primitive List Data Type

# Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(str(q.items))
q.dequeue()
print(str(q.items))
q.enqueue("Hello")
print(str(q.items))
q.dequeue()
print(str(q.items))
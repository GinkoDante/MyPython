# Palindrome: Word that is the same forward as it is backwards
# Examples: radar, madam, toot

# We can use a deque to get a string from the rear and from the front
# and compare to see if the strings ae the same
# If they are the same then the word is a palindrome

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


def PalindromeChecker(checkWord):

    rearDeque = Deque()

    for letter in checkWord:
        rearDeque.addRear(letter)

    stillEqual = True

    while rearDeque.size() > 1 and stillEqual:
        if rearDeque.removeRear() == rearDeque.removeFront():
            stillEqual = True
        else:
            stillEqual = False

    return stillEqual

print(PalindromeChecker("radar"))
print(PalindromeChecker("cook"))
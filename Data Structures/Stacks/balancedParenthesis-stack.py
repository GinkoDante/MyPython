# Check that for every open parenthesis "(" their is a corresponding close parenthesis ")"
# (((((()))))): Balanced
# (((()(((): Unbalanced

# Stack Data Structure
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        popItemIndex = len(self.items)-1
        return self.items[popItemIndex]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def parenthesisChecker(string):

    stack = Stack()
    index = 0
    balanced = True

    while index < len(string) and balanced:
        if string[index] == "(":
            stack.push(string[index])

        else:
            # Try to put an ) on the empty stack
            if stack.isEmpty():
                balanced = False

            # Stack has an "(" to remove
            else:
                stack.pop()

        index += 1

    # STack should be empty now and still balanced
    if stack.isEmpty() and balanced:
        return True
    else:
        return False

# Algorithm

balanced = "((((()))))"

unbalanced = "(((())("


print("Is the string \"" + balanced + "\" balanced? ")
print(parenthesisChecker(balanced))

print("Is the string \"" + unbalanced + "\" balanced? ")
print(parenthesisChecker(unbalanced))





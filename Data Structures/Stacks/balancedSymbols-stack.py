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

def SymbolChecker(symbolString):

    stack = Stack()
    index = 0
    balanced = True

    while index < len(symbolString) and balanced:
        '''
        if string[index] == "(":
            stack.push(string[index])

        else if string[index] == "[":
            stack.push(string[index])

        else if string[index] == "{":
            stack.push(string[index])
        '''
        symbol = symbolString[index]

        if symbol in "([{":
            stack.push(symbolString[index])

        else:
            # Try to put an ) on the empty stack
            if stack.isEmpty():
                balanced = False

            # Check to see if this symbol is the correct closing symbol
            else:
                if SymbolMatches(stack.peek(), symbolString[index]):
                    stack.pop()
                else:
                    balanced = False

        index += 1

    # STack should be empty now and still balanced
    if stack.isEmpty() and balanced:
        return True
    else:
        return False

def SymbolMatches(open, close):
    '''
    if stackChar == "(":
        if symbolChar == ")":
            return True
        else:
            return False

    else if stackChar == "[":
        if symbolChar == "]":
            return True
        else:
            return False

    else if stackChar == "{":
    if symbolChar == "}":
        return True
    else:
        return False
    '''

    openSymbols = "{[("
    closeSymbols = "}])"

    return openSymbols.index(open) == closeSymbols.index(close)

# Algorithm

balanced = "{{([][])}()}"

unbalanced = "[{()]"


print("Is the string \"" + balanced + "\" balanced? ")
print(SymbolChecker(balanced))

print("Is the string \"" + unbalanced + "\" balanced? ")
print(SymbolChecker(unbalanced))





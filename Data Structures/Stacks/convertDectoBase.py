# We can use a stack to convert Decimal Numbers
# of base 10 to any other base (up to 16 here) using a rule
# were the remainder of a number by the wanted base gets pushed to the stack
# and the division of the number continues until we get to 0.

# Popping the elements off of the stack then gives the correct sequence for value
# in the specified base

# Example: Convert number 233 in base 10 to base 2:
# a. 233 % 2 = 1, 233 // 2 = 116            Stack: 1
# b. 116 % 2 = 0, 116 // 2 = 58             Stack: 1, 0
# c. 58 % 2 = 0, 58 // 2 = 29               Stack: 1, 0, 0
# d. 29 % 2 = 1, 29 // 2 = 14               Stack: 1, 0, 0, 1
# e. 14 % 2 = 0, 14 // 2 = 7                Stack: 1, 0, 0, 1, 0
# f. 7 % 2 = 1, 7 // 2 = 3                  Stack: 1, 0, 0, 1, 0, 1
# g. 3 % 2 = 1, 3 // 2 = 1                  Stack: 1, 0, 0, 1, 0, 1, 1
# h. 1 % 2 = 1, 1 // 2 = 0  ==> STOP        Stack: 1, 0, 0, 1, 0, 1, 1, 1 (Top of Stack)
# Binary value is received by popping values off of stack:  11101001

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

def baseConverter(decNumber, wantedBase):

    # Create a list to hold digits whose index correspond to a max 16 character base
    digits = "0123456789ABCDEF"

    newBaseStack = Stack()

    while decNumber > 0:
        newBaseDigit = decNumber % wantedBase

        # print(newBaseDigit)

        newBaseStack.push(newBaseDigit)

        decNumber = decNumber // wantedBase

    newBaseString = ""

    print(newBaseStack.items)

    while not newBaseStack.isEmpty():
        baseDigit = newBaseStack.items.pop()
        print(baseDigit)
        newBaseString = newBaseString + digits[baseDigit]

    return newBaseString


print(baseConverter(25,2))
print(baseConverter(25,16))
print(baseConverter(25,8))
print(baseConverter(256,16))
print(baseConverter(122,6))
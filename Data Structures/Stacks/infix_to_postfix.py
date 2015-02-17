# Infix Expression:     A+B*C        (A+B)*C     A+B*C+D   (A+B)*(C+D)  A*B+C*D    A+B+C+D

# Group every two operands and then perform the operation pre or postfixed
# Prefix Expression: +[A*[BC]]     *[+[AB]C]     ++A*BCD    *+AB+CD     +*AB*CD     +++ABCD
# PostFix Expression: [A[BC]*]+     [[AB]+C]*     ABC*+D+   AB+CD+*     AB*CD*+     AB+C+D+

# Prefix: Add all parenthesis to infix and replace left parenthesis with operator,
# delete right parenthesis

# Postfix: Add all parenthesis to infix and replace right parenthesis with operator,
# delete left parenthesis

# Convert  (A + B) * C - (D - E) * (F + G) to postfix and prefix
# a. Fully Parenthesize:
#           (((A + B) * C) - ((D - E) * (F + G)))
# Prefix:   -*+ABC*-DE+FG       # Replace closest left parenthesis with operator
# Postfix:   AB+C*DE-FG+*-      # Replace closest right parenthesis with operator

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        popItemIndex = len(self.items)-1
        return self.items[popItemIndex]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def infixToPostfix(infixString):

    # Define operators and precedence value using a dictionary
    opPrec = {}

    opPrec["*"] = 3
    opPrec["/"] = 3
    opPrec["+"] = 2
    opPrec["-"] = 2
    opPrec["("] = 1

    openParenthesis = "("
    closeParenthesis = ")"

    # Use stack to hold operators
    opStack = Stack()

    # Convert Infix espression string into a list
    infixList = infixString.split()

    postfixList = []

    for token in infixList:

        if token == openParenthesis:
            opStack.push(token)

        elif token == closeParenthesis:
            # remove all operators from stack up until open parenthesis is found
            while opStack.peek() != openParenthesis:
                # Append all operators to postfix List
                postfixList.append(opStack.items.pop())
            # Remove the open parenthesis
            opStack.pop()

        elif token in "+-/*":
            # print("Token found: "+ token)
            # Compare to other operators on stack to pop any operators with higher
            # or equal precedence
            while (not opStack.isEmpty()) and (opPrec[opStack.peek()] >= opPrec[token]):

                popItem = opStack.pop()

                # print("Item popped from stack: " + str(popItem))

                postfixList.append(popItem)

            # Push token onto stack after all higher operators removed
            opStack.push(token)

            print("opStack: " + str(opStack.items))

        # Place all operands into postfixList
        else:
            postfixList.append(token)

    # Add all remaining operators to postfix
    while (not opStack.isEmpty()):

        postfixList.append(opStack.pop())

    #print(postfixList)

    return " ".join(postfixList)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


















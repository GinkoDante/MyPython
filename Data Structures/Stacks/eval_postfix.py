# Wwe can evaluate postfix expressions by using a Stack
# to keep track of the operands to be operated upon.

# When we reach an operator (+/-*) then pop the top two operands
# off the stack and perform the operation putting the result back at the top
# of the Stack until only one operand is left as the result

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def popTop(self):
        return self.items.pop()

    def peek(self):
        popItemIndex = len(self.items)-1
        return self.items[popItemIndex]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def PostFixEval(postfixString):

    # Split string into an iterable collection list
    postfixList = postfixString.split()

    # Create stack to hold operands
    operandStack = Stack()

    # Put operands on stack
    # Pop off 2 top to perform operation
    # Returns result of all operations
    for token in postfixList:

        # Trigger: Operator found in postFix List
        # Action: Pop top two opernads from operandStack and perform operation
        #         Add result of operation to the top of the stack
        # Result: Result value at the top of the stack
        if token in "+-/*":

            secondOperand = operandStack.popTop()
            firstOperand = operandStack.popTop()

            if token == "+":
                result = firstOperand + secondOperand
            elif token == "-":
                result = firstOperand - secondOperand
            elif token == "*":
                result = firstOperand * secondOperand
            else:
                result = firstOperand / secondOperand

            # Put result at the top of the Stack
            operandStack.push(result)

        # Trigger: token is not an operator then it is an operand
        # Action: Add operand to the stack
        # Result: most recently found operand added to the top of the stack
        else:
            operandStack.push(int(token))
            print("Stack: " + str(operandStack.items))

    # Final result should be last remaining element on the Stack
    result = operandStack.popTop()
    return result

print(PostFixEval('7 8 + 3 2 + /'))
print(PostFixEval('17 10 + 3 * 9 /'))
print(PostFixEval('25 10 + 25 + 10 + 2 / 5 - 2 /'))


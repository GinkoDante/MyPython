# Here we see that Python prioritizes the fast pop() off of the end of a list
import timeit

# Define popFirst as x.pop(0)
popFirst = timeit.Timer("x.pop(0)", "from __main__ import x")

# Define popLast as x.pop()
popLast = timeit.Timer("x.pop()", "from __main__ import x")

# x is a list of 2 million elements
x = list(range(2000000))

# Repeat popLast 1000 times
popLast.timeit(number=1000)

# x is a list of 2 million elements
x = list(range(2000000))

# Repeat popFirst 1000 times
popFirst.timeit(number=1000)
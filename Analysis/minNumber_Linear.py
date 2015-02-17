# Linear: O(n) implementation of finding the min number in a list

import time
from random import randrange

def minNumber_Linear(listNumbers):

    minNumber = listNumbers[0]

    # Use a single for loop
    for i in listNumbers:
        if minNumber > i:
            minNumber = i

    return minNumber

'''
listNumbers = [17,4,36,48,19,52,2,10,91]
min = minNumber_Linear(listNumbers)
print("The minimum number is " + str(min))
'''

# Generate random lists of 1,000 - 100,000 Numbers in the range of (0, 9,999)
for listSize in range(1000, 100001, 1000):
    listNumbers = [randrange(100000) for x in range(listSize)]

    start = time.time()
    print(minNumber_Linear(listNumbers))
    end = time.time()

    print("size: %d time: %f" % (listSize, end-start))
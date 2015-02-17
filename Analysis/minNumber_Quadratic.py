# Quadratic: O(n^2) implementation of finding the min number in a list
import time
from random import randrange

def minNumber_Quadratic(listNumbers):

    minNumber = listNumbers[0]

    # Use a nested for loop to get a Quadratic function
    for i in listNumbers:
        for j in listNumbers:
            # If we find any smaller number then move on to the next value in array
            if i > j:
                # Skip the else statement and go to first for loop
                break

        else:
            minNumber = listNumbers[i]

    return minNumber

'''
ALTERNATIVE using Booleans
def minNumber_Quadratic(listNumbers):

    minNumber = listNumbers[0]

    # Use a nested for loop to get a Quadratic function
    for i in listNumbers:

        # Assume is is the smallest value for now
        isSmallest = True

        for j in listNumbers:
            # If we find any smaller number then set boolean to False
            if i > j:
                isSmallest = False

        # If i is still considered smallest then set it to the minNumber
        if isSmallest:
            minNumber = i

    return minNumber
'''

#listNumbers = [17,4,36,48,19,52,2,10,91]
#min = minNumber_Quadratic(listNumbers)

#print("The minimum number is " + str(min))

# Generate random lists of 1,000 - 100,000 Numbers in the range of (0, 9,999)
for listSize in range(1000, 100001, 1000):
    listNumbers = [randrange(100000) for x in range(listSize)]

    start = time.time()
    print(minNumber_Quadratic(listNumbers))
    end = time.time()

    print("size: %d time: %f" % (listSize, end-start))
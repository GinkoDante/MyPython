# Here we will compare the contains() method for a list and a dictionary.
# contains(): Tests if value is within the primitive data structure

# For a list contains is an O(n) operation
# For a dictionary contains() is an O(1) operation

import timeit
import random

# For i values from ten thousand to 1 million incrementing by 20 thousand
for i in range(10000, 1000001, 20000):

    # Get a random number in range of 0 to i to test if it is in the data structure x
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random,x")

    # Recreates list as long as i for each iteration of for loop
    x = list(range(i))

    list_time = t.timeit(number=1000)

    # ReCreate a dictionary as long as i for each iteration of for loop
    x = {j:None for j in range(i)}

    dict_time = t.timeit(number=1000)

    print("%d,%10.3f,%10.3f" % (i, list_time, dict_time))
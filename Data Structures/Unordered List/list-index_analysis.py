# The Python List primitive data structure is programmed to be a O(1) operation
# We will verify by timing a run of various list sizes looking for the index of random values

import timeit
import random

for i in range(10000, 1000001, 20000):

    # Recreates list as long as i for each iteration of for loop
    x = list(range(i))

    # Get a random number in range of 0 to i to test if it is in the list x
    t = timeit.Timer("x.index(random.randrange(%d))"%i, "from __main__ import random,x")

    list_time = t.timeit(number=1000)

    print("%d,%10.3f" % (i, list_time))



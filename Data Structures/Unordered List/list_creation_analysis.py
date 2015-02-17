import timeit

# Python lists prioritize indexing

# These following operations are all valid ways to add elements to a list
# but some are much faster than others

def concat():

    timelist = []

    for i in range(1000):
        timelist = timelist + [i]

def append():

    timelist = []

    for i in range(1000):
        timelist.append(i)

def listComprehend():
    timelist = [i for i in range(1000)]


def initialize():
    timelist = list(range(1000))


# We can use timeit to capture the amount of time it takes to execute each of these functions
concatTime = timeit.Timer("concat()", "from __main__ import concat")
print("concat(): ", concatTime.timeit(number=1000), "milliseconds")

appendTime = timeit.Timer("append()", "from __main__ import append")
print("append(): ", appendTime.timeit(number=1000), "milliseconds")

listCompTime = timeit.Timer("listComprehend()", "from __main__ import listComprehend")
print("listComprehend(): ", listCompTime.timeit(number=1000), "milliseconds")

initializeTime = timeit.Timer("initialize()", "from __main__ import initialize")
print("initialize(): ", initializeTime.timeit(number=1000), "milliseconds")
# The Brute Force method would be to take the StringA and find all possible
# permutations until we find one which matches stringB

# This would be n! possibilities which is greater than an exponential function!

def anagramDetect_BruteForce(stringA, stringB):

    listA = list(stringA)

    permIndex = 0

    numPermutations = Factorial(len(listA))

    permutationList = listofPerms(stringA, numPermutations)

    permFound = False

    for permutation in permutationList and not permFound:

        if permutation == stringB:
            permFound = True

    return permFound

# Returns integer for the factorial of n
def Factorial(n):

    if n > 0:
        n * Factorial(n-1)

# Return a list of all permutations of string
def listofPerms(strtoPermute, numPermutations):

    listtoPermute = list(strtoPermute)

    permList = []

    permList.append(listtoPermute)

    letter1Index = 0

    letter2Index = 1

    while numPermutations > 0:

        while letter1Index < len(listtoPermute):


            while letter2Index < len(listtoPermute):

                # swap two letters as long as not the same index
                temp = letter1Index


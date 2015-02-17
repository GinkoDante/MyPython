# We can also sort each of the strings and then compare their values
# to test if the strings are anagrams

def anagramDetect_Sorting(stringA, stringB):

    #Convert both immutable strings to lists
    listA = list(stringA)
    listB = list(stringB)

    # Sort using Pythons function
    listA.sort()
    listB.sort()

    continueSearch = True
    index = 0

    # Compare the two lists
    while index < len(listA) and continueSearch:

        if listA[index] != listB[index]:
            continueSearch = False

        else:
            index += 1

    return continueSearch

print(anagramDetect_Sorting('abcd', 'dcba'))
# Anagrams are words which have all of the same letters in different positions
# Example: steam => teams

# Given a string we can convert to a list and for each matching letter convert list element into a
# None primitive type

def anagramDetect_Quadratic(stringA, stringB):

    listB = list(stringB)

    anagramTest = True

    indexA = 0

    while indexA < len(stringA) and anagramTest:

        letterFound = False

        # Start at the beginning of the list each time
        indexB = 0

        while indexB < len(listB) and not letterFound:

            # If we find match set bool letterFound to True
             if stringA[indexA] == listB[indexB]:
                 letterFound = True
            # Otherwise keep searching
             else:
                 indexB += 1

        # Since we stop a the found letter through condition in while loop we can assign to
        # None here at the correct index
        if letterFound:
            listB[indexB] = None

        else:
            anagramTest = False

        indexA += 1

    return anagramTest


print(anagramDetect_Quadratic('abcd','dcba'))
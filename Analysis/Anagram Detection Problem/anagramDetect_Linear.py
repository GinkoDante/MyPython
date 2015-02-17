# The Linear approach resolves around counting the number of occurrences of each letter
# and comparing these dictionaries for both words to one another


def anagramDetect_Linear(stringA, stringB):

    # Create List of 26 elements where each index
    # represents the letters alphabetical position
    # a = 0, b = 1, c = 2, d = 3
    # The values at each index indicate the number of occurrences of each letter in te string
    listA = [0]*26
    listB = [0]*26

    # count the number of occurrences of each letter in stringA
    for charIndex in range(len(stringA)):

        # Returns the alphabetical index for each letter of stringA
        alphaIndex = ord(stringA[charIndex]) - ord('a')
        # Increment the value at this letters alphabetical Index in list
        listA[alphaIndex] = listA[alphaIndex] + 1

    # count the number of occurrences of each letter in stringB
    for charIndex in range(len(stringB)):
        # Returns the alphabetical index for each letter of stringA
        alphaIndex = ord(stringB[charIndex]) - ord('a')
        # Increment the value at this letters alphabetical Index in list
        listB[alphaIndex] = listB[alphaIndex] + 1

    # We need to compare both listA and listB to see if they match
    continueTest = True

    index = 0

    while index < len(listA) and continueTest:

        if listA[index] != listB[index]:
            continueTest = False

        else:
            index += 1

    return continueTest

print(anagramDetect_Linear('apple','pleap'))
print(anagramDetect_Linear('apple','pl'))
print(anagramDetect_Linear('dog','godd'))
print(anagramDetect_Linear('trick','kcirt'))
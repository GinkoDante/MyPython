# Define a method which can construct a string of length N with K pairs of AB
'''
Example 1: N = 3, K = 2 => "AAB"
Example 2: N = 2, K = 0 => "BA"
Example 3: N = 5, K = 8 => ""
Example 4: N = 10, K = 12 => "AAAAAABBAA"
'''

def ABStrGen(N,K):

    # Create a list of initially all 'A' of length n
    pairList = []

    for num in range(N):

        pairList.append('A')

    # print(pairList)

    # Begin adding B charaters to the end of the the list by deteming the number of pairs
    # which would be generated
    numB = 1
    numA = N-1

    maxNumB = 1

    max_NumPairs = numB * numA

    strFound = False

    while not strFound:

        while max_NumPairs < K:

            # Increment the number of B's and decrement number of A's then try again
            numB += 1
            numA -= 1

            max_NumPairs = numB * numA

            if numA == 0:
                pairList = []
                print(pairList)
                return

        # Place B's into end of list
        startBIndex = N - numB
        endBIndex = N - 1

        for elem in range(startBIndex, N):
            pairList[elem] = 'B'

        print(pairList)

        print("B Start Index: " + str(startBIndex) + "\nB End Index: " + str(endBIndex) + "\n")
        print("Max Num Pairs: " + str(max_NumPairs) + "\n")

        # We might not have a max_NumPairs greater than the K wanted
        while max_NumPairs > K:

            startBIndex -= 1
            numA -= 1
            # Shift our B's to the left to reduce the number of pairs
            max_NumPairs = numB * (numA)

        endBIndex = startBIndex + numB

        print("B Start Index: " + str(startBIndex) + "\nB End Index: " + str(endBIndex) + "\n")

        for elem in range(0, N):
            if elem in range(startBIndex, endBIndex):
                pairList[elem] = 'B'

            else:
                pairList[elem] = 'A'

        strFound = True

        print(pairList)

ABStrGen(10,12)
print("\n")
ABStrGen(3,2)
print("\n")
ABStrGen(2,0)
print("\n")
ABStrGen(5,8)
from Bio.Seq import Seq

mySeq = Seq("AGTACACTGGT")

print("Original Sequence: " + str(mySeq))

# print(mySeq.alphabet)

print("Complement Sequence: " + str(mySeq.complement()))

print("Reverse Complement Sequence: " + str(mySeq.reverse_complement()))
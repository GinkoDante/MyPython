from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

# Define the Alphabet as having unambiguous DNA: basic letters
mySeq = Seq("AGTACACTGGT", IUPAC.unambiguous_dna)

print("My DNA Sequence: " + repr(mySeq))


# Define as an Amino Acid Sequence
myProtein = Seq("AGTACACTGGT", IUPAC.protein)

print("My Amino Acid Sequence: " + repr(myProtein))

print("\nDNA Sequence:\n")

for index, letter in enumerate(mySeq):
    print("%i %s" % (index, letter))

print("\nLength of my DNA Sequence: " + str(len(mySeq)))

print("\nCount Pairs of GT in my DNA Sequence: " + str(mySeq.count("GT")))

mySeq2 = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)

print("\nMy DNA Sequence 2 count of G: " + str(mySeq2.count("G")))

percentGCalc = 100 * float(mySeq2.count('C') + mySeq2.count('G')) / len(mySeq2)

# Easier way to calculate GC Percentage

print("Percentage of G and C in DNA Seq 2 (" + mySeq2 + "): " + str(GC(mySeq2)) )

# Get a slice of a sequence using the normal Python list conventions
print(mySeq2[4:12])

# We can also do slices with a [start:stop:stride] convention to find various codons
# Start at first nucleotide and retrieve every third nucleotide
print("First Codon: " + str(mySeq2[0::3]))
# Start at second nucleotide and retrieve every third nucleotide
print("Second Codon: " + str(mySeq2[1::3]))
# Start at third nucleotide and retrieve every third nucleotide
print("Third Codon: " + str(mySeq2[2::3]))

print("Reverse a Sequence using slicing: " + str(mySeq2[::-1]))

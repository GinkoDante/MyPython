__author__ = 'Bill Lee'
from Bio import SeqIO

count = SeqIO.convert("MyDBRecords.faa", "fasta", "MyDBRecords_GB.gbk", "genbank")

print("Converted %i records"%count)
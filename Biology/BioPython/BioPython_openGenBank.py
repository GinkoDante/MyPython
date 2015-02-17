from Bio import SeqIO

for seqRecord in SeqIO.parse("ls_orchid.gbk", "genbank"):
    print(seqRecord.id)
    print(repr(seqRecord.seq))
    print(len(seqRecord))
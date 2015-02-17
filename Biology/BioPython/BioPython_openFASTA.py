from Bio import SeqIO

for seqRecord in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seqRecord.id)
    print(repr(seqRecord.seq))
    print(len(seqRecord))
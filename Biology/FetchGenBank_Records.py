from Bio import Entrez
from Bio import SeqIO

Entrez.email = "ginkodante@gmail.com"

# Get a single record
handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="6273291")

# Read(): handles one record
seq_record = SeqIO.read(handle, "fasta")

handle.close()
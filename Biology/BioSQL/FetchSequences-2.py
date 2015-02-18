from Bio import Entrez
from Bio import SeqIO
# Fetch the following records
handle = Entrez.efetch(db="nuccore", id="6273291,6273290,6273289", rettype="gb", retmode="text")

# Parse each genbank Sequence Record
for seq_record in SeqIO.parse(handle, "gb"):

    print seq_record.id, seq_record.description[:50] + "..."
    print "Sequence Length: %i," % len(seq_record),
    print "%i features," % len(seq_record.features),
    print "from: %s" % seq_record.annotations['source']

handle.close()
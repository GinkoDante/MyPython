from BioSQL import BioSeqDatabase
from Bio import SeqIO

# Connect to "server" and open db
server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2",
                                      host="127.0.0.1", db="bioseqdb")
# select sub database
db = server["orchids"]

print("This database contains %i records" % len(db))

myRecords = []

# find records for each identifier
for identifier in ['6273291', '6273290', '6273289']:
    # Retrieve the sequence record by lookuping the Id
    seq_record = db.lookup(gi=identifier)
    print(seq_record.id, seq_record.description[:50] + "...")
    print("Sequence Length: %i\n" % len(seq_record.seq))

    myRecords.append(seq_record)

# Write list of records to a file
SeqIO.write(myRecords, "MyDBRecords.faa", "fasta")

'''
# We can also retrive records from a db by having it act as a dict with keys being the primary key
# and values being the identifier
for key, record in db.iteritems():
    print("Key %r maps to a sequence record with the id %s" % (key, record.id))
'''
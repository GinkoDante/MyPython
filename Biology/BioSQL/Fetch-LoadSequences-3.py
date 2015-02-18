from Bio import Entrez
from Bio import SeqIO
from BioSQL import BioSeqDatabase

# Connect to Database
server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2", host="127.0.0.1", db="bioseqdb")

db = server["orchids"]

# Fetch the following records from the Web
handle = Entrez.efetch(db="nuccore", id="6273291,6273290,6273289", rettype="gb", retmode="text")

# Load returns number of records handled into db
count = db.load(SeqIO.parse(handle, "genbank"))

print "Loaded %i records" % count

handle.close()

# Commit records to db to ensure they are entered
server.adaptor.commit()

# Check the affected Tables in orchids sub database:
# mysql --user=root bioseqdb -e "select * from bioentry;"
# mysql --user=root bioseqdb -e "select * from biosequence;"
# mysql --user=root bioseqdb -e "select * from seqfeature;"
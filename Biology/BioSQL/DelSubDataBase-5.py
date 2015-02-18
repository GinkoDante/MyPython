# We defined the sub database (namespace) called orchids within our main database of bioseqdb
# Here we will delete the subdatabase and all its records while keeping the main db

from BioSQL import BioSeqDatabase

server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2",
                                      host="127.0.0.1", db="bioseqdb")

db = server['orchids']

print("The sub database %s contains %i records" % (db.name, len(db)))

server.remove_database('orchids')

server.adaptor.commit()

# Check with the following command that the sib bd is removed:
# mysql --user=root -p bioseqdb -e "select * from biodatabase;"
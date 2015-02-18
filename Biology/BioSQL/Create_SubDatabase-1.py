from BioSQL import BioSeqDatabase

server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2", host="127.0.0.1", db="bioseqdb")

db = server.new_database("orchids", description="Just to Test")
server.adaptor.commit()

# Check that the subdatabse has been created:
# mysql --user=root bioseqdb -e "select * from biodatabase;"
# psql -c "SELECT * FROM biodatabase;" bioseqdb
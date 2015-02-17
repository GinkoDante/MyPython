from BioSQL import BioSeqDatabase

server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="", host="localhost", db="bioseqdb")

db = server.new_database("orchids", description="Just to Test")
server.commit()
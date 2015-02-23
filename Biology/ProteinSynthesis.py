import random
import socket
import sys
from Bio import Entrez
from Bio import SeqIO
from BioSQL import BioSeqDatabase


class BioServer:

    def __init__(self):
        # server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2", host="127.0.0.1", db="bioseqdb")
        serverName = ""
        driver = "MySQLdb"
        user = ""
        passwd = ""
        host = "127.0.0.1"
        db = "bioseqdb"
        connected = True

    def get_Connected(self):
        return self.connected

    def set_Connnected(self, connectAction):
        self.connected = connectAction

    def Disconnect(self):
        self.connected = False

#Structure of each cells functions, time and quantity
class Cell:

    def __init__(self, id, dnaSeq, maxPSNum):
        self.id = id
        self.startDNASeq = dnaSeq
        self.currDNASeq = list(dnaSeq)
        self.rnaSeq = []
        # self.ribosome = Ribosome()
        # self.mRNA = mRNA()
        # self.tRNA = tRNA()
        self.atpAmount = 0
        self.proteins = []
        self.origReps = []
        self.errorRate = 0
        self.timeToLive = 110
        self.DNAState = 0
        self.timeToRep = 150
        self.replicate = False
        self.dnaDiff = 0
        self.ps_amtTime = 45
        self.ps_srtNum = random.randrange(1, maxPSNum+1)
        self.numPS = 0

    def Respiration(self):
        None

    def Glycolysis(self):
        None

    def DNATranscription(self):
        None

    def Translation(self):
        None
        #For translation, RNA sequence is needed and a library of the (2) amino acids (3 lett. abbrev)

    def ProteinSynthesis(self):

        self.rnaSeq = []
        self.numPS += 1

        # Replication of dna strand into sense (coding) strand and anti-sense strand (template)

        # Transcribe dna strand and find complement rna sequence via RNA polymerase

    def Apoptosis(self):
        None

    def DNA_Damage(self):
        None

    def DNA_Repair(self):
        None

    def __iter__(self):
        return self.__iter__()

def ProteinSynthesis_Sim(numSeconds, dnaSeq, maxPSNum, numCells):

    ps_cellLists = []

    for i in range(maxPSNum):

        ps_cellLists.insert(i, [])

    for i in range(numCells):

        aCell = Cell(i, dnaSeq, maxPSNum)
        '''
        if ps_cellLists[aCell.ps_srtNum] == None:

            ps_cellLists[aCell.ps_srtNum] = []
            ps_cellLists[aCell.ps_srtNum].append(aCell)

        else:
        '''
        ps_cellLists[aCell.ps_srtNum].append(aCell)

    ''' Create a balance tree of cells organized by process_StartNum
    rootNum = maxPSNum / 2
    rootNode = Tree(rootNum)

    psTree = BinarySearchTree()
    psTree.root = rootNode
    '''

    for currentSecond in range(numSeconds):

        #  Check if a cell is ready to perform protein synthesis
        genTime = GenPSTime(maxPSNum)

        # Run all cells whose startTime is less than the time Number generated
        for i in range(genTime):
            for cell in ps_cellLists[i]:
                cell.ProteinSynthesis()
                # print("Cell " + str(cell.id) + ": " + str(cell.rnaSeq))

    for i in range(maxPSNum):
        for cell in ps_cellLists[i]:
            print("Cell " + str(cell.id) + "(" + str(cell.numPS) + "): " + str(cell.rnaSeq))

def GenPSTime(maxPSNum):

    return random.randrange(1, maxPSNum+1)


def Create_SubDB():
    # 1. Create a sub database for sequences to be added to
    server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2", host="127.0.0.1", db="bioseqdb")

    db = server.new_database("orchids", description="Just to Test")

def Connect_Server():

    server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2", host="127.0.0.1", db="bioseqdb")


def Connect_DB(server):

    # Fetch the wanted sequences and load into the created sub database
    db = server["orchids"]

def Connect_SvrDB():
        server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2", host="127.0.0.1", db="bioseqdb")

        # Fetch the wanted sequences and load into the created sub database
        db = server["orchids"]

def FetchSeq(connectedToServer):

    if connectedToServer:
        # Get server Already connected to
    else:
        Connect_Server()

    # Fetch the following records from the Web
    handle = Entrez.efetch(db="nuccore", id="6273291,6273290,6273289", rettype="gb", retmode="text")

    # Load returns number of records handled into db
    count = db.load(SeqIO.parse(handle, "genbank"))

    print "Loaded %i records" % count

    handle.close()

    # Commit records to db to ensure they are entered
    server.adaptor.commit()

def FetchSeq():
    # Extract sequences from sub database for use
    # Connect to "server" and open db
    server = BioSeqDatabase.open_database(driver="MySQLdb", user="root", passwd="gtrhalo2", host="127.0.0.1", db="bioseqdb")

    # select sub database
    db = server["orchids"]

    print("This database contains %i records" % len(db))

    # find records for each identifier
    for identifier in ['6273290']:
        # Retrieve the sequence record by lookuping the Id
        seq_record = db.lookup(gi=identifier)

        print(seq_record.id, seq_record.description[:50] + "...")

        print("Sequence Length: %i\n" % len(seq_record.seq))

# Create A Menu to display
showMenu = True
menuSelection = 0

connectedToServer = False

while showMenu:
    print("Welcome to Protein Synthesis Simulation!\n")
    print("Please select an option below.\n\n")
    print("1. Create a Sub Database\n")
    print("2. Connect to a Sub Database\n")
    print("3. Fetch and Load a Sequence\n")
    print("4. Run Protein Synthesis\n")

    raw_input(menuSelection)

    if menuSelection == 1:
        connectedToServer = Connect_Server()
        Create_SubDB()

    elif menuSelection == 2:
        Connect_Server()
        Connect_DB()

    elif menuSelection == 3:
        Connect_Server()
        Connect_DB()
        FetchSeq()

    elif menuSelection == 4:
        ProteinSynthesis_Sim(100, str(seq_record.seq), 200, 15)

    else:
        print("Error")


# Create cells and run program to simulate
# program has pieces which move in various ways through the knights tour problem
# but are dictated by AI logic as to which path to take

import random
import socket
import sys
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        print(str(self.get_starttag_text()))
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)

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

        #Replication of dna strand into sense (coding) strand and anti-sense strand (template)



        # Transcribe dna strand and find complement rna sequence via RNA polymerase
        for nucleo in self.currDNASeq:
            if nucleo == 'A':
                self.rnaSeq.append('U')
            elif nucleo == 'G':
                self.rnaSeq.append('C')
            elif nucleo == 'C':
                self.rnaSeq.append('G')
            else:
                self.rnaSeq.append('A')

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


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to web server at port 80
mysock.connect(('www.ncbi.nlm.nih.gov', 80))

# Send command to get text file
request = 'GET http://www.ncbi.nlm.nih.gov/nuccore/?term=earthworm HTTP/1.0\n\n'
mysock.send(request.encode())

while True:
    data = mysock.recv(512).decode()
    if ( len(data) < 1 ) :
        break
    print(data)

mysock.close()

# Block for Links
'''

</div>
    <div>
        <div class="rprt">
            <div class="rprtnum nohighlight">
                <label for="UidCheckBox25989914" class="ui-helper-hidden-accessible">Select item 25989914</label>
                    <input name="EntrezSystem2.PEntrez.Nuccore.Sequence_ResultsPanel.Sequence_RVDocSum.uid" sid="1" type="checkbox" id="UidCheckBox25989914" value="25989914" accn="AY154648.1" /><span>1.</span>
                        </div>
                            <div class="rslt"><p class="title"><a href="/nuccore/AY154648.1" ref="ordinalpos=1">Uncultured <b>earthworm</b> intestine bacterium clone wi128 16S ribosomal RNA gene, partial sequence</a></p><div class="supp"><p class="desc">1,292 bp linear DNA </p>
                        </div>
                            <div class="aux">
                                <div class="resc">
                                    <class="rprtid"><dt>Accession:</dt> <dd>AY154648.1</dd> <dt>GI:</dt> <dd>25989914</dd> </dl></div>
                                    <p class="links">
                                        <a ref="ordinalpos=1" href="/nuccore/25989914?report=genbank">GenBank</a>
                                        <a ref="ordinalpos=1" href="/nuccore/25989914?report=fasta">FASTA</a>
                                        <a ref="ordinalpos=1" href="/nuccore/25989914?report=graph">Graphics</a>
                                        <a ref="ordinalpos=1" href="/popset?DbFrom=nuccore&amp;Cmd=Link&amp;LinkName=nuccore_popset&amp;IdsFromResult=25989914">PopSet</a>
                                    </p>
                                </div>
                            </div>
'''
# Look for FATSA Links
# <a ref="ordinalpos=1" href="/nuccore/25989914?report=fasta">FASTA</a>

parser = MyHTMLParser()

# File containing html to parse
# htmlFileName = sys.argv[1]

htmlFileName = 'NCBI_Connect.txt'

# Try to open the file
try:
    htmlFile = open(htmlFileName)

    outLinkLines = []

    htmlLineList = htmlFile.readlines()

    for line in htmlLineList:
        if parser.handle_starttag()

except IOError:
    print("Unable to open file.")





'''
# Open and read in a dna sequence in FASTA format coding strand
seqFileName = open("/Users/aliseramirez/Desktop/dna.txt")
seqFile = seqFileName.read()
#CodednaSeq = file_contents.rstrip("\n")
print(seqFile)
seqFileName.close()

#Calculate the length of the DNA Sequence
dna_length = len(seqFile)
print("Number of nucleotides in sequence is " + str(dna_length))

#Calculate the frequency of 'A,T,G,C' against background


#Calculate the number of genes

#Create an output file that will be the complement of the input file DNA sequence, the template the strand for RNA
output_file = open("tempdnaSeq", "w")
output_file.write(seqFile.replace('A', 'T'))
output_file.write(seqFile.replace('G','C'))
print(output_file)
output_file.close()
'''
''' ProteinSynthesis_Sim(100, 'AGCT', 200, 15) '''
import socket

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
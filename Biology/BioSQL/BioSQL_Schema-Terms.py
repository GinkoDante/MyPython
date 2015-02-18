

''' BioEntry:
This is the core entity of the BioSQL schema;
a bioentry is any single entry or record in a biological database.
The bioentry contains information about the record's:
    public name, public accession and version, its description and an identifier field.
'''

''' Example BioEntry:
    name:		S63169S6
    accession:	S63178
    identifier:     386456
    division:       PRI
    description:	NDP=Norrie disease {first three exons, microdeletion regions}
    version:	1
'''

''' BioDatabase
A biodatabase is simply a collection of bioentries;

SQL Example 1 - fetch the accessions of all sequences from SwissProt:

 SELECT DISTINCT bioentry.accession
 FROM   bioentry JOIN biodatabase USING (biodatabase_id)
 WHERE  biodatabase.name = 'swiss'  -- or 'Swiss-Prot'

SQL Example 2 - how many unique entries are there in GenBank:
 SELECT COUNT(DISTINCT bioentry.accession)
 FROM   bioentry JOIN biodatabase USING (biodatabase_id)
 WHERE  biodatabase.name = 'genbank'

SQL Example 3 - fetch the locus names for the latest versions of all entries where the biodatabase name is 'swiss' (Mysql syntax):
 SELECT MID(MAX(CONCAT(RPAD(LPAD(bioentry.version,5,'?'),10,'?'),
        bioentry.name)),11)
        FROM bioentry JOIN biodatabase USING (biodatabase_id)
 WHERE  biodatabase.name = 'swiss'
 GROUP BY bioentry.name
'''
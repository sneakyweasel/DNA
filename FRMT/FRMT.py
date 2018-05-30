import os
import sys
from Bio import Entrez
from Bio import SeqIO
Entrez.email = "sneaky_weasel@hotmail.fr"

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_frmt.txt'))
vars = file.read()
ids = vars.rstrip('\n').split(" ")
print(ids)

handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))

min = 100000
min_id = -1
for id, record in enumerate(records):
    print(len(record.seq))
    if len(record.seq) < min:
        min = len(record.seq)
        min_id = id

print("-----")
print(min_id)
print(len(records[min_id].seq))
print("-----")
print(">" + records[min_id].description)
print(records[min_id].seq)

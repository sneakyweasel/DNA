import os
import sys
from Bio import Entrez

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_gbk.txt'))
lines = [line.rstrip('\n') for line in file]
name = lines[0]
date1 = lines[1]
date2 = lines[2]

print(name)
print(date1)
print(date2)

Entrez.email = "sneaky_weasel@hotmail.fr"
handle = Entrez.esearch(
    db="nucleotide",
    term=f"{name}[Organism]",
    mindate={date1},
    maxdate={date2},
    datetype="pdat"
    )
record = Entrez.read(handle)
record["Count"]
print(record)

import os
import sys
from Bio.Seq import translate

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ptra.txt'))
lines = [line.rstrip('\n') for line in file]

dna = lines[0]
prot_str = lines[1]

for x in range(1, 15):
    if x != 7 and x != 8:
        prot_test = translate(dna, table=x, to_stop=True)
        if prot_test == prot_str:
            print(x)

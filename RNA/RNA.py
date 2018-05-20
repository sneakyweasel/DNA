import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_rna.txt'))
dna = [line.rstrip('\n') for line in file][0]
# dna = "GATGGAACTTGACTACGTAAATT"

rna = dna.replace("T", "U")
print rna

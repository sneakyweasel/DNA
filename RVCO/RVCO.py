import os
import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Read input file to fatsas
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_rvco.txt'))
lines = [line.rstrip('\n') for line in file]
blob = ''.join(lines)
raw = blob.split('>')
raw.pop(0)
fatsas = []
for x in range(0, len(raw), 1):
    id     = raw[x][0:13]
    strand = raw[x][13:]
    fatsas.append([id, strand])
print(f"Strands: {fatsas}")

# Check if string match their reverse complement
counter = 0
for fatsa in fatsas:
    my_seq = Seq(fatsa[1], IUPAC.unambiguous_dna)
    if fatsa[1] == my_seq.reverse_complement():
        counter += 1
        print(fatsa)

print(counter)

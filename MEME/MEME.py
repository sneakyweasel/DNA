import os
import sys
from Bio.Seq import Seq
from Bio import motifs

# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_meme.txt'))
# lines = [line.rstrip('\n') for line in file]
# name = lines[0]
# date1 = lines[1]
# date2 = lines[2]

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_meme.txt'))

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

# Used MEME finding tool

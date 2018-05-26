import os
import sys
import string
import itertools
import re
from graphviz import Digraph

# Read input file to fatsas
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_sseq.txt'))
lines = [line.rstrip('\n') for line in file]
blob = ''.join(lines)
raw = blob.split('>')
raw.pop(0)
fatsas = []
for x in range(0, len(raw), 1):
    strand = raw[x][11:]
    fatsas.append(strand)
print(f"Strands: {fatsas}")

# Generate custom REGEX from second strand
def subsequence(dna, strand):
    regex = "*.".join(strand)
    regex = '(?=' + regex + ')'
    print(regex)
    matches = re.finditer(regex, dna)
    indexes = []
    for match in matches:
        indexes.append(match.start() + 1)
    return indexes

for 
subs = subsequence(fatsas[0], fatsas[1])
print(subs)

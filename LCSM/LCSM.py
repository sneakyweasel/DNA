import os
import sys
import string
from itertools import zip_longest

# Read input file to fatsas
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lcsm.txt'))
# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lcsm_test.txt'))
lines = [line.rstrip('\n') for line in file]
blob = ''.join(lines)
raw = blob.split('>')
print(raw)
raw.pop(0)
fatsas = []
for x in range(0, len(raw), 1):
    strand = raw[x][13:]
    fatsas.append(strand)
print(f"Strands: {fatsas}")

# Find common longest substring
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr

solution = long_substr(fatsas)
print(solution)

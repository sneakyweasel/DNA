import os
import sys
import string
from itertools import zip_longest

# Read input file
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_prot.txt'))
lines = [line.rstrip('\n') for line in file]
dna = ''.join(lines)

# Dna to process
# dna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

# Convert codon file to array
codons = []
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'codon.txt'))
for line in file.read().splitlines():
    triplet = line.split(" ")[0]
    letter  = line.split(" ")[1]
    codons.append([triplet, letter])

# Group into triplets
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
chunks = chunker(dna, 3)
triplets = []
for chunk in chunks:
    triplets.append(''.join(chunk))

# Iterate and translate
solution = ""
for triplet in triplets:
    for codon in codons:
        if triplet == codon[0]:
            if codon[1] == "Stop":
                break
            else:
                solution += codon[1]

# Print solution
print(solution)

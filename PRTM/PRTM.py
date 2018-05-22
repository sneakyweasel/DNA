import os
import sys
import string
from itertools import zip_longest

# Read input file
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_prtm.txt'))
dna = [line.rstrip('\n') for line in file][0]

# Dna to process
# dna = "SKADYEK"

# Convert codon file to array
letters = []
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'mass.txt'))
for line in file.read().splitlines():
    letter = line.split(" ")[0]
    mass   = float(line.split(" ")[1])
    letters.append([letter, mass])

# Iterate and translate
solution = 0
for c in dna:
    for letter in letters:
        if c == letter[0]:
            solution += letter[1]

# Round solution to 3 decimals
solution = round(solution, 3)

# Print solution
print(solution)

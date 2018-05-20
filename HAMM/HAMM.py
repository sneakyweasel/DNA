import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_hamm.txt'))
dna = [line.rstrip('\n') for line in file]
# dna = ["GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"]

counter = 0
for index in range(0, len(dna[0])):
    if dna[0][index] != dna[1][index]:
        counter += 1

print counter

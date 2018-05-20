import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_dna.txt'))
dna = file.read()
# dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

counterA = 0
counterC = 0
counterG = 0
counterT = 0

for c in dna:
    if c == "A":
        counterA += 1
    elif c == "C":
        counterC += 1
    elif c == "G":
        counterG += 1
    else:
        counterT += 1

print str(counterA) + " " + str(counterC) + " " + str(counterG) + " " + str(counterT)

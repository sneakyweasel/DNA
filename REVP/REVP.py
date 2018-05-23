# Locating Restriction Sites

import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_revp.txt'))
lines = [line.rstrip('\n') for line in file]
lines.pop(0)
dna = ''.join(lines)
# dna = "TCAATGCATGCGGGTCTATATGCAT"

# Create reverse complement of a DNA string
def reverse_complement(dna):
    reverse = dna[::-1]
    complement = ""
    for c in reverse:
        if c == "A":
            complement += "T"
        elif c == "T":
            complement += "A"
        elif c == "C":
            complement += "G"
        else:
            complement += "C"
    return complement

# Palindrome
def palindrome_tester(dna):
    positions = []
    for i in range(0, len(dna)):
        # Range 4..12
        for x in range(12, 2, -2):
            strand = dna[i:i + x]
            length = len(strand)
            if length >= 4 and length % 2 == 0:
                prev = strand[0:int(length/2)]
                next = strand[int(length/2):]
                # print(prev + " " + next + " " + reverse_complement(next) + " i:" + str(i) + " x:" + str(x))
                if prev == reverse_complement(next):
                    # print(prev + " " + reverse_complement(next) + " i:" + str(i + 1) + " x:" + str(x))
                    positions.append([i + 1, length])
                    break
    return positions

# Find pos, length of reverse
palindromes = palindrome_tester(dna)
for palindrome in palindromes:
    print(str(palindrome[0]) + " " + str(palindrome[1]))

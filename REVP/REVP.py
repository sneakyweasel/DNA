# Locating Restriction Sites

import os
import sys

# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_revp.txt'))
# lines = [line.rstrip('\n') for line in file]
# blob = ''.join(lines)
dna = "TCAATGCATGCGGGTCTATATGCAT"

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
    position = []
    for index in range(2, len(dna) - 2):
        # Range 4..12
        for x in range(2, 6):
            prev_strand = dna[index:(index-x)]
            next_strand = dna[index:(index+x)]
            # print(prev_strand + " " + next_strand + " i:" + str(index) + " x:" + str(index))

            if prev_strand == reverse_complement(next_strand):
                position.append([index, x])
                print(prev_strand + " " + next_strand + " i:" + str(index) + " x:" + str(index))
                break


# Dedupe solution

# Find pos, length of reverse
solution = palindrome_tester(dna)
print(solution)

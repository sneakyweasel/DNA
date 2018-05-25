import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_mrna.txt'))
proteins = file.read()
# proteins = "MA"

# Convert codon file to array
codons = []
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'codon.txt'))
for line in file.read().splitlines():
    triplet = line.split(" ")[0]
    letter  = line.split(" ")[1]
    codons.append([triplet, letter])

# Unique proteins
letters = []
for codon in codons:
    letters.append(codon[1])
uniq_prot = list(sorted(set(letters)))

# Recreate list with possible combination
inv_codons = []
for prot in uniq_prot:
    count = 0
    for codon in codons:
        if prot == codon[1]:
            count += 1
    inv_codons.append([prot, count])

# Translate protein to RNA values
counter = 1
for protein in proteins:
    for codon in inv_codons:
        if protein == codon[0]:
            counter *= codon[1]
counter *= 3
solution = counter % 1000000

print(uniq_prot)
print(inv_codons)
print(counter)
print(solution)

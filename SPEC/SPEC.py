import os
import sys
from decimal import *
from Bio.Seq import Seq
from operator import itemgetter, attrgetter, methodcaller

# Import proteins
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'proteins.txt'))
lines = [line.rstrip('\n') for line in file]
proteins = []
for line in lines:
    protein = line.split(' ')[0]
    mass = Decimal(line.split(' ')[1]).quantize(Decimal('.001'), rounding=ROUND_DOWN)
    proteins.append([protein, mass])

for mass in (sorted(proteins, key=itemgetter(1))):
    print(mass)

# Import masses
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_spec.txt'))
masses = [Decimal(line.rstrip('\n')) for line in file][::-1]
print(masses)

# Loop
strand = ""
for x in range(0, len(masses) - 1):
    diff = masses[x] - masses[x+1]
    diff = diff.quantize(Decimal('.001'), rounding=ROUND_DOWN)
    for protein in proteins:
        if diff == protein[1]:
            strand += protein[0]
            break
    print(f"Diff: {diff} - {masses[x]} {masses[x+1]}")

print(strand[::-1])

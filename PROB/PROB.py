import os
import sys
import itertools
import math
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqUtils import GC

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_prob.txt'))
lines = [line.rstrip('\n') for line in file]
dna = Seq(lines[0], generic_dna)
arrA = [float(x) for x in lines[1].split(' ')]

results = []
for k in arrA:
    totalLog = 0
    gc = k / 2
    at = (1 - k) / 2

    for x in dna:
        if x == "G" or x == "C":
            totalLog += math.log10(gc)
        else:
            totalLog += math.log10(at)
    results.append(str(round(totalLog, 3)))

print(" ".join(results))

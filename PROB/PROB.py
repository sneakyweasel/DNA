import os
import sys
import itertools
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqUtils import GC

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_prob.txt'))
lines = [line.rstrip('\n') for line in file]
dna = Seq(lines[0], generic_dna)
probs = [float(x) for x in lines[1].split(' ')]

print(dna)
print(probs)

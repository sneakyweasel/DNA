import os
import sys
import Bio
import string
import itertools
import re
from Bio import SeqIO
from Bio.Alphabet import IUPAC

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_kmp.txt'))
record = list(SeqIO.parse(file, "fasta"))
dna = record[0].seq
print(f"SEQ1: {(dna)}")

# http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/kmpen.htm
# Knuth-Morris-Pratt algorithm
def compute_prefix_function(p):
    m  = len(p)
    b  = list(range(m+1))
    i  = 0
    j  = -1
    b[i] = j
    while i < m:
        while j >= 0 and p[i] != p[j]:
            j = b[j]
        i += 1
        j += 1
        b[i] = j
    b.pop(0)
    return b

failures = compute_prefix_function(dna)
print(" ".join(map(str, failures)))

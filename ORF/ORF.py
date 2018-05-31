import os
import sys
import Bio
import string
import itertools
import re
from Bio import SeqIO
from Bio.Alphabet import IUPAC

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_orf.txt'))
record = list(SeqIO.parse(file, "fasta"))
seq1 = record[0].seq
print(f"SEQ1: {str(seq1)}")

# ORFs
arr = []
for frame_num in range(3):
    rev = seq1.reverse_complement()
    frame = rev[frame_num:].translate()
    for spl in frame.split('*'):
        arr.append(spl)
    frame = rev[frame_num:].translate()
    for spl in frame.split('*'):
        arr.append(spl)

for prot in arr:
    print(prot)

import os
import sys
import Bio
import string
import itertools
import re
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio import pairwise2
from operator import itemgetter, attrgetter, methodcaller


# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_edta.txt'))
record = list(SeqIO.parse(file, "fasta"))
seq1 = record[0].seq
seq2 = record[1].seq
# print(f"SEQ1: {str(seq1)}")
# print(f"SEQ2: {str(seq2)}")
# print("------")

alignments = pairwise2.align.globalxx(seq1, seq2)

# for alignment in alignments:
#     print(f"{alignment[2]} {alignment[3]} {alignment[4]}")

alignment = sorted(alignments, key=itemgetter(4))[0]
# print(f"{alignment[2]} {alignment[3]} {alignment[4]}")
print(int(alignment[2]))
print(alignment[0])
print(alignment[1])

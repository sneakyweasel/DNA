import os
import sys
import Bio
import string
import itertools
import re
from Bio import SeqIO
from Bio.Alphabet import IUPAC

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lcsq.txt'))
record = list(SeqIO.parse(file, "fasta"))
seq1 = record[0].seq
seq2 = record[1].seq
print(f"SEQ1: {str(seq1)}")
print(f"SEQ2: {str(seq2)}")
print("------")

# LCS (https://rosettacode.org/wiki/Longest_common_subsequence#Python)
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

strand = lcs(str(seq1), str(seq2))
print(strand)

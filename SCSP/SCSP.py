import os
import sys
import Bio
import string
import itertools
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_scsp.txt'))
seqs = file.readlines()
seq1 = Seq(seqs[0])
seq2 = Seq(seqs[1])
print(f"Seq1: {str(seq1)}")
print(f"Seq2: {str(seq2)}")
print("------")

# Longest common subsequence
def longest_common_subsequence(a, b):
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

# Shortest Common Supersequence
def shortest_common_supersequence(a, b):
    lcs = longest_common_subsequence(a, b)
    scs = ""
    # Consume lcs
    while len(lcs) > 0:
        if a[0]==lcs[0] and b[0]==lcs[0]:
        # Part of the LCS, so consume from all strings
            scs += lcs[0]
            lcs = lcs[1:]
            a = a[1:]
            b = b[1:]
        elif a[0]==lcs[0]:
            scs += b[0]
            b = b[1:]
        else:
            scs += a[0]
            a = a[1:]
    # append remaining characters
    return scs + a + b

# scs = shortest_common_supersequence(str(seq1), str(seq2))
scs = shortest_common_supersequence("WEASELS", "WARDANCE")
print(scs)

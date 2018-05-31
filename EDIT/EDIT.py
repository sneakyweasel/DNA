import os
import sys
import Bio
import string
import itertools
import re
from Bio import SeqIO
from Bio.Alphabet import IUPAC

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_edit.txt'))
record = list(SeqIO.parse(file, "fasta"))
seq1 = record[0].seq
seq2 = record[1].seq
print(f"SEQ1: {str(seq1)}")
print(f"SEQ2: {str(seq2)}")
print("------")

# Edit distance
def edit_distance(seq1, seq2):

    return score

def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]


print(minimumEditDistance(str(seq1) ,str(seq2)))

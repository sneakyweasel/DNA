import os
import sys
import Bio
import string
import itertools
import re
from graphviz import Digraph
from Bio import SeqIO
from Bio.Alphabet import IUPAC

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_sseq.txt'))
records = list(SeqIO.parse(file, "fasta"))
seq1 = str(records[0].seq)
seq2 = str(records[1].seq)
print(f"SEQ1: {seq1}")
print(f"SEQ2: {seq2}")

# Generate custom REGEX from second strand
def subsequence(dna, strand):
    pos = []
    offset = 0
    for i, c in enumerate(strand):
        for x in range(offset, len(dna)):
            if c == dna[x]:
                print(f"Char {c} at {i}")
                offset = x + 1
                pos.append(str(x + 1))
                break
    return pos


subs = subsequence(seq1, seq2)
print(" ".join(subs))

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
print("-----")
# print(f"SEQ1: {str(seq1)}")

# ORFs
strands = []
for frame in range(0, 3):
    rev = seq1.reverse_complement()
    trips = (len(seq1) - frame) // 3
    total = trips * 3
    end   = total - frame
    strand = str(seq1)[frame:end]
    print(f"Frame {frame}: [{frame}:{end}] len:{len(strand)} - {trips} - {total}")
    strands.append(seq1[frame:end].translate(table=1))
    strands.append(rev[frame:end].translate(table=1))

def isolate_prot(a):
    start = []
    end = []
    results = []
    for i, c in enumerate(a):
        if c == "M":
            start.append(i)
        if c == "*":
            end.append(i)
    for element in itertools.product(start, end):
        if element[0] < element[1]:
            prot = a[element[0]:element[1]]
            if "*" not in prot:
                results.append(prot)
                # print(f"{element} - {prot}")
    return(results)

results = []
for strand in strands:
    results += isolate_prot(strand)
uniq = list(set(results))

for prot in uniq:
    print(prot)

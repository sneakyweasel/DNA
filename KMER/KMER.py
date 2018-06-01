import os
import sys
import Bio
import itertools
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio import pairwise2
from operator import itemgetter, attrgetter, methodcaller

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_kmer.txt'))
record = list(SeqIO.parse(file, "fasta"))
seq = record[0].seq
print(f"SEQ1: {str(seq)}")
print("------")

def prod(n):
    lex = ["A", "C", "G", "T"]
    perms = list(itertools.product(lex, repeat=n))
    arr = []
    for perm in perms:
        arr.append(["".join(perm), 0])
    return arr

def kmer(dna, n):
    tuples = prod(n)
    for x in range(0, len(dna)):
        for i in range(0, len(tuples)):
            if dna[x:x+n] == tuples[i][0]:
                tuples[i][1] += 1
    return tuples

results = kmer(seq, 4)
arr = []
for tup in results:
    arr.append(str(tup[1]))
print(" ".join(arr))

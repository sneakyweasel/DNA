import os
import sys
from Bio import ExPASy
from Bio import SeqIO
from Bio import SwissProt
from Bio import pairwise2

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_need.txt'))
vars = file.read()
id1 = vars.split(' ')[0]
id2 = vars.split(' ')[1]
print(id1)
print(id2)

handle = ExPASy.get_sprot_raw(id1)
record = SwissProt.read(handle)
seq1 = record.seq
print(seq1)



# seq1 = SeqIO.read("alpha.faa", "fasta")
# seq2 = SeqIO.read("beta.faa", "fasta")
# alignments = pairwise2.align.globalxx(seq1.seq, seq2.seq)

import os
import sys
from Bio import ExPASy
from Bio import SeqIO
from Bio import SwissProt
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import Entrez

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_subo.txt'))
vars = file.read()
id1 = vars.split(' ')[0]
id2 = vars.split(' ')[1]
print(id1)
print(id2)

Entrez.email = "sneaky_weasel@hotmail.fr"
handle = Entrez.efetch(db="nucleotide", id=id1, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()
seq1 = record.seq

handle = Entrez.efetch(db="nucleotide", id=id2, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()
seq2 = record.seq

print(seq1)
print("-----")
print(seq2)

# alns = pairwise2.align.localxs(seq1, seq2, -10, -1)
# print(pairwise2.format_alignment(*alns[0]))
# https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=emboss_needle-I20180530-222527-0494-89071188-p1m

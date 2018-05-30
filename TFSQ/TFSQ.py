import os
import sys
from Bio import ExPASy
from Bio import Entrez
from Bio import SeqIO

# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_tfsq.txt'))
# vars = file.read()

with open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_tfsq.txt')) as input_handle, open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_tfsq_fastq.txt'), "w") as output_handle:
    sequences = SeqIO.parse(input_handle, "fastq")
    count = SeqIO.write(sequences, output_handle, "fasta")

print("Converted %i records" % count)

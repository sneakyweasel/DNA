import os
import sys
from Bio.Seq import Seq

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ini.txt'))
dna = file.read()

# my_seq = Seq("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
my_seq = Seq(dna)

counts = [str(my_seq.count("A")), str(my_seq.count("C")), str(my_seq.count("G")), str(my_seq.count("T"))]
solution = " ".join(counts)
print(solution)

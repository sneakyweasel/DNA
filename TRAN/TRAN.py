import os
import sys
import Bio
from Bio import SeqIO
from Bio.Alphabet import IUPAC

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_tran.txt'))
records = list(SeqIO.parse(file, "fasta"))
seq1 = records[0].seq
seq2 = records[1].seq

def trans_ratio(seq1, seq2):
    purines = ["A", "G"]
    pyrimidines = ["C", "T"]
    counter_transition = 0
    counter_transversion = 0
    for i, c in enumerate(seq1):
        if seq1[i] != seq2[i]:
            # Transition A <-> G | C <-> T
            if seq1[i] in purines and seq2[i] in purines or seq1[i] in pyrimidines and seq2[i] in pyrimidines:
                counter_transition += 1
            # Transversion A <-> C | G <-> T
            if seq1[i] in purines and seq2[i] in pyrimidines or seq1[i] in pyrimidines and seq2[i] in purines:
                counter_transversion += 1
    return counter_transition / counter_transversion

result = trans_ratio(seq1, seq2)
print(result)

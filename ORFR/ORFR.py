import os
import sys
from Bio.Seq import Seq
from Bio.Seq import translate
from Bio.Alphabet import IUPAC

# Read input file to fatsa
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_orfr.txt'))
lines = [line.rstrip('\n') for line in file]
fatsa = ''.join(lines)

for x in range(0, 3):
    dna = fatsa[x:]
    dna += "N" * x
    seq = Seq(dna, IUPAC.unambiguous_dna)
    prot = translate(seq, to_stop=True)
    print(prot)

    seq = Seq(fatsa, IUPAC.unambiguous_dna)
    rev_seq = seq.reverse_complement()
    dna = rev_seq[x:]
    dna += "N" * x
    prot = translate(dna, to_stop=True)
    print(prot)

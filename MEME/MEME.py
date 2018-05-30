import os
import sys
from Bio import motifs

# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_meme.txt'))
# lines = [line.rstrip('\n') for line in file]
# name = lines[0]
# date1 = lines[1]
# date2 = lines[2]

with open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_meme.txt')) as handle:
    record = motifs.parse(handle, "MEME")

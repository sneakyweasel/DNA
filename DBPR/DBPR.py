import os
import sys
from Bio import ExPASy
from Bio import SeqIO
from Bio import SwissProt

# file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_dbpr.txt'))
# vars = file.read()
vars = "Q8LPK5"

handle = ExPASy.get_sprot_raw(vars)
record = SwissProt.read(handle)

solution = []
for line in record.cross_references:
    if line[0] == 'GO':
        result = line[2].split(':')
        if result[0] == 'P':
            print(result[1])

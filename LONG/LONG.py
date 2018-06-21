import os
import sys
import string
import itertools as it
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from collections import defaultdict

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_long.txt'))
records = list(SeqIO.parse(file, "fasta"))
print(len(records))

SEQUENCES = [str(x.seq) for x in records]

def dijkSuperstring(originalSeqs):
  paths = defaultdict(set)
  paths[0] =  { '' }
  while paths:
    minLength = min(paths.keys())
    while paths[minLength]:
      candidate = paths[minLength].pop()
      seqAdded = False
      for seq in originalSeqs:
        if seq in candidate:
          continue
        seqAdded = True
        for i in reversed(range(len(seq)+1)):
          if candidate.endswith(seq[:i]):
            newCandidate = candidate + seq[i:]
            paths[len(newCandidate)].add(newCandidate)
      if not seqAdded:  # nothing added, so all present?
        return candidate
    del paths[minLength]

print(dijkSuperstring(SEQUENCES))

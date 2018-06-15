import os
import sys
import string
import itertools
from graphviz import Digraph
from Bio import SeqIO
from Bio.Alphabet import IUPAC

# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_grph.txt'))
records = list(SeqIO.parse(file, "fasta"))
k = 3

print(len(records))

# Longest common subsequence
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

# Suffix and prefix lcs
def fix(a, b):
    result = []
    for x in range(0, len(a)):
        suffix = a[-x:]
        prefix = b[:x]
        if prefix == suffix:
            result.append(prefix)
            # print(f"X: {x} - PreA: {prefix} | SufB: {suffix}")
    if len(sorted(result)) > 0:
        return sorted(result)[-1]
    else:
        return ""

# Create directed graph
f = Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')
f.attr('node', shape='doublecircle')

for pair in itertools.product(records, repeat=2):
    # print(f"{pair[0].id} {pair[1].id}")
    sub = fix(pair[0].seq, pair[1].seq)
    if len(sub) == 3 and (pair[0].seq != pair[1].seq):
        f.edge(pair[0].id, pair[1].id, label=str(sub))
        print(f"{pair[0].id} {pair[1].id}")
f.view()



# AAATAAA           (0498)
#     AAATCCC       (0442)
#     AAATTTT       (2391)
#        TTTTCCC    (2323)
# GGGTGGG           (5013)

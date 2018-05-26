import os
import sys
import string
import itertools
from graphviz import Digraph

# Read input file to fatsas
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_grph.txt'))
lines = [line.rstrip('\n') for line in file]
blob = ''.join(lines)
raw = blob.split('>')
raw.pop(0)
fatsas = []
for x in range(0, len(raw), 1):
    id     = raw[x][0:13]
    strand = raw[x][13:]
    fatsas.append([id, strand])
print(f"Strands: {fatsas}")

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

#
def create_edges(fatsas):


# Create a digraph
f = Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')
f.attr('node', shape='doublecircle')
for fatsa in fatsas:
    f.node(fatsa[0])


f.edge('LR_8', 'LR_5', label='S(a)')
f.view()

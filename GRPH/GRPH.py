import os
import sys
import string
import itertools
from Bio import SeqIO
from Bio.Alphabet import IUPAC
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv


# Read input file to seqs
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_grph.txt'))
records = list(SeqIO.parse(file, "fasta"))
k = 3
print(len(records))

# Suffix and prefix lcs
def fix(a, b, k):
    result = []
    suffix_a = a[-k:]
    prefix_a = a[:k]
    suffix_b = b[-k:]
    prefix_b = b[:k]
    # if prefix_a == suffix_b:
    #     result.append(str(prefix_a))
    if prefix_b == suffix_a:
        return(str(prefix_b))
    else:
        return ""

# A length k suffix of s that matches a length k prefix of t, as long as s≠t
# suffix = s[:k]
# prefix = t[:k]

# Create directed graph
G = nx.DiGraph()

for pair in itertools.product(records, repeat=2):
    s = str(pair[0].seq)
    t = str(pair[1].seq)
    sub = fix(s, t, 3)

    if len(sub) == 3 and s != t:
        G.add_edge(pair[0].id, pair[1].id, str=str(sub))

for line in nx.generate_edgelist(G, data=False):
    print(line)

# Draw graph
# AG = nx.nx_agraph.to_agraph(G)
# AG.layout()
# AG.draw(f'graph.png')

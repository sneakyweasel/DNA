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
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_tree.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
print(f"NODES: {n}")

# Process file
pairs = []
for line in lines:
    pairs.append([int(x) for x in line.split(" ")])

# Create graph
G = nx.Graph()

# Place nodes
for i in range(1, n):
    G.add_node(i)


# Place edges
for pair in pairs:
    G.add_edge(pair[0], pair[1])

# Number of connected components
result = nx.number_connected_components(G)
print(result - 1)

# Draw graph
AG = nx.nx_agraph.to_agraph(G)
AG.layout()
AG.draw(f'tree.png')

import os
import sys
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ts.txt'))
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
G = nx.DiGraph()

# Place edges
for pair in pairs:
    G.add_edge(pair[0], pair[1])
    print(pair[0], pair[1])

# Topological sort
results = list(nx.topological_sort(G))

print(" ".join([str(x) for x in results]))

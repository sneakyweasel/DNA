import os
import sys
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_scc.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
m = int(first_line.split(" ")[1])
print(f"VERTICES: {n} - EDGES: {m}")

# Process file
pairs = []
for line in lines:
    pairs.append([int(x) for x in line.split(" ")])

# Create graph
G = nx.DiGraph()

# Place vertices
for i in range(1, n+1):
    G.add_node(i)

# Place edges
for pair in pairs:
    G.add_edge(pair[0], pair[1])

# SCC
results = nx.number_strongly_connected_components(G)
print(results)

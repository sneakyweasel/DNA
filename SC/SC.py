import os
import sys
import networkx as nx
from networkx.algorithms import bipartite
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_sc.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
print(lines)

# Process file
graphs = []
pairs = []
for line in lines:
    if len(line.split(" ")) == 2:
        pairs.append([int(x) for x in line.split(" ")])
    else:
        pairs = []
        graphs.append(pairs)

# Iterate graphs
i = 0
results = []
for graph in graphs:
    graph.pop(0)

    # Create graph
    G = nx.DiGraph()
    i += 1

    # Place edges
    for pair in graph:
        G.add_edge(pair[0], pair[1])

    # Compute connected components
    if nx.is_semiconnected(G) == True:
        results.append(1)
    else:
        results.append(-1)

    # AG = nx.nx_agraph.to_agraph(G)
    # AG.layout()
    # AG.draw(f'file{i}.png')

print(" ".join([str(x) for x in results]))

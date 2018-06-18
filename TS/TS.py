import os
import sys
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_dag.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
print(lines)
# lines.pop(0)

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
results = []

for graph in graphs:
    print(graph)
    # Create graph
    G = nx.DiGraph()

    # Place edges
    for pair in graph:
        G.add_edge(pair[0], pair[1])
        print(pair[0], pair[1])

    # Find cycles
    if nx.is_directed_acyclic_graph(G) == True:
        results.append(1)
    else:
        results.append(-1)


print(" ".join([str(x) for x in results]))

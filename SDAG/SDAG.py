import os
import sys
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_sdag.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
print(lines)

# Process file
pairs = []
for line in lines:
    pairs.append([int(x) for x in line.split(" ")])

# Iterate graphs
results = []

# Create graph
G = nx.DiGraph()

# Unique nodes
flat_list = [val for sublist in pairs for val in sublist]
uniq_node = list(set(flat_list))
for node in range(1, max(uniq_node)):
    G.add_node(node)
print(f"Nodes: {max(uniq_node)}")

# Place edges
for pair in pairs:
    G.add_edge(pair[0], pair[1], weight=pair[2])

# Compute connected components
sd = nx.single_source_bellman_ford_path_length(G, 1)
results = []
for i in range(1, n+1):
    if i not in sd:
        sd[i] = 'x'
    results.append(sd[i])


# Viz
# AG = nx.nx_agraph.to_agraph(G)
# AG.layout()
# AG.draw(f'viz.png')

print(" ".join([str(x) for x in results]))

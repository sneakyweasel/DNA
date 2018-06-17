import os
import sys
import networkx as nx

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_cc.txt'))
lines = [line.rstrip('\n') for line in file]

pairs = []
for line in lines:
    pairs.append([int(x) for x in line.split(" ")])
print(pairs)
pairs.pop(0)

# Create graph
G = nx.Graph()

# Unique nodes
flat_list = [val for sublist in pairs for val in sublist]
uniq_node = list(set(flat_list))
for node in range(1, max(uniq_node)):
    G.add_node(node)

# Place edges
for pair in pairs:
    G.add_edge(pair[0], pair[1])

# Compute connected components
results = len(list(nx.connected_components(G)))
print(results)

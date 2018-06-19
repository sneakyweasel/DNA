import os
import sys
import networkx as nx

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_hdag.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])

# Process file
graphs = []
pairs = []
for line in lines:
    if len(line.split(" ")) == 2:
        pairs.append([int(x) for x in line.split(" ")])
    else:
        pairs = []
        graphs.append(pairs)
print(f"LEN: {len(graphs)}")

# Iterate graphs
i = 0
results = []
for graph in graphs:
    max = graph.pop(0)[0]

    G = nx.DiGraph()
    for pair in graph:
        if pair[0] != pair[1]:
            G.add_edge(pair[0], pair[1])

    # Place edges
    try:
        path = nx.dag_longest_path(G)
    except nx.exception.NetworkXUnfeasible:
        path = [-1]

    if len(path) == max:
        results.append([1] + path)
    else:
        results.append([-1])

    # AG = nx.nx_agraph.to_agraph(G)
    # AG.layout()
    # AG.draw(f'file{i}.png')

for result in results:
    print(" ".join([str(x) for x in result]))

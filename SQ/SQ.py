import os
import sys
import networkx as nx
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_sq.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
# print(lines)

# Process file
graphs = []
pairs = []
for line in lines:
    if len(line.split(" ")) == 2:
        pairs.append([int(x) for x in line.split(" ")])
    else:
        pairs = []
        graphs.append(pairs)
print(len(graphs))

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
        G.add_edge(pair[1], pair[0])

    # Compute simple cycles
    simple_cycles = list(nx.simple_cycles(G))
    square = -1
    for cycle in simple_cycles:
        if len(cycle) == 4:
            print(cycle)
            square = 1
            break
    print(f"{i}: {square}")
    results.append(square)

    # AG = nx.nx_agraph.to_agraph(G)
    # AG.layout()
    # AG.draw(f'file{i}.png')


print(" ".join([str(x) for x in results]))

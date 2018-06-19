import os
import sys
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_cte.txt'))
lines = [line.rstrip('\n') for line in file]

# Remove header
first_line = lines.pop(0)
n = int(first_line.split(" ")[0])
print(lines)

# Process file
graphs = []
pairs = []
for line in lines:
    if len(line.split(" ")) == 3:
        pairs.append([int(x) for x in line.split(" ")])
    elif len(line.split(" ")) == 2:
        print("New block")
    else:
        pairs = []
        graphs.append(pairs)

print(graphs)
# Iterate graphs
i = 0
for graph in graphs:
    graph.pop(0)

    # Create graph
    G = nx.DiGraph()
    i += 1

    # Place edges
    for pair in graph:
        G.add_edge(pair[0], pair[1], weight=pair[2])

    # Compute connected components
    results = []
    try:
        cycle = list(nx.simple_cycles(G))
    except:
        cycle = [-1]
    print(f"Cycle {i}: {cycle}")

    AG = nx.nx_agraph.to_agraph(G)
    AG.layout()
    AG.draw(f'file{i}.png')


print(" ".join([str(x) for x in results]))

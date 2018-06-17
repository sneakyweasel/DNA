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


# Iterate graphs
i = 0
for graph in graphs:
    # Create graph
    G = nx.DiGraph()
    i += 1

    # Unique nodes
    flat_list = [val for sublist in graph for val in sublist]
    uniq_node = list(set(flat_list))
    for node in range(1, max(uniq_node)):
        G.add_node(node)

    # Place edges
    for pair in graph:
        G.add_edge(pair[0], pair[1], weight=pair[2])

    # Compute connected components
    results = []
    cycle = list(nx.simple_cycles(G))[0]
    print(cycle)
    total = 0
    for x in range(0, len(cycle) - 1):
        start = cycle[x]
        end   = cycle[x+1]
        weight = G[start][end]['weight']
        # print(f"EDGE: {cycle[x]} {cycle[x+1]}: {weight}")
        total += weight
    print(f"Total: {total}")

    AG = nx.nx_agraph.to_agraph(G)
    AG.write("file.dot")
    AG.layout()
    AG.draw(f'file{i}.png')


print(" ".join([str(x) for x in results]))

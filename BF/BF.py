import os
import sys
import networkx as nx
import matplotlib.pyplot as plt

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_bf.txt'))
lines = [line.rstrip('\n') for line in file]

n = int(lines[0].split(" ")[0])

pairs = []
for line in lines:
    pairs.append([int(x) for x in line.split(" ")])
print(pairs)
pairs.pop(0)

# Create graph
G = nx.DiGraph()

# Unique nodes
flat_list = [val for sublist in pairs for val in sublist]
uniq_node = list(set(flat_list))
for node in range(1, max(uniq_node)):
    G.add_node(node)

# Place edges
for pair in pairs:
    G.add_edge(pair[0], pair[1], weight=pair[2])

# Compute connected components
results = []
for x in range(1, n+1):
    try:
        path = nx.bellman_ford_path_length(G, 1, x)
    except:
        path = "x"
    results.append(path)

print(results)
print(" ".join([str(x) for x in results]))

# nx.draw_networkx(G)
# plt.savefig("dji.png")
# plt.show()

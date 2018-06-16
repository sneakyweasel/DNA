import os
import sys
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_ddeg.txt'))
lines = [line.rstrip('\n') for line in file]

pairs = []
for line in lines:
    pairs.append([int(x) for x in line.split(" ")])
print(pairs)
pairs.pop(0)

flat_list = [val for sublist in pairs for val in sublist]
uniq_node = list(set(flat_list))
print(uniq_node)

# Create directed graph
G = pgv.AGraph()
for pair in pairs:
    G.add_edge(str(pair[0]), str(pair[1]))

results = []
for x in uniq_node:
    adj_nodes = G.neighbors(str(x))
    print(f"{x} : {adj_nodes}")
    total = 0
    for adj_node in adj_nodes:
        nei = G.neighbors(adj_node)
        total += len(nei)
    results.append(total)
print(results)

print(" ".join([str(x) for x in results]))

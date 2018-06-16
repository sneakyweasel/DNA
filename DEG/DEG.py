import os
import sys
import pygraphviz as pgv

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_deg.txt'))
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
    results.append(len(G.neighbors(str(x))))
    print(f"{x} : {G.neighbors(str(x))}")
print(results)

print(" ".join([str(x) for x in results]))

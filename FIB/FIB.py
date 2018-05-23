import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_fib.txt'))
dna = file.read()
print(dna)
# dna = "5 3"
n = int(dna.split(' ')[0])
k = int(dna.split(' ')[1])
population = [1, 1]

def next_generation(population, k):
    current = population[-1]
    # reproductor_pairs = (population - (population % 2)) / 2
    offsprings = population[-2] * k
    result = current + offsprings
    return result

for i in range(0, n - 2):
    population.append(next_generation(population, k))

print(population[-1])



# Any given month will contain the rabbits that were alive the previous month, plus any new offspring.
# A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior.
# The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
# start = 1
# current = alive(prevmonth) + offsprings

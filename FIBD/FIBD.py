import os
import sys

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_fibd.txt'))
vars = file.read()
print(vars)
# vars = "6 3"
n = int(vars.split(' ')[0])
m = int(vars.split(' ')[1])
k = 1

# Populate first generation
population = [1]
for x in range(1, m):
    population.append(0)
print(population)

# Dynamic programming of next generation
def next_generation(population, k, m):
    # Current population
    current_babies = population[0]
    reproductors   = sum(population) - current_babies

    # Reproduce
    new_babies = reproductors * k

    # Age and kill rabbits
    current_dying = population[-1]

    # Shift months
    deaths = population.pop()
    population.insert(0, new_babies)
    return population

results = []
for i in range(2, n+1):
    current = next_generation(population, k, m)
    results.append(current)
    print(current)

print(sum(current))




# Any given month will contain the rabbits that were alive the previous month, plus any new offspring.
# A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior.
# The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
# start = 1
# current = alive(prevmonth) + offsprings

import os
import sys
import random
import itertools
from scipy.special import comb

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_lia.txt'))
vars = file.read()
k = int(vars.split(' ')[0]) # number of generations
N = int(vars.split(' ')[1]) # number of Aa Bb organisms

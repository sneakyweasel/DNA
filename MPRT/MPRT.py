import os
import sys
import string
import urllib.request
import requests
import re

# PROBLEM: Finding a Protein Motif
# To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

# Read input file and extract ids
ids = []
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_mprt.txt'))
for line in file.read().splitlines():
    ids.append(line)
# ids = ["A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]

# Retrieve dna sequence from fatsa remote file on uniprot
def get_fatsa(url):
    # contents = urllib.request.urlopen(urls[0]).read().decode("utf-8")
    contents = requests.get(url).content.decode("utf-8")
    lines = [s.strip() for s in contents.splitlines()]
    lines.pop(0)
    dna = ''.join(lines)
    return dna

# Protein REGEX motif detection N{P}[ST]{P} - /(N{1}[^P]{1}[S|T]{1}[^P]{1})\w+/g
# X    | X            | X
# [XY] | X or Y       | X|Y
# {X}  | Any except X | [^X]
def protein_motif(dna):
    regex = r"(?=N[^P][S|T][^P])"
    matches = re.finditer(regex, dna)
    indexes = []
    for match in matches:
        indexes.append(match.start() + 1)
    return indexes

# Connect to uniprot with id and retrieve the fatsa for the protein
urls = []
for id in ids:
    url = "http://www.uniprot.org/uniprot/" + id + ".fasta"
    dna = get_fatsa(url)
    matches = protein_motif(dna)
    if len(matches) != 0:
        print(id)
        print(' '.join(str(x) for x in matches))

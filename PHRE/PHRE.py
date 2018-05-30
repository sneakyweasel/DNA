import os
import sys
from Bio import ExPASy
from Bio import Entrez
from Bio import SeqIO

file = open(os.path.join(os.path.dirname(sys.argv[0]), 'rosalind_phre.txt'))
# lines = [line for line in file]
# score = lines.pop(0)
# print(score)
threshold = 26

records = list(SeqIO.parse(file, "fastq"))
print("Found %i records" % len(records))

length = len(records[0].letter_annotations["phred_quality"])
counter = 0
for x in range(0, length):
    total = 0
    for record in records:
        total += record.letter_annotations["phred_quality"][x]
        # print(record.letter_annotations["phred_quality"])
    mean = total / len(records)
    print(f"Mean: {mean}")
    if mean < threshold:
        counter += 1

print(counter)

# Used FASTQC: 48

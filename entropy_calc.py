# entropy_calc.py
import sys
from math import log2
from Bio import AlignIO

def shannon_entropy(column):
    freqs = {}
    total = 0
    for aa in column:
        if aa != '-':  # αγνοούμε gaps
            freqs[aa] = freqs.get(aa, 0) + 1
            total += 1
    entropy = 0
    for aa in freqs:
        p = freqs[aa] / total
        entropy -= p * log2(p)
    return entropy

alignment = AlignIO.read(sys.argv[1], "fasta")
length = alignment.get_alignment_length()

with open(sys.argv[2], "w") as out:
    for i in range(length):
        column = alignment[:, i]
        ent = shannon_entropy(column)
        out.write(f"{i+1}\t{ent:.4f}\n")


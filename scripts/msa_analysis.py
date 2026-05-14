#!/usr/bin/env python3
from Bio import AlignIO
from collections import Counter
import math
import sys

def calc_entropy(freqs):
    """Calculate Shannon entropy in bits for one position"""
    total = sum(freqs.values())
    entropy = 0
    for aa, count in freqs.items():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

# Input alignment
alignment_file = sys.argv[1]
alignment = AlignIO.read(alignment_file, "fasta")
alignment_length = alignment.get_alignment_length()

print("Pos\tConsensus\tEntropy\tFrequencies")
for i in range(alignment_length):
    col = [record.seq[i] for record in alignment]
    freqs = Counter(col)
    # remove gaps and unknown X amino acids from alignments
    filtered_freqs = {aa: c for aa, c in freqs.items() if aa != '-' and aa != 'X'}
    if filtered_freqs:
        consensus = max(filtered_freqs, key=filtered_freqs.get)
    else:
        consensus = '-'
    entropy = calc_entropy(filtered_freqs)
    freqs_str = ";".join(f"{aa}:{count}" for aa, count in filtered_freqs.items())
    print(f"{i+1}\t{consensus}\t{entropy:.3f}\t{freqs_str}")


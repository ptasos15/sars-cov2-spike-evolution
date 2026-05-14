#!/bin/bash

# Activate conda environment
conda activate sarsphylo

# Merge FASTA files
cat *.fasta > all_europe.fasta

# Add Wuhan reference
cat all_europe.fasta sequencesWUHAN.fasta > all_europe_plus_wuhan.fasta

# Alignment
nextalign run \
  --input-ref sarscov2_ref/reference.fasta \
  --genemap sarscov2_ref/genemap.gff \
  --output-fasta aligned_sarscov2.fasta \
  all_europe.fasta

# Remove insertions and ambiguous regions
seqkit seq -u aligned_sarscov2.fasta > aligned_no_insertions.fasta

seqkit subseq -r 266:29674 aligned_no_insertions.fasta \
> aligned_coding.fasta

seqkit grep -v -r -p "N{300,}" aligned_coding.fasta \
> aligned_clean.fasta

# Whole genome phylogeny
iqtree2 \
  -s aligned_clean.fasta \
  -m GTR+G \
  -bb 1000 \
  -nt AUTO

# Extract Spike region
seqkit subseq -r 21563:25384 aligned_sarscov2.fasta \
> aligned_spike_nt.fasta

# Translate Spike protein
seqkit translate aligned_spike_nt.fasta \
> aligned_spike_aa.fasta

# Spike phylogeny
iqtree2 \
  -s aligned_spike_aa.fasta \
  -m LG+G \
  -bb 1000 \
  -nt AUTO

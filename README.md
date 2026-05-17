# SARS-CoV-2 Spike Protein Evolution Analysis

## Overview
This repository contains the code and analysis workflow used to investigate the temporal evolution of the SARS-CoV-2 Spike protein using phylogenetic reconstruction and Shannon entropy analysis. The study compares early pandemic sequences from Greece (2020) with later European datasets (2022) to evaluate patterns of amino acid variability, diversification and fixation across the Spike glycoprotein.

## Methods
The workflow includes:

- Multiple sequence alignment using Nextalign
- Sequence filtering and cleaning
- Spike protein extraction and amino acid translation
- Phylogenetic tree reconstruction using IQ-TREE
- Site-specific Shannon entropy calculation
- Comparative analysis between Greece 2020 and Europe 2022 datasets

## Repository Structure

```text
scripts/        Python analysis scripts
workflow/       Bash workflow pipeline
results/        Trees and entropy outputs
data/           Processed datasets and metadata
```
## Scripts
- msa_analysis.py : 
  Calculates amino acid frequencies and Shannon entropy per Spike position.
- entropy_calc.py :
  Computes Shannon entropy across aligned Spike protein sequences.
- delta_entropy.py :
  Calculates entropy differences between datasets.
- conserved_positions.py :
  Identifies conserved amino acid positions across alignments.

## Phylogenetic Tree Visualization
Phylogenetic trees were visualized and annotated using the Interactive Tree of Life (iTOL) platform. Custom Python scripts were developed to automatically assign country-specific color annotations based on sequence metadata extracted from Newick tree labels.

Countries were color-coded as follows:

- Greece → light blue
- Italy → green
- France → orange
- Germany → yellow
- Spain → purple
- Slovakia → pink
- Russia → red
- United Kingdom → turquoise

The script generates iTOL-compatible DATASET_COLORSTRIP annotation files for visualization of geographic clustering patterns.

## Lineage Annotation and Visualization
SARS-CoV-2 phylogenetic trees were additionally annotated according to Pangolin lineage classifications. Sequence headers were reformatted to include accession number, lineage assignment and country metadata prior to tree reconstruction.

Custom annotation files compatible with the Interactive Tree of Life (iTOL) platform were generated using Python scripts, enabling lineage-specific and country-specific color visualization of phylogenetic clustering patterns.

## Entropy Analysis and Statistical Visualization
Shannon entropy profiles were calculated across aligned Spike protein amino acid sequences to quantify site-specific variability.

Entropy analyses included:

- Greece 2020 Spike dataset
- Europe 2022 Spike dataset
- ΔEntropy comparison between datasets
- Smoothed entropy profiles
- Receptor-Binding Domain (RBD) highlighting
- Volcano-style variability plots
- Mean entropy comparison between populations

Statistical visualization and plotting were performed in R using custom scripts and ggplot2.

## Data Availability
Sequence datasets were obtained from the NCBI Virus Database. Processed datasets, metadata and analysis outputs used in this study are included in this repository and in the Supplementary Material associated with the manuscript.

## Results
The repository contains:
- Whole-genome phylogenetic trees
- Spike protein phylogenetic trees
- Amino acid entropy profiles
- Delta entropy analyses
- Conserved position analyses
- Processed FASTA alignments

## Reproducibility
The complete analysis can be reproduced using the provided scripts and workflow pipeline. Required software includes:
- Nextalign
- IQ-TREE
- SeqKit
- Python 3
- Biopython
- pandas

## Citation
If you use this repository, please cite:

Panagoulias A. SARS-CoV-2 Spike Protein Evolution Analysis. GitHub repository (2026).

## License
This project is distributed under the MIT License.


  

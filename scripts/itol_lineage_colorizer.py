#!/usr/bin/env python3
"""
iTOL Lineage Colorstrip - Create separate circle for lineages (ex. A, B..)
Reads IDs directly from the Newick tree file
"""

import re
from urllib.parse import unquote

# Colors for main lineages 
LINEAGE_COLORS = {
    'A': '#FF6B6B',      # Light red
    'B': '#4ECDC4',      # Turquoise
    'C': '#FFD93D',      # Yellow
    'D': '#95E1D3',      # Mint
    'E': '#F38181',      # Coral
    'F': '#AA96DA',      # Light purple
    'G': '#FCBAD3',      # Light pink
    'H': '#A8E6CF',      # Light green 
}

def parse_newick(newick_file):
    """Reads the Newick tree and extracts the IDs with the lineages"""
    sequences = {}
    
    with open(newick_file, 'r') as f:
        newick_content = f.read()
    
    # URL decode
    newick_content = unquote(newick_content)
    
    # Find all the IDs in newick
    # Pattern: ID|Lineage|Country:distance
    pattern = r"[\(,]([A-Z0-9_]+\|[A-Z0-9\.]+\|[A-Za-z_]+):"
    matches = re.findall(pattern, newick_content)
    
    for seq_id in matches:
        if '|' in seq_id:
            parts = seq_id.split('|')
            if len(parts) >= 3:
                lineage_full = parts[1].strip()  # ex. "B.1.1", "BA.2", "AY.4"
                # Take ONLY the first letter (ex. A, B, C..)
                lineage_main = lineage_full[0] if lineage_full else 'Unknown'
                sequences[seq_id] = lineage_main
    
    return sequences

def create_itol_lineage_colorstrip(sequences, output_file):
    """Create iTOL colored strip for main lineages"""
    
    with open(output_file, 'w') as f:
        # Header of iTOL file
        f.write("DATASET_COLORSTRIP\n")
        f.write("SEPARATOR TAB\n")
        f.write("DATASET_LABEL\tVirus Lineages\n")
        f.write("COLOR\t#000000\n")
        f.write("STRIP_WIDTH\t50\n")
        f.write("MARGIN\t10\n")
        f.write("SHOW_INTERNAL\t0\n")
        f.write("BORDER_WIDTH\t1\n")
        f.write("BORDER_COLOR\t#000000\n")
        
        # Find the lineages that exist in the dataset
        unique_lineages = sorted(set(sequences.values()))
        
        # Legend - only for the lineages that exist
        f.write("\n# Legend\n")
        f.write("LEGEND_TITLE\tLineages\n")
        f.write("LEGEND_SHAPES")
        for lineage in unique_lineages:
            f.write(f"\t1")
        f.write("\n")
        
        f.write("LEGEND_COLORS")
        for lineage in unique_lineages:
            color = LINEAGE_COLORS.get(lineage, '#CCCCCC')  # grey if it doesn't exist!
            f.write(f"\t{color}")
        f.write("\n")
        
        f.write("LEGEND_LABELS")
        for lineage in unique_lineages:
            f.write(f"\t{lineage}")
        f.write("\n")
        
        # Data section
        f.write("\n# Data\n")
        f.write("DATA\n")
        
        # For each sequence, write color of main lineage
        for seq_id, lineage in sorted(sequences.items()):
            color = LINEAGE_COLORS.get(lineage, '#CCCCCC')
            f.write(f"{seq_id}\t{color}\t{lineage}\n")
    
    print(f" Created file: {output_file}")
    print(f" Found {len(sequences)} sequences in tree")
    
    # Statistics
    lineage_counts = {}
    for lineage in sequences.values():
        lineage_counts[lineage] = lineage_counts.get(lineage, 0) + 1
    
    print("\n Statistics for each lineage:")
    for lineage, count in sorted(lineage_counts.items()):
        color_code = LINEAGE_COLORS.get(lineage, '#CCCCCC')
        print(f"  Lineage {lineage}: {count} sequences (color: {color_code})")

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Use: python3 itol_lineage_colorstrip.py <newick_file>")
        print("\nExample: python3 itol_lineage_colorstrip.py g2NGvTaE75Qnlzg_newick.txt")
        sys.exit(1)
    
    newick_file = sys.argv[1]
    output_file = "itol_lineage_colorstrip.txt"
    
    print(f" Read tree from: {newick_file}")
    sequences = parse_newick(newick_file)
    
    print(f" Creation of iTOL lineage colorstrip annotation...")
    create_itol_lineage_colorstrip(sequences, output_file)
    
    print(f"\n Ready! Upload file '{output_file}' in iTOL")
    print("   (Drag & Drop in tree)")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
iTOL Country Label Colorizer - 8 European Countries
"""

import re
from urllib.parse import unquote

# Colors for each counrty (8 different colors)
COUNTRY_COLORS = {
    'Russia': '#FF0000',           # Red
    'Greece': '#87CEEB',           # Light blue
    'Italy': '#00FF00',            # Green
    'France': '#FFA500',           # Orange
    'Germany': '#FFFF00',          # Yellow
    'Slovakia': '#FF69B4',         # Pink
    'Spain': '#9370DB',            # Purple
    'United_Kingdom': '#00CED1',   # Turquoise (with underscore for file)
    'United Kingdom': '#00CED1',   # Turquoise (without underscore for iTOL)
    'China': '#FFB6C1'             # Light Pink
}

def parse_newick(newick_file):
    """This reads the Newick tree and exports the IDs with the countries"""
    sequences = {}
    
    with open(newick_file, 'r') as f:
        newick_content = f.read()
    
    #  URL decode to fix the names (ex. Fra% -> France)
    newick_content = unquote(newick_content)
    
    # Find all IDs in newick tree (ex. PQ995252|AY.43|France)
    # Pattern : ID|Lineage|Country:distance
    # WARNING: Countries with underscore (ex. United_Kingdom)!
    pattern = r"[\(,]([A-Z0-9_]+\|[A-Z0-9\.]+\|[A-Za-z_]+):"
    matches = re.findall(pattern, newick_content)
    
    print(f"🔍 DEBUG: Found {len(matches)} matches from regex")
    if len(matches) > 0:
        print(f"   Example of first match: {matches[0]}")
    
    for seq_id in matches:
        # Export each country (then put | to separate metadata!)
        if '|' in seq_id:
            parts = seq_id.split('|')
            if len(parts) >= 3:
                country = parts[2].strip()
                sequences[seq_id] = country
    
    return sequences

def create_itol_label_styles(sequences, output_file):
    """Creates iTOL colorstrip annotation file"""
    
    with open(output_file, 'w') as f:
        # Header of iTOL file - use DATASET_COLORSTRIP
        f.write("DATASET_COLORSTRIP\n")
        f.write("SEPARATOR SPACE\n")
        f.write("DATASET_LABEL Country_Colors\n")
        f.write("COLOR #ff0000\n")
        f.write("\n")
        
        # Legend
        f.write("LEGEND_TITLE Countries\n")
        f.write("LEGEND_SHAPES")
        for _ in COUNTRY_COLORS:
            f.write(" 1")
        f.write("\n")
        
        f.write("LEGEND_COLORS")
        for color in COUNTRY_COLORS.values():
            f.write(f" {color}")
        f.write("\n")
        
        f.write("LEGEND_LABELS")
        for country in COUNTRY_COLORS.keys():
            f.write(f" {country}")
        f.write("\n")
        
        f.write("\n")
        f.write("DATA\n")
        
        # For each sequence, write color
        # Format: ID color label (Without quotes!)
        for seq_id, country in sorted(sequences.items()):
            if country in COUNTRY_COLORS:
                color = COUNTRY_COLORS[country]
                f.write(f"{seq_id} {color} {country}\n")
    
    print(f"✓ Created file: {output_file}")
    print(f"✓ Found {len(sequences)} sequences in tree")
    
    # Statistics
    country_counts = {}
    for country in sequences.values():
        country_counts[country] = country_counts.get(country, 0) + 1
    
    print("\n Statistics for each country:")
    for country, count in sorted(country_counts.items()):
        color_code = COUNTRY_COLORS.get(country, 'N/A')
        print(f"  {country}: {count} sequences (color: {color_code})")
    
    # Warning for colors without color
    unknown_countries = set()
    for country in sequences.values():
        if country not in COUNTRY_COLORS:
            unknown_countries.add(country)
    
    if unknown_countries:
        print("\n  Warning! Countries found without color:")
        for country in sorted(unknown_countries):
            print(f"  - {country}")

def main():
    import sys
    
    # Newick tree file
    if len(sys.argv) < 2:
        print("Use: python3 itol_8countries.py <newick_file>")
        print("\nExample: python3 itol_8countries.py tree.treefile")
        print("           python3 itol_8countries.py alignment.fasta.treefile")
        sys.exit(1)
    
    newick_file = sys.argv[1]
    output_file = "itol_8countries_labels.txt"
    
    print(f" Read tree from: {newick_file}")
    sequences = parse_newick(newick_file)
    
    print(f" Creation of iTOL label styles...")
    create_itol_label_styles(sequences, output_file)
    
    print(f"\n Ready! Upload '{output_file}' in iTOL")
    print("   (Drag & Drop in tree)")
    print("\n Colors:")
    for country, color in sorted(COUNTRY_COLORS.items()):
        print(f"   {country}: {color}")

if __name__ == "__main__":
    main()

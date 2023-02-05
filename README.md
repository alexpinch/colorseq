# FASTA Colours
FASTA Colours is a fun and simple Python script that creates a list of hexadecimal colour codes from the counted base pairs of a given FASTA file. These values can be imported into R as a colour palette for plotting figures.  

## How it works  
Bases G and T are converted to the nearest alphabetical characters in the hexadecimal range (A-F): G and T are replaced with D and E respectively. Base pair counts are truncated so that only the first digit is kept. The converted base pair counts are then cycled to create 4 hexadecimal colour codes, and outputted to a CSV in your home directory.

## How to run    
Run ```main.py```, and input the directory to your FASTA file.  
If using the example FASTA file, this should output:  
  
```
Counted base pairs:   
A = 787, G = 566, C = 621, , T = 783  

Output:  
'#7A5B6C', '#5B6C7D', '#6C7D7A', '#7D7A5B'  
```  
  
You can find the CSV hex codes in your home directory, saved as ```FASTA_hex_colours.csv```  
The script also outputs a plot showcasing the palette. If using the example FASTA file, this should output:  
  
<img align="center" src="https://raw.githubusercontent.com/alexpinch/FASTA-colours/main/example_data/example_palette.png" width=500/>  

## Dependencies  
```python
from Bio import SeqIO
import math, csv
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
```  

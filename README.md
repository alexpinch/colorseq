# FASTA-colours
FASTA colours is Python script that creates a list of hexadecimal colour codes from the counted base pairs of a given FASTA file. These values can be imported into R as a colour palette for plotting figures.  

## How it works  
Since bases G and T are outside the hexadecimal colour range (0-9 and A-F), they are converted to the nearest alphabetic characaters (G=D, T=E). Base pair counts are truncated so that only the first digit is kept. The converted base pair counts are then cycled to create 4 hexadecimal colour codes, and outputted to a CSV in your home directory.

## Dependencies  
```python
from Bio import SeqIO
import math, csv
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
```  

## Example I/O  
Run ```main.py```, and input the directory to your FASTA file.  
  
```
Counted base pairs:   
A = 787, G = 566, C = 621, , T = 783  

Output:  
'#7A5B6C', '#5B6C7D', '#6C7D7A', '#7D7A5B'  
```  
  
```FASTA_hex_colours.csv``` is saved to your home directory.  
  
<img align="left" src="https://raw.githubusercontent.com/alexpinch/FASTA-colours/main/example_data/example_palette.png" width=500/>  

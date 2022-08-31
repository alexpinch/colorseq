# FASTA-colours
A script that creates a list of hexadecimal colour codes from the counted base pairs of a given FASTA file. These values can be imported into R as a colour palette for plotting figures.  
  
## How it works  
Since bases G and T are outside the hexadecimal colour range (0-9 and A-F), they are converted to the nearest alphabetic characaters. Therefore, G becomes D and T becomes E. Base pair counts are truncated so that only the first digit is kept. The converted base pair counts are then cycled to create 4 hexadecimal colour codes, outputted to a CSV. 

## Dependencies  
```python
from Bio import SeqIO
import math, csv
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
```  

## Example I/O  
Run the Python script 'FASTA_colours.py', and input your FASTA file.  
  
Counted base pairs:  
A = 1224, C = 6212, G = 782, T = 2825  
  
Output:  
1A6C7D  
6C7D2E  
7D2E1A  
2E1A6C  
  
<img align="left" src="https://raw.githubusercontent.com/alexpinch/FASTA-colours/main/examples/example_palette.png" width=200/>  

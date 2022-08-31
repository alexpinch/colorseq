from Bio import SeqIO
import math, csv
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# User passes a FASTA file, counts the base pairs
fastaName = input("Enter your FASTA file name (do not include extension .fasta): ")
fastaDirectory=fastaName + ".fasta"
inputFileName=fastaDirectory
seqObject = SeqIO.read(inputFileName,"fasta")
sequence=seqObject.seq
length=len(sequence)
A_counter, G_counter, C_counter, T_counter,  = 0, 0, 0, 0
for record in SeqIO.parse(inputFileName, "fasta"):
    A_counter += record.seq.count('A')
    G_counter += record.seq.count('G')
    C_counter += record.seq.count('C')
    T_counter += record.seq.count('T')

# Keeps the counts under 10, truncates the decimal into a whole number (example: 32 A's becomes 3, 256 becomes 2, 1024 becomes 1)
if A_counter < 100:
    A_counter = math.trunc(A_counter / 10)
elif A_counter > 100 and A_counter < 1000:
    A_counter = math.trunc(A_counter / 100)
else:
    A_counter = math.trunc(A_counter / 1000)

if G_counter < 100:
    G_counter = math.trunc(G_counter / 10)
elif G_counter > 100 and G_counter < 1000:
    G_counter = math.trunc(G_counter / 100)
else:
    G_counter = math.trunc(G_counter / 1000)

if C_counter < 100:
    C_counter = math.trunc(C_counter / 10)
elif C_counter > 100 and C_counter < 1000:
    C_counter = math.trunc(C_counter / 100)
else:
    C_counter = math.trunc(C_counter / 1000)

if T_counter < 100:
    T_counter = math.trunc(T_counter / 10)
elif T_counter > 100 and T_counter < 1000:
    T_counter = math.trunc(T_counter / 100)
else:
    T_counter = math.trunc(T_counter / 1000)

# Since G and T are outside the hexadecimal range, G is converted to C and T is converted to D
hex_colours = [str(A_counter)+"A"+str(G_counter)+"B"+str(C_counter)+"C", str(G_counter)+"B"+str(C_counter)+"C"+str(T_counter)+"D", str(C_counter)+"C"+str(T_counter)+"D"+str(A_counter)+"A", str(T_counter)+"D"+str(A_counter)+"A"+str(G_counter)+"B"]
print(hex_colours)

outputFileName=fastaName+"_hex_colours.csv"
# Saves hexadecimal values to a .csv
file = open(outputFileName, 'w')
writer = csv.writer(file)
writer.writerow(hex_colours)
file.close()

# Generate a palette image of the hexadecimal colour set.
X, Y = 0.0, 0.0
fig,ax = plt.subplots()
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((X, Y), 0.25, 1,
                      alpha=1, facecolor=hex_colours[0]))
currentAxis.add_patch(Rectangle((X+0.25, Y), 0.25, 1,
                      alpha=1, facecolor=hex_colours[1]))
currentAxis.add_patch(Rectangle((X+0.50, Y), 0.25, 1,
                      alpha=1, facecolor=hex_colours[2]))
currentAxis.add_patch(Rectangle((X+0.75, Y), 0.25, 1,
                      alpha=1, facecolor=hex_colours[3]))
plt.show()

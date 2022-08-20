## fasta-colours
A tool that creates an R colour palette from the counted base pairs of any given FASTA file!  
In case you've ever wanted to say "This figure's colour palette is straight from their DNA!"  
  
** How it works **  
Since hexadecimal colour codes range from 0-9 and A-F, A and C counts can be included while G and T must be converted. G becomes D and T becomes E.  
Base pair counts are truncated so only the first digit is kept.  
The converted base pair counts are cycled to create 4 hexadecimal colour codes.  
  
For example: A = 1224, C = 6212, G = 782, T = 2825  
1A6C7D  
6C7D2E  
7D2E1A  
2E1A6C  

f = open('rosalind_revc.txt', 'r');
dnaString = f.read()[0:-1];											# For this question the \n needs to be stripped
swaps = {'A':'T', 'T':'A', 'G':'C', 'C':'G'};
dnaString = ''.join(swaps[char] for char in dnaString[::-1]);
print(dnaString);
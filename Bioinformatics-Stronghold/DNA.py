f = open('rosalind_dna.txt', 'r');
dnaString = f.read();
print('{} {} {} {}'.format(dnaString.count('A'), dnaString.count('C'), dnaString.count('G'), dnaString.count('T')));
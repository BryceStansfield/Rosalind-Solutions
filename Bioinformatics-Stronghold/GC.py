f = open('rosalind_gc.txt', 'r');
current = f.readline()[1::1].strip();
maxGc = [current, 0];
dnaString = '';
for line in f:
	if(line[0] != '>'):
		dnaString += line.strip();
	else:
		if((dnaString.count('G') + dnaString.count('C')) / len(dnaString) > maxGc[1]):
			maxGc[0] = current;
			maxGc[1] = (dnaString.count('G') + dnaString.count('C')) / len(dnaString);
		current = line[1::1].strip();
		dnaString = '';
if((dnaString.count('G') + dnaString.count('C')) / len(dnaString) > maxGc[1]):
	maxGc[0] = current;
	maxGc[1] = (dnaString.count('G') + dnaString.count('C')) / len(dnaString);
print(maxGc[0]);
print(round(maxGc[1] * 100, 6));				# The final formatting requires it to be in percent to 6 decimal places
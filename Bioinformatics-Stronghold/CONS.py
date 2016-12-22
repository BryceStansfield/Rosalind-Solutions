from usefulFunctions import returnFastaAsDict
dna = returnFastaAsDict('rosalind_cons.txt');
occurances = [];
for i in range(0, len(dna[list(dna.keys())[0]])):
	occurances.append([0,0,0,0]);
for key in dna:
	for i in range(0, len(dna[key])):
		char = dna[key][i];
		if(char == 'A'):
			occurances[i][0] += 1;
		elif(char == 'C'):
			occurances[i][1] += 1;
		elif(char == 'G'):
			occurances[i][2] += 1;
		else:
			occurances[i][3] += 1;

consensus = '';
matrix = ['A: ', 'C: ', 'G: ', 'T: '];
for occurance in occurances:
	if(occurance[0] > occurance[1] and occurance[0] > occurance[2] and occurance[0] > occurance[3]):
		consensus += 'A';
	elif(occurance[1] > occurance[2] and occurance[1] > occurance[3]):
		consensus += 'C';
	elif(occurance[2] > occurance[3]):
		consensus += 'G';
	else:
		consensus += 'T';

	for i in range(0, 4):
		matrix[i] += ' ' + str(occurance[i]);

print(consensus);
for i in range(0, 4):																								# This came out huge, so I think I might start outputting to text files instead of console
	print(matrix[i]);
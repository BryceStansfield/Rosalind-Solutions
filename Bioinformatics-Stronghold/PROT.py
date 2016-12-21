import re
table = open('rnaCodonTable.txt', 'r');

# Parsing that table into a dict
acids = {};
for line in table:
	regex = re.search('([A-Z]*) (.*)', line.strip());
	acids[regex.group(1)] = regex.group(2);

# The rest of the questions
f = open('rosalind_prot.txt', 'r');
dna = f.read();
rna = '';													
stop = 0;
index = 0;
while(stop == 0):
	if(acids[dna[index:index+3]] != 'Stop'):
		rna += acids[dna[index:index+3]];
		index += 3;
	else:
		stop = 1;
print(rna);											
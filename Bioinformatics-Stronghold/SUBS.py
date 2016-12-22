f = open('rosalind_subs.txt', 'r');
dna = f.readline().strip();
subString = f.readline().strip();
locations = [];
stop = 0;

while(stop == 0):
	try:
		locations.append(dna.index(subString));
		dna = dna[dna.index(subString) + 1: -1];
	except ValueError:
		stop = 1;

for i in range(0, len(locations)):
	locations[i] += 1;
	if(i>0):
		locations[i] += locations[i-1];

print(str(locations).strip('[]').replace(',',''));
f = open('rosalind_hamm.txt', 'r');
first = f.readline().strip();
second = f.readline().strip();
mutations = 0;
for n in range(0, len(first)):
	if(first[n] != second[n]):
		mutations += 1;
print(mutations);
import re
f = open('rosalind_fib.txt', 'r');
regex = re.search('([0-9]*) ([0-9]*)', f.read());
months = int(regex.group(1));
pairs = int(regex.group(2));
rabbitPairs = [0,1];
for n in range(0, months-1):
	rabbitPairs = [rabbitPairs[1] + rabbitPairs[0], rabbitPairs[0] * pairs]
print(rabbitPairs[0] + rabbitPairs[1]);
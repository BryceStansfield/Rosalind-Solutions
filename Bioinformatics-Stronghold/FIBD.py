import re
f = open('rosalind_fibd.txt', 'r');
regex = re.search('([0-9]*) ([0-9]*)', f.read());
months = int(regex.group(1));
lifeSpan = int(regex.group(2));
dyingOnModMonth = [1];
for i in range(0, lifeSpan-1):
	dyingOnModMonth.append(0);
pairs = 1;													# This is just a modification of FIB.py, so it was easier to keep this in here, not to mention it stops me from using magic numbers
rabbitPairs = [0,1];
for n in range(1, months):									# Starting value changed to one to make the original mod one after the death of the original pair
	dyingThisMonth = dyingOnModMonth[n%lifeSpan];
	dyingOnModMonth[n%lifeSpan] = rabbitPairs[0] * pairs;
	rabbitPairs = [rabbitPairs[1] + rabbitPairs[0], rabbitPairs[0] * pairs];
	rabbitPairs[0] -= dyingThisMonth;
print(rabbitPairs[0] + rabbitPairs[1]);
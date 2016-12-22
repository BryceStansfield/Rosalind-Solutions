import re
f = open('rosalind_iev.txt', 'r');
regex = re.search('([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*)', f.read());															# Yeah, next time this happens I'll just write a parser
couples = [int(regex.group(1)), int(regex.group(2)), int(regex.group(3)), int(regex.group(4)), int(regex.group(5)), int(regex.group(6))];		# Yep, next time I'm definitely writing a parser																													# [Dom, non-Dom]
print((couples[0] + couples[1] + couples[2]) * 2 + couples[3] * 1.5 + couples[4]);																# All couples with an AA then Aa-Aa then Aa-aa

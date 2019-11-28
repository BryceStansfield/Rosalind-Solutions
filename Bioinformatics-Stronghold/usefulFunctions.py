def returnFastaAsDict(filePath):
	f = open(filePath, 'r')
	dna = {}
	temp = ['','']
	for line in f:
		line = line.strip()
		if(line[0] == '>'):
			if(temp[0] != ''):
				dna[temp[0]] = temp[1]
			temp[0] = line[1::1]
			temp[1] = ''
		else:
			temp[1] += line
	dna[temp[0]] = temp[1]
	return(dna)

def fact(n):
	prod = 1
	for i in range(2, n+1):
		prod *= i
	return(prod)

def choose(x,y):
	return(fact(x)/(fact(y)*fact(x-y)))
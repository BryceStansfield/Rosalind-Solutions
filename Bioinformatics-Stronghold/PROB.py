import math
inp = open("rosalind_prob.txt", "r")
dna = inp.readline().rstrip()
GCs = [float(i) for i in inp.readline().split(" ")]


letter_num = {"A":0, "C":1, "G":2, "T":3}

output = open("prob_out.txt", "w")
for gc in GCs:
    logs = [math.log10((1-gc)/2), math.log10(gc/2), math.log10(gc/2), math.log10((1-gc)/2)]
    output.write(str(sum(logs[letter_num[i]] for i in dna)) + " ")
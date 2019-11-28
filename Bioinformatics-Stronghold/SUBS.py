inp = open("rosalind_subs.txt", "r")
dna = inp.readline().rstrip()
search = inp.readline().rstrip()


output = open("Subs_out.txt", "w")
for i in range(0, len(dna)):
    if dna[i:i+len(search)] == search:
        output.write(" " + str(i+1))

import usefulFunctions
inp = open("rosalind_cons.txt", "r")
dna = usefulFunctions.returnFastaAsDict("rosalind_cons.txt")
titles = [t for t in dna]
dna_len = len(dna[titles[0]])

letter_num = {"A":0, "C":1, "G":2, "T":3}
num_letter = {0:"A", 1:"C", 2:"G", 3:"T"}
prof_mat = [[0 for i in range(0, dna_len)] for j in range(0, 4)]

for title in dna:
    string = dna[title]
    for i in range(0, len(string)):
        prof_mat[letter_num[string[i]]][i] += 1

cons_string = ""
for i in range(0, dna_len):
    best_so_far = -1
    most_so_far = -1
    for j in range(0,4):
        if prof_mat[j][i] > most_so_far:
            best_so_far = j
            most_so_far = prof_mat[j][i]
    
    cons_string += num_letter[best_so_far]

output = open("cons_out.txt", "w")
output.write(cons_string + "\n")
for j in range(0, 4):
    nums = ""
    for i in range(0, dna_len):
        nums += str(prof_mat[j][i]) + " "
    output.write(num_letter[j] + ": " + nums + "\n")
#Assignment 1, Q8
#this code takes in single DNA strand as input and computes base stacking energy

#creating list with all the unique bases
dnaBases = ["A", "T", "G", "C"]

#creating dictionary with all base pair
energies = {"AA" : -4, "AT": -7, "AC": -5, "AG": -11, "TA": -7,
            "TT": -2, "TC": -3, "TG": -4, "CA": -9, "CT": -5, "CC": -6, "CG": -7,
            "GA": -9, "GT": -6, "GC": -4, "GG": 11}


finalEnergy = 0
dnaString = input()
#input: CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG
start = 0

#will need to compute stacking energy by summing energy of pairs in dna string input
for end in range(len(dnaString)):
    if end - start + 1 > 2:
        start += 1

    if end - start + 1 == 2:
        word = dnaString[start:end+1]

        if word in energies:
            finalEnergy += energies.get(word)



print(finalEnergy/(len(dnaString)))

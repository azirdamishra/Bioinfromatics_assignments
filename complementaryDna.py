#Assignment 1, Q3
#Write a program to find complementary strand for the sequence

dnaSeq = input()
#input: CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG

#function to find the complement
def findComplement(letter):
    if letter == "A":
        return "T"
    if letter == "T":
        return "A"
    if letter == "G":
        return "C"
    if letter == "C":
        return "G"


finalStr = "" #result of the program

for letter in dnaSeq:
    finalStr += findComplement(letter)

print("Printing the complementary strand from 3' to 5'")
print(finalStr)
print("Printing the complementary strand from 5' to 3'")
print(finalStr[::-1])

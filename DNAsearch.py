#Assignment 1, Q6

#Write a code to search the DNA sequence provided in the Q4 for a specific string,
#The program should print the total number of matches for the given string and the positions
#of the matches. Run the code with different length of input string and observe the trend in
#no of matches

counter = 0 #to find the number of matches
positions = [] #will contain a list of the first coordinates of the matches

dnaSeq = "GACATTGTGAACAGTAAAAAAGTCCATGCAATGCGCAAGGAGCAGAAGAGGAAGCAGGGCAAGCAGCGCTCCATGGGCTCTCCCATGGACTACTCTCCTCTGCCCATCGACAAGCATGAGCCTGAATTTGGTCCATGCAGAAGAAAACTGGATGGG"
string = input() #user input of string to be found
start = 0

for end in range(len(dnaSeq)):

    #using a sliding window to check for strings
    if end - start + 1 > len(string):
        start += 1

    if end - start + 1 == len(string):
        word = dnaSeq[start:end+1]

        if word == string:
            counter += 1
            positions.append(end)

#printing the output
print("No of matches of the string: ", counter)
print("First index of the positions of the matches: ")
print(positions)

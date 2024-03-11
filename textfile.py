# textfile.py
# author: Joseph Benkanoun
# read in a text file and output the number of e's it contains
# program should take the filename from an argument on the command line

# initial attempt at coding the program
# trying to focus on the count before looking at reading in the file as an argument

FILENAME = "sample.txt"
counts = {}

with open (FILENAME, 'r') as txt:
    data = txt.read()
    for i in data:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

lower = counts['e']
upper = counts['E']
total = lower + upper

print(f"There are {total} instances of the letter E in this text. {lower} are lower case, {upper} are upper case.")

# this works however throws an error if lower or upper = 0 so needs further work
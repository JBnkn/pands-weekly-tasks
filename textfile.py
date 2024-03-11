# textfile.py
# author: Joseph Benkanoun
# read in a text file and output the number of e's it contains
# program should take the filename from an argument on the command line

FILENAME = "sample.txt"
counts = {}

with open (FILENAME, 'r') as txt:
    data = txt.read()
    for i in data:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

lower = counts.get('e', 0)
upper = counts.get('E', 0)
total = lower + upper

print(f"There are {total} instances of the letter E in this text. {lower} are lower case, {upper} are upper case.")

# used w3schools get method to define value for a key that doesn't exist
# https://www.w3schools.com/python/ref_dictionary_get.asp
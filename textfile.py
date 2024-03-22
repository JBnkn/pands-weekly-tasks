# textfile.py
# author: Joseph Benkanoun
# read in a text file and output the number of e's it contains
# program should take the filename from an argument on the command line

# importing sys module to read filename into command line as an argument
# was discussed in Week09 Errors lecture
# reviewed documentation at https://docs.python.org/3/library/sys.html#sys.argv
# also looked at https://www.youtube.com/watch?v=ZQ9JO0e9468
import sys

# taking filename as argument, I have set up sample.txt in the folder
FILENAME = sys.argv[1]

# set an empty dict to capture the counts
counts = {}

# open the file
with open (FILENAME, 'r') as txt:
    data = txt.read()
    # run through the data to capture instances of each character
    for i in data:
    # if the character is already in the dict, add one to the count
        if i in counts:
            counts[i] += 1
    # if not, assign it one for the first count
        else:
            counts[i] = 1

# check the counts for e and E in the dict
lower = counts.get('e', 0)
upper = counts.get('E', 0)

# combine them for the total
total = lower + upper

# print the total value and counts for lower and upper
print(f"There are {total} instances of the letter E in this text. {lower} are lower case, {upper} are upper case.")

# used w3schools get method to define value for a key that doesn't exist
# https://www.w3schools.com/python/ref_dictionary_get.asp
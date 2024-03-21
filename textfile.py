# textfile.py
# author: Joseph Benkanoun
# read in a text file and output the number of e's it contains
# program should take the filename from an argument on the command line

# prompt user to enter a filename (I have created sample.txt in the folder for demo purposes)

## TRY THESE
## https://askubuntu.com/questions/1059579/input-the-filename-in-the-commandline-as-an-argument-in-python
## https://www.youtube.com/watch?v=ZQ9JO0e9468
FILENAME = str(input("Please enter a filename (txt format only): "))

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
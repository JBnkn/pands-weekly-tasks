# collatz.py
# author: Joseph Benkanoun
# ask the user to input any positive integer and output the successive values of the following calculation:
# calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one

sequence = [] # defining a list to capture the sequence
num = abs(int(input("Enter an integer: "))) # prompting an input positive integer to begin the sequence
sequence.append(num) # appending the number to the list

while num != 1: # sequence will stop once it reaches 1
    if num % 2 == 0: # if number is even
        num = num//2 # divide number by 2 - this is the next number
        sequence.append(num) # append next number to list
    else: # if number isn't even it must be odd
        num = (num*3)+1 # multiply number by 3 and then add 1 - this is the next number
        sequence.append(num) # append next number to list

print(sequence[0:]) # when While loop ends (number reaches 1), print entire list

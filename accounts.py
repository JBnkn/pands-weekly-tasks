# accounts.py
# author: Joseph Benkanoun
# read a 10 character acct number and only output the last 4 digits

# prompting user to enter 10 digit number
acc_no = input("Please enter a 10 digit account number: ")

# added an error message if input is in the incorrect format (eg, a string)
while not acc_no.isdigit():
    print("Incorrect format.")
    acc_no = input("Please enter a 10 digit account number: ")
else:

# added an error message if account number of wrong length is input (eg, 5 digits)
    while len(acc_no) != 10:
        print("You have entered an invalid account number (incorrect number of digits)")
        acc_no = str(input("Please enter a 10 digit account number: "))
    else:
        digits = acc_no[-4:]
        print(f"XXXXXX{digits}")

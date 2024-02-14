# accounts.py
# author: Joseph Benkanoun
# read a 10 character acct number and only output the last 4 digits

# attempting to read last four digits as an spliced output
acc_no = str(input("Please enter a 10 digit account number: "))
digits = acc_no[-4:]
print(f"XXXXXX{digits}")

# this works and is straightforward enough
# will try to code it to deal with account numbers of any length
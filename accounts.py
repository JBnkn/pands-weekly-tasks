# accounts.py
# author: Joseph Benkanoun
# read a 10 character acct number and only output the last 4 digits

# attempting to add a function to deal with account numbers of any length
acc_no = str(input("Please enter a 10 digit account number: "))
digits = acc_no[-4:]
anon = "X"*(len(acc_no)-4)
print(f"{anon}{digits}")

# I have added a line which takes overall length of account number, subtracts four from overall length, and generates that many Xs
# it then adds those Xs as anon fields alongside the last four digits
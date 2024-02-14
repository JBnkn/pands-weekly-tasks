# accounts.py
# author: Joseph Benkanoun
# read a 10 character acct number and only output the last 4 digits

# attempting to add an error message if account number of wrong length is input
acc_no = str(input("Please enter a 10 digit account number: "))
digits = acc_no[-4:]
while len(acc_no) != 10:
    print("You have entered an invalid account number (incorrect number of digits)")
    acc_no = str(input("Please enter a 10 digit account number: "))
else:
    print(f"XXXXXX{digits}")

# this almost works as expected except second prompt to enter account number goes nowhere
# will have to look into ways to loop back to initial prompt rather than another prompt under IF statement
    
# learned about WHILE loops in Week04 which helped me solve what I was trying to do
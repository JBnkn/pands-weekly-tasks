# bank.py
# author: Joseph Benkanoun
# prompt user for two cent amounts and print output as a euro value

# still needed a solution to output a centvalue, so decided to try converting total to a string and only selecting the last two characters (the centvalue)
amount1 = int(input("Enter first amount (in c): "))
amount2 = int(input("Enter second amount (in c): "))
total = (amount1 + amount2)
eurovalue = total//100
print (f"The sum of these is €{eurovalue}.{str(total)[-2:]}")

# works broadly but doesn't work for total values under >10 so will need to determine a solution for those
# bank.py
# author: Joseph Benkanoun
# prompt user for two cent amounts and print output as a euro value

# had an idea to define euro value by dividing to integer and define cell value as remainder on the basis of arithmetic function learned in Week 2
amount1 = int(input("Enter first amount (in c): "))
amount2 = int(input("Enter second amount (in c): "))
total = (amount1 + amount2)
eurovalue = total//100
centvalue = total%100
print (f"The sum of these is €{eurovalue}.{centvalue}")

# doesn't work, as if centvalue < 10, the console only prints one decimal point so 02 becomes 2 (ie 27 + 75 = €1.2)
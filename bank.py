# bank.py
# author: Joseph Benkanoun
# prompt user for two cent amounts and print output as a euro value

# included an if function to account for anomolies when total was less than 10
# was familiar with Excel before taking the course so had an understanding of IF functions, Googled how they applied within Python
amount1 = int(input("Enter first amount (in c): "))
amount2 = int(input("Enter second amount (in c): "))
total = (amount1 + amount2)
eurovalue = total//100
if total < 10:
    print (f"The sum of these is €{eurovalue}.0{str(total)[-2:]}")
else:
    print (f"The sum of these is €{eurovalue}.{str(total)[-2:]}")

# this now seems to work as required whether value is €0.0x, €0.xx, €x.xx, or beyond
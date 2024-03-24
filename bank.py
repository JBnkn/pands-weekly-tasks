# bank.py
# author: Joseph Benkanoun
# prompt user for two cent amounts and print output as a euro value

# using a while loop to catch exceptions if non-numeric characters are entered
# want the user to be continually prompted until they enter a number
# reviewed at https://www.reddit.com/r/learnpython/comments/ln40vj/how_to_make_a_tryexcept_statement_loop_until_true/
def input_num(prompt):
    while True:
        response = input(prompt)
        try:
            response = int(response)
            return response
        except:
            print("That wasn't a valid entry. Please enter a whole number value only.")

# used existing input_num function to prompt for two values separately
def input_total():
    first_number = input_num("Enter first amount (in c): ")
    second_number = input_num("Enter second amount (in c): ")
    # returm total of two values
    return first_number + second_number

total = input_total()

# determine euro value by using integer division
eurovalue = total//100

# determine cent value by taking last two characters from total
# pair euro value and cent value in relative positions
# IF function accounts for total values under 10
# ELSE function accounts for all other values
if total < 10:
    print (f"The sum of these is €{eurovalue}.0{str(total)[-2:]}")
else:
    print (f"The sum of these is €{eurovalue}.{str(total)[-2:]}")

# this now seems to work as required whether value is €0.0x, €0.xx, €x.xx, or beyond
    
# was familiar with Excel before taking the course so had an understanding of IF functions, Googled how they applied within Python
# https://www.w3schools.com/python/python_conditions.asp
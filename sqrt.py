# sqrt.py
# author: Joseph Benkanoun
# take a positive floating-point number as input and output an approximation of its square root

# trying out a while loop to catch exceptions if non-numeric characters are entered
# want the user to be continually prompted until they enter a number
# reviewed at https://www.reddit.com/r/learnpython/comments/ln40vj/how_to_make_a_tryexcept_statement_loop_until_true/
def input_num():
    while True:
        response = input("Enter a number: ")
        try:
            response = float(response)
            return response
        except:
            print("That wasn't a number.")

# assign returned response to num
num = input_num()

# outline initial guess by dividing input by two
guess = num / 2

# set acceptable tolerance level to determine approximation of square root
gap = 0.001

# run WHILE function according to Newton method of square root approximation
# while the difference between the guess squared and the inital number is larger than accepted tolerance
while abs(guess * guess - num) > gap: 
    print(f"Current guess is {guess}. {guess} squared is {guess * guess}. Current gap is {abs(guess * guess - num)}.")
    # apply Newton method to iterate
    guess = (guess + num / guess) / 2 
    
# print result to console when WHILE condition is met
print(f"The square root of {num} is approximately {guess}.")
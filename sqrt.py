# sqrt.py
# author: Joseph Benkanoun
# take a positive floating-point number as input and output an approximation of its square root

# prompt a user input and clean it to ensure it's a positive floating-point
num = abs(float(input("Enter a number: ")))

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
# sqrt.py
# author: Joseph Benkanoun
# take a positive floating-point number as input and output an approximation of its square root

num = abs(float(input("Enter a number: ")))
sq = 1.1
test = sq*sq
gap = num - test

while gap > 0.1:
    print(f"Your number is {num}, {sq} squared is {test}: the gap is now {gap}")
    root = 0.5 * (sq + (num / sq))
    test = root * root
    gap = num - test
    sq += 0.1

print(f"The square root of {num} is {sq} with a tolerance of {gap}.")
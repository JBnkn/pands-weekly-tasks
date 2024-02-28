# weekday.py
# author: Joseph Benkanoun
# output whether or not today is a weekday

# found detail at https://pynative.com/python-get-the-day-of-week/ about datetime module
from datetime import datetime

# this assigns an index to day of the week; Monday=0 to Sunday=6
today = datetime.today()
x = today.weekday()

# anything from 0-4 will be a weekday
if x <=4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

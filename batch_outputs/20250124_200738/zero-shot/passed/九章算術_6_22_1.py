"""
今有一人一日矯矢五十，一人一日羽矢三十，一人一日筈矢十五。今令一人一日自矯、羽、筈，問︰成矢幾何？
術曰：矯矢五十，用徒一人。羽矢五十，用徒一人、太半人。筈矢五十，用徒三人、少半人。并之，得六人，以為法。以五十矢為實。實如法得一矢。
荅曰： a矢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Define the rates of work for each task
rate_k = Fraction(50, 1)  #矯矢 rate: 50矢/day
rate_y = Fraction(30, 1)  #羽矢 rate: 30矢/day
rate_h = Fraction(15, 1)  #筈矢 rate: 15矢/day

# Define the combined work rate for one person doing all tasks
combined_rate = Fraction(1, rate_k) + Fraction(1, rate_y) + Fraction(1, rate_h)

# Calculate the number of arrows completed in one day by one person
a = Fraction(1, combined_rate)

# Output the result
a  # The number of arrows completed in one day by one person
#----- content ends here -----


"""


The variable `a` will hold the solution, which represents the number of arrows completed in one day by one person.
"""


"""
"""

"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，犬價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of a dog (`b`) based on the given conditions. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given conditions
insufficient_amount = 90  # Not enough by 90
rate1 = 5  # Each person contributes 5
rate2 = 50  # Each person contributes 50

# Step 1: Calculate the number of people (a)
# Formula: (insufficient_amount + sufficient_amount) / (rate2 - rate1)
a = (insufficient_amount + 0) / (rate2 - rate1)

# Step 2: Calculate the price of a dog (b)
# Formula: rate2 * a
b = rate2 * a

# Convert to Fraction for exact representation
a = Fraction(a)
b = Fraction(b)

# Results
a, b
#----- content ends here -----


"""


This code calculates the number of people (`a`) and the price of a dog (`b`) using the given conditions. The results are stored in variables `a` and `b`.
"""


"""
"""

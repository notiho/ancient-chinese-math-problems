"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，犬價 b 。
"""

"""
This is a classic ancient Chinese math problem. Let's translate it into Python code to compute the values of the unknowns `a` (number of people) and `b` (price of a dog). We'll use the `Fraction` class to ensure accurate calculations.


"""

#----- content starts here -----

from fractions import Fraction

# Given data
insufficient_amount = 90  # Not enough by 90 when each person pays 5
sufficient_rate = 50  # Exactly enough when each person pays 50
insufficient_rate = 5  # Rate when insufficient

# Step 1: Calculate the number of people (a)
# Formula: a = (insufficient_amount + sufficient_rate - insufficient_rate) / (sufficient_rate - insufficient_rate)
a = (insufficient_amount + sufficient_rate - insufficient_rate) / (sufficient_rate - insufficient_rate)

# Step 2: Calculate the price of a dog (b)
# Formula: b = sufficient_rate * a
b = sufficient_rate * a

# Convert to Fraction for exact representation
a = Fraction(a)
b = Fraction(b)

# Results
a, b
#----- content ends here -----


"""


After running this code, the variables `a` and `b` will contain the number of people and the price of a dog, respectively, as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 3
Variable 'b' has wrong value. Expected: 100, Actual: 150"""

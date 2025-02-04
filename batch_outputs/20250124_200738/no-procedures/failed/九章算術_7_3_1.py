"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
荅曰： a家 ，牛價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people is buying a cow. 
- Seven families together contribute 190, which is 330 less than the required amount.
- Nine families together contribute 270, which is 30 more than the required amount.

Question: How many families are there (*a*) and what is the price of the cow (*b*)?

Answer: *a* families, and the price of the cow is *b*.
"""

# Let the number of families be `a` and the price of the cow be `b`.

# From the problem:
# 7 families contribute 190, which is 330 less than the price of the cow:
# 7 * (b / a) = 190 + 330
# 9 families contribute 270, which is 30 more than the price of the cow:
# 9 * (b / a) = 270 - 30

# Solve these equations step by step.

from fractions import Fraction

# Equation 1: 7 * (b / a) = 520
# Equation 2: 9 * (b / a) = 240

# Divide Equation 1 by Equation 2 to eliminate `b / a`:
# (7 / 9) = (520 / 240)
# Simplify:
ratio = Fraction(520, 240)  # Simplify the ratio
a = ratio.denominator  # Number of families
b = ratio.numerator * 240  # Price of the cow

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 6
Variable 'b' has wrong value. Expected: 3750, Actual: 3120"""

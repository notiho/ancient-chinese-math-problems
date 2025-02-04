"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Let's define the variables and compute the values of the unknowns `a` (number of people) and `b` (price of the chicken). We'll use the `Fraction` class to handle non-integer results.

The problem states:
- If each person contributes 9, there is an excess of 11.
- If each person contributes 6, there is a deficit of 16.

From this, we can derive the equations:
1. \( 9a - b = 11 \) (excess)
2. \( 6a - b = -16 \) (deficit)

We solve these equations to find `a` (number of people) and `b` (price of the chicken).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# 9a - b = 11
# 6a - b = -16

# Step 1: Subtract the second equation from the first to eliminate b
# (9a - b) - (6a - b) = 11 - (-16)
# 3a = 27
a = Fraction(27, 3)

# Step 2: Substitute a into the first equation to solve for b
# 9a - b = 11
b = 9 * a - 11

# Results
a, b
#----- content ends here -----


"""


The solution will compute the values of `a` (number of people) and `b` (price of the chicken).
"""


"""
"""

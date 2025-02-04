"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
荅曰：大器容 a斛 ，小器容 b斛 。
"""

#----- content starts here -----
"""
Suppose there are large vessels and small vessels. 
Five large vessels and one small vessel together hold 3 hu. 
One large vessel and five small vessels together hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

Answer: each large vessel holds *a* hu, and each small vessel holds *b* hu.
"""

# Using variables for the problem
from fractions import Fraction

# Let the capacity of a large vessel be `a` hu
# Let the capacity of a small vessel be `b` hu

# Equations:
# 5a + b = 3
# a + 5b = 2

# Solve for `a` and `b` using substitution or elimination
# From the first equation: b = 3 - 5a
# Substitute into the second equation:
# a + 5(3 - 5a) = 2
# a + 15 - 25a = 2
# -24a = -13
a = Fraction(13, 24)

# Substitute `a` back into b = 3 - 5a
b = 3 - 5 * a
b = Fraction(27, 24)

# Results
a  # Capacity of a large vessel in hu
b  # Capacity of a small vessel in hu#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 7/24, Actual: 9/8"""

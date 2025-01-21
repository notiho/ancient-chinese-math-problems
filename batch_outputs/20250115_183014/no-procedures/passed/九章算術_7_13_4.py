"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
Suppose there are large vessels and small vessels. 
Five large vessels and one small vessel together hold 3 hu. 
One large vessel and five small vessels together hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

Answer: each large vessel holds *a* hu, and each small vessel holds *b* hu.
"""

# Let the capacity of a large vessel be `a` hu and the capacity of a small vessel be `b` hu.
# From the problem, we have the following system of equations:
# 5a + b = 3
# a + 5b = 2

from fractions import Fraction

# Solve the system of equations
# Multiply the second equation by 5 to align coefficients of `a`
# 5a + b = 3
# 5a + 25b = 10

# Subtract the first equation from the modified second equation
# (5a + 25b) - (5a + b) = 10 - 3
# 24b = 7
b = Fraction(7, 24)

# Substitute `b` into the first equation to solve for `a`
# 5a + b = 3
# 5a + (7/24) = 3
# 5a = 3 - (7/24)
# 5a = (72/24) - (7/24)
# 5a = 65/24
a = Fraction(65, 120)

# Final answer
a, b  # a is the capacity of a large vessel, b is the capacity of a small vessel
"""
"""

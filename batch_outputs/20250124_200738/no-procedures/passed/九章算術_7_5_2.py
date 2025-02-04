"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
荅曰： a人 ，羊價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buy sheep. If each person contributes 5, they are short by 45. If each person contributes 7, they are short by 3.
Question: how many people are there, and what is the price of the sheep?

Answer: there are *a* people, and the price of the sheep is *b*.
"""

# Let the number of people be `a` and the price of the sheep be `b`.
# From the problem, we have the following equations:
# 1. 5 * a + 45 = b
# 2. 7 * a + 3 = b

# Solve for `a` and `b`.

from fractions import Fraction

# Equation 1: b = 5 * a + 45
# Equation 2: b = 7 * a + 3

# Set the two equations equal to each other:
# 5 * a + 45 = 7 * a + 3
# Simplify:
# 45 - 3 = 7 * a - 5 * a
# 42 = 2 * a
a = Fraction(42, 2)

# Substitute `a` into one of the equations to solve for `b`:
b = 5 * a + 45

# Final results:
a = int(a)  # Number of people
b = int(b)  # Price of the sheep

a, b  # Output the results#----- content ends here -----

"""
"""

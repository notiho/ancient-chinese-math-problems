"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
答曰： a 車， b人 。
"""

#----- content starts here -----
"""
Suppose there are three people sharing one cart, and two carts are empty. If two people share one cart, nine people are walking.
Question: how many carts and how many people are there?

Answer: there are *a* carts and *b* people.
"""

# Let the number of carts be `a` and the number of people be `b`.

# Equation 1: When 3 people share 1 cart, 2 carts are empty.
# Total people = 3 * (a - 2)

# Equation 2: When 2 people share 1 cart, 9 people are walking.
# Total people = 2 * a + 9

# Solve the system of equations:
# 3 * (a - 2) = 2 * a + 9

from fractions import Fraction

# Solve for `a` (number of carts)
a = Fraction(9 + 6, 3 - 2)

# Solve for `b` (number of people)
b = 3 * (a - 2)

a, b  # Output the number of carts and people#----- content ends here -----

"""
"""

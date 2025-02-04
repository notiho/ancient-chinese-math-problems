"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
答曰： a 車， b人 。
"""

#----- content starts here -----
"""
Suppose there are three people sharing a cart, and two carts are empty. If two people share a cart, nine people are walking.
Question: how many carts and people are there?

Answer: there are *a* carts and *b* people.
"""

# Let the number of carts be `a` and the number of people be `b`.

# Equation 1: When 3 people share a cart, 2 carts are empty.
# Total people = 3 * (total carts - 2)
# b = 3 * (a - 2)

# Equation 2: When 2 people share a cart, 9 people are walking.
# Total people = 2 * total carts + 9
# b = 2 * a + 9

# Solve the system of equations:
# From Equation 1: b = 3a - 6
# From Equation 2: b = 2a + 9
# Set the two equations for `b` equal:
# 3a - 6 = 2a + 9
# a = 15

# Substitute `a` into one of the equations for `b`:
# b = 3a - 6
# b = 3 * 15 - 6
# b = 45 - 6
# b = 39

# Final answer:
a = 15  # Number of carts
b = 39  # Number of people#----- content ends here -----

"""
"""

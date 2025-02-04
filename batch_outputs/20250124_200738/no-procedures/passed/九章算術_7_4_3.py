"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
荅曰： a人 。金價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buys gold. If each person contributes 400, there is a surplus of 3400. If each person contributes 300, there is a surplus of 100.
Question: how many people are there, and what is the price of the gold?

Answer: there are *a* people, and the price of the gold is *b*.
"""

# Let the number of people be `n` and the price of the gold be `p`.

# Equation 1: 400n - p = 3400
# Equation 2: 300n - p = 100

# Subtract the second equation from the first to eliminate `p`:
# (400n - p) - (300n - p) = 3400 - 100
# 100n = 3300
n = Fraction(3300, 100)

# Substitute `n` into the first equation to solve for `p`:
# 400n - p = 3400
p = 400 * n - 3400

# Final results
a = n  # Number of people
b = p  # Price of the gold#----- content ends here -----

"""
"""

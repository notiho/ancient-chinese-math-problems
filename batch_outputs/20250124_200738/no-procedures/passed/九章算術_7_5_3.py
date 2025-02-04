"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
荅曰： a人 ，羊價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buys sheep. If each person contributes 5, they are short by 45. If each person contributes 7, they are short by 3.
Question: how many people are there, and what is the price of the sheep?

Answer: there are *a* people, and the price of the sheep is *b*.
"""

# Let the number of people be `a` and the price of the sheep be `b`.
# From the problem, we have two equations:
# 1. 5 * a + 45 = b
# 2. 7 * a + 3 = b

# Solve for `a` and `b` using substitution:
# From equation (1): b = 5 * a + 45
# Substitute into equation (2): 7 * a + 3 = 5 * a + 45

# Simplify:
# 7 * a + 3 = 5 * a + 45
# 2 * a = 42
# a = 21

# Substitute `a` into equation (1) to find `b`:
# b = 5 * a + 45
# b = 5 * 21 + 45
# b = 105 + 45
# b = 150

# Final results:
a = 21  # Number of people
b = 150  # Price of the sheep#----- content ends here -----

"""
"""

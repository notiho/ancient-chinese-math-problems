"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
荅曰： a人 ，羊價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys sheep. If each person contributes 5 units of money, they are short by 45 units. 
If each person contributes 7 units of money, they are short by 3 units. 

Question: how many people are there (*a*), and what is the price of the sheep (*b*)?

Answer: *a* people, and the price of the sheep is *b*.
"""

# Let the number of people be `a` and the price of the sheep be `b`.
# From the problem, we have two equations:
# 1. 5a + 45 = b
# 2. 7a + 3 = b

# Solve for `a` and `b`:
# From the first equation: b = 5a + 45
# Substitute into the second equation: 7a + 3 = 5a + 45
# Simplify: 2a = 42
a = 42 // 2  # Number of people

# Substitute `a` back into the first equation to find `b`:
b = 5 * a + 45  # Price of the sheep

# Final results:
a, b  # a = number of people, b = price of the sheep#----- content ends here -----

"""
"""

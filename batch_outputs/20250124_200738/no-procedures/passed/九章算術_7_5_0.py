"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
荅曰： a人 ，羊價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buys sheep. If each person contributes 5 units of money, they are short by 45 units. 
If each person contributes 7 units of money, they are short by 3 units. 

Question: How many people are there (*a*), and what is the price of the sheep (*b*)?

Answer: *a* people, and the price of the sheep is *b*.
"""

# Let the number of people be `a` and the price of the sheep be `b`.
# From the problem, we have the following equations:
# 5a + 45 = b  (1)
# 7a + 3 = b   (2)

# Subtract equation (1) from equation (2) to eliminate `b`:
# (7a + 3) - (5a + 45) = 0
# 2a - 42 = 0
# a = 21

# Substitute `a = 21` into equation (1) to solve for `b`:
# 5a + 45 = b
# b = 5(21) + 45
# b = 105 + 45
# b = 150

# Final results:
a = 21  # Number of people
b = 150  # Price of the sheep

# Output:
a, b  # (21, 150)#----- content ends here -----

"""
"""

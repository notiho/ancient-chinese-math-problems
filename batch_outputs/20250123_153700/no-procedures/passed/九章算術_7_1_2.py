"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
荅曰： a人 ，雞價 b 。
"""

"""
Suppose a group of people buys chickens. If each person contributes 9 coins, there is an excess of 11 coins. 
If each person contributes 6 coins, there is a shortage of 16 coins.
Question: How many people are there, and what is the price of the chicken?

Answer: There are *a* people, and the price of the chicken is *b* coins.
"""

# Let the number of people be x and the price of the chicken be y.

# Equation 1: 9x = y + 11
# Equation 2: 6x = y - 16

# Solving for x and y:
# From Equation 1, y = 9x - 11
# Substitute y into Equation 2: 6x = (9x - 11) - 16
# Simplify: 6x = 9x - 27
# 3x = 27
# x = 9

# Substitute x = 9 into Equation 1: y = 9(9) - 11
# y = 81 - 11
# y = 70

# Final results:
a = 9  # Number of people
b = 70  # Price of the chicken
"""
"""

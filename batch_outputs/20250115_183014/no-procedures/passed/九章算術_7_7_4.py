"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
荅曰： a人 ，犬價 b 。
"""

"""
Suppose a group of people wants to buy a dog. If each person contributes 5 units of money, they are 90 units short. If each person contributes 50 units of money, the amount is exactly enough.
Question: how many people are there, and what is the price of the dog?

Answer: there are *a* people, and the price of the dog is *b*.
"""

# Let the number of people be `a` and the price of the dog be `b`.
# From the problem, we have two equations:
# 1. 5 * a + 90 = b
# 2. 50 * a = b

# Solve the equations:
# From equation (2): b = 50 * a
# Substitute b into equation (1): 5 * a + 90 = 50 * a

# Simplify:
# 90 = 50 * a - 5 * a
# 90 = 45 * a
# a = 90 / 45

a = 90 // 45  # Number of people

# Substitute a into equation (2) to find b:
b = 50 * a  # Price of the dog

# Final results:
a, b  # a = number of people, b = price of the dog
"""
"""

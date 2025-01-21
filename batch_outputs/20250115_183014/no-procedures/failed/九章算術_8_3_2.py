"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾). The problem gives the following relationships:

1. Five bundles (秉) of upper grain lose 1 dou and 1 sheng (i.e., 11 sheng) when converted to lower grain, which is equivalent to seven bundles of lower grain.
2. Seven bundles of upper grain lose 2 dou and 5 sheng (i.e., 25 sheng) when converted to lower grain, which is equivalent to five bundles of lower grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain contain, respectively?

Answer: One bundle of upper grain contains *a* dou and *b* sheng, and one bundle of lower grain contains *c* dou and *d* sheng.
"""

from fractions import Fraction

# Convert dou and sheng to a single unit (sheng)
# 1 dou = 10 sheng
loss_1 = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
loss_2 = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Let x = amount of grain in one bundle of upper grain (in sheng)
# Let y = amount of grain in one bundle of lower grain (in sheng)

# Equation 1: 5x - 11 = 7y
# Equation 2: 7x - 25 = 5y

# Solve for x and y
# From Equation 1: 5x - 11 = 7y => y = (5x - 11) / 7
# Substitute y into Equation 2: 7x - 25 = 5y
# 7x - 25 = 5((5x - 11) / 7)
# Multiply through by 7 to eliminate the denominator:
# 49x - 175 = 25x - 55
# Simplify:
# 49x - 25x = 175 - 55
# 24x = 120
# x = 120 / 24 = 5

# Substitute x = 5 into Equation 1 to solve for y:
# 5x - 11 = 7y
# 5(5) - 11 = 7y
# 25 - 11 = 7y
# 14 = 7y
# y = 14 / 7 = 2

# Convert x and y back to dou and sheng
a = 5 // 10  # Upper grain: dou part
b = 5 % 10   # Upper grain: sheng part

c = 2 // 10  # Lower grain: dou part
d = 2 % 10   # Lower grain: sheng part

# Final result
a, b, c, d  # (a dou b sheng for upper grain, c dou d sheng for lower grain)
"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""

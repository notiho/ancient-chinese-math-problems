"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
Suppose there are two types of grain, "upper grain" (上禾) and "lower grain" (下禾). The problem states:

1. Five bundles (秉) of upper grain lose 1 dou and 1 sheng (1斗1升) of grain when converted to lower grain, which is equivalent to seven bundles of lower grain.
2. Seven bundles of upper grain lose 2 dou and 5 sheng (2斗5升) of grain when converted to five bundles of lower grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain contain?

Answer: One bundle of upper grain contains *a* dou and *b* sheng, and one bundle of lower grain contains *c* dou and *d* sheng.
"""

from fractions import Fraction

# Convert dou and sheng to a single unit (1 dou = 10 sheng)
loss_1 = 1 * 10 + 1  # 1斗1升 = 11升
loss_2 = 2 * 10 + 5  # 2斗5升 = 25升

# Let x = grain in one bundle of upper grain (in sheng)
# Let y = grain in one bundle of lower grain (in sheng)

# Equation 1: 5x - 11 = 7y
# Equation 2: 7x - 25 = 5y

# Solve the system of equations
# From Equation 1: y = (5x - 11) / 7
# Substitute into Equation 2:
# 7x - 25 = 5((5x - 11) / 7)
# Multiply through by 7 to eliminate the denominator:
# 49x - 175 = 25x - 55
# Simplify:
# 49x - 25x = 175 - 55
# 24x = 120
x = Fraction(120, 24)  # x = 5 (in sheng)

# Substitute x = 5 into Equation 1 to solve for y:
# 5x - 11 = 7y
# 5(5) - 11 = 7y
# 25 - 11 = 7y
# 14 = 7y
y = Fraction(14, 7)  # y = 2 (in sheng)

# Convert x and y back to dou and sheng
a = x // 10  # a = number of dou in x
b = x % 10   # b = remaining sheng in x

c = y // 10  # c = number of dou in y
d = y % 10   # d = remaining sheng in y

# Final results
a, b, c, d  # a = 0 dou, b = 5 sheng; c = 0 dou, d = 2 sheng
"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""

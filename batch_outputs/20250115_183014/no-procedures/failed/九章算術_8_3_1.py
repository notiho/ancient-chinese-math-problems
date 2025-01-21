"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾). 
The problem provides the following relationships:

1. 5 bundles (秉) of upper grain lose 1 dou and 1 sheng (i.e., 11 sheng) when converted to 7 bundles of lower grain.
2. 7 bundles of upper grain lose 2 dou and 5 sheng (i.e., 25 sheng) when converted to 5 bundles of lower grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain contain?

Answer: Each bundle of upper grain contains *a* dou and *b* sheng, and each bundle of lower grain contains *c* dou and *d* sheng.
"""

from fractions import Fraction

# Conversion of dou and sheng to total sheng
# 1 dou = 10 sheng
損實_1 = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
損實_2 = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Equations based on the problem:
# Let x = amount of grain in one bundle of upper grain (in sheng)
# Let y = amount of grain in one bundle of lower grain (in sheng)
# Equation 1: 5x - 7y = 11
# Equation 2: 7x - 5y = 25

# Solve the system of equations
# Multiply the first equation by 7 and the second equation by 5 to eliminate y
# 35x - 49y = 77
# 35x - 25y = 125
# Subtract the first equation from the second
# 24y = 48
y = Fraction(48, 24)  # y = 2 sheng (amount of grain in one bundle of lower grain)

# Substitute y into the first equation to solve for x
# 5x - 7(2) = 11
# 5x - 14 = 11
# 5x = 25
x = Fraction(25, 5)  # x = 5 sheng (amount of grain in one bundle of upper grain)

# Convert x and y into dou and sheng
a = x // 10  # a = number of dou in upper grain
b = x % 10   # b = number of sheng in upper grain
c = y // 10  # c = number of dou in lower grain
d = y % 10   # d = number of sheng in lower grain

# Final result
a, b, c, d  # Upper grain: a dou b sheng, Lower grain: c dou d sheng
"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 0"""

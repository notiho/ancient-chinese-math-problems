"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

#----- content starts here -----
"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾).

1. Six bundles (秉) of upper grain lose 1 dou and 8 sheng (1斗8升) of grain, which is equivalent to 10 bundles of lower grain.
2. Fifteen bundles of lower grain lose 5 sheng (5升) of grain, which is equivalent to 5 bundles of upper grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain yield?

Answer: One bundle of upper grain yields *a* sheng, and one bundle of lower grain yields *b* sheng.
"""

from fractions import Fraction

# Given data
upper_grain_loss = 1 * 10 + 8  # 1斗8升 = 10升 + 8升 = 18升
lower_grain_loss = 5  # 5升

# Relationships
# 6 bundles of upper grain = 10 bundles of lower grain
# 15 bundles of lower grain = 5 bundles of upper grain

# Let:
# x = grain per bundle of upper grain (in 升)
# y = grain per bundle of lower grain (in 升)

# From the first relationship:
# 6x = 10y + 18  (Equation 1)

# From the second relationship:
# 15y = 5x + 5  (Equation 2)

# Solve the system of equations
# From Equation 1: x = (10y + 18) / 6
# Substitute x into Equation 2:
# 15y = 5((10y + 18) / 6) + 5
# Multiply through by 6 to eliminate the fraction:
# 90y = 50y + 90 + 30
# 90y - 50y = 120
# 40y = 120
# y = 3

# Substitute y = 3 into Equation 1:
# 6x = 10(3) + 18
# 6x = 30 + 18
# 6x = 48
# x = 8

# Final results
a = Fraction(8)  # Upper grain per bundle (in 升)
b = Fraction(3)  # Lower grain per bundle (in 升)

a, b  # Output the results#----- content ends here -----

"""
"""

"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
Suppose there are two types of grain, "upper grain" (上禾) and "lower grain" (下禾). 
The relationships between their yields are as follows:

- 6 bundles (秉) of upper grain lose 1 dou and 8 sheng (1斗8升) of yield, which is equivalent to 10 bundles of lower grain.
- 15 bundles of lower grain lose 5 sheng (5升) of yield, which is equivalent to 5 bundles of upper grain.

Question: How much yield does 1 bundle of upper grain and 1 bundle of lower grain produce?

Answer: 1 bundle of upper grain produces *b* sheng, and 1 bundle of lower grain produces *d* sheng.
"""

from fractions import Fraction

# Define the known relationships
# 6 bundles of upper grain lose 1 dou 8 sheng, equivalent to 10 bundles of lower grain
upper_to_lower_ratio = Fraction(6, 10)  # Ratio of upper grain bundles to lower grain bundles
upper_loss = 1 * 10 + 8  # Convert 1 dou 8 sheng to sheng (1 dou = 10 sheng)

# 15 bundles of lower grain lose 5 sheng, equivalent to 5 bundles of upper grain
lower_to_upper_ratio = Fraction(15, 5)  # Ratio of lower grain bundles to upper grain bundles
lower_loss = 5  # Loss in sheng for lower grain

# Let the yield of 1 bundle of upper grain be `b` sheng
# Let the yield of 1 bundle of lower grain be `d` sheng

# From the first relationship:
# 6 bundles of upper grain lose 1 dou 8 sheng, equivalent to 10 bundles of lower grain
# 6 * b - upper_loss = 10 * d
# 6 * b - 18 = 10 * d  (Equation 1)

# From the second relationship:
# 15 bundles of lower grain lose 5 sheng, equivalent to 5 bundles of upper grain
# 15 * d - lower_loss = 5 * b
# 15 * d - 5 = 5 * b  (Equation 2)

# Solve the system of equations
# From Equation 1: 6 * b - 18 = 10 * d
# Rearrange: b = (10 * d + 18) / 6

# Substitute b into Equation 2:
# 15 * d - 5 = 5 * ((10 * d + 18) / 6)
# Multiply through by 6 to eliminate the fraction:
# 90 * d - 30 = 50 * d + 90
# Simplify:
# 40 * d = 120
# d = 3

# Substitute d = 3 into b = (10 * d + 18) / 6:
b = (10 * 3 + 18) / 6
b = 8

# Final results:
a = 1  # 1 bundle of upper grain
c = 1  # 1 bundle of lower grain
d = 3  # Yield of 1 bundle of lower grain in sheng
b = 8  # Yield of 1 bundle of upper grain in sheng

# Output the results
a, b, c, d  # 上禾 1秉 實 8升, 下禾 1秉 實 3升
"""
"""

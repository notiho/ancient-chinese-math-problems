"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾).

1. Six bundles (秉) of upper grain lose 1 dou and 8 sheng (1斗8升) of grain, which is equivalent to 10 bundles of lower grain.
2. Fifteen bundles of lower grain lose 5 sheng (5升) of grain, which is equivalent to 5 bundles of upper grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain yield?

Answer: One bundle of upper grain yields *b* sheng, and one bundle of lower grain yields *d* sheng.
"""

from fractions import Fraction

# Define the known values
上禾_損實 = 1 * 10 + 8  # 1斗8升 = 10升 + 8升 = 18升
上禾_秉數 = 6
下禾_秉數_對應上禾 = 10

下禾_損實 = 5  # 5升
下禾_秉數 = 15
上禾_秉數_對應下禾 = 5

# Calculate the grain yield per bundle for each type
# Let x = yield per bundle of upper grain (in 升)
# Let y = yield per bundle of lower grain (in 升)

# Equation 1: 6x = 10y + 18
# Equation 2: 15y = 5x + 5

# Solve for x and y
# From Equation 1: x = (10y + 18) / 6
# Substitute x into Equation 2: 15y = 5((10y + 18) / 6) + 5

# Simplify Equation 2:
# 15y = (50y + 90) / 6 + 5
# Multiply through by 6 to eliminate the fraction:
# 90y = 50y + 90 + 30
# 90y - 50y = 120
# 40y = 120
y = Fraction(120, 40)  # y = 3 (升 per bundle of lower grain)

# Substitute y back into Equation 1 to solve for x:
x = Fraction(10 * y + 18, 6)
x = Fraction(10 * 3 + 18, 6)
x = Fraction(48, 6)  # x = 8 (升 per bundle of upper grain)

# Final results
a = 1  # One bundle of upper grain
b = x  # Grain yield per bundle of upper grain (8升)

c = 1  # One bundle of lower grain
d = y  # Grain yield per bundle of lower grain (3升)

# Results
a, b, c, d  # (1秉, 8升, 1秉, 3升)
"""
"""

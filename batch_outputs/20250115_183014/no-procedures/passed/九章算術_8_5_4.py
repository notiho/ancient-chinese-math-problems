"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
Suppose there are two types of grain, "upper grain" (上禾) and "lower grain" (下禾). 
- 3 bundles (秉) of upper grain plus 6 dou of grain is equivalent to 10 bundles of lower grain.
- 5 bundles of lower grain plus 1 dou of grain is equivalent to 2 bundles of upper grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain yield?

Answer: One bundle of upper grain yields *b* dou, and one bundle of lower grain yields *d* dou.
"""

from fractions import Fraction

# Let x = the amount of grain (in dou) per bundle of upper grain
# Let y = the amount of grain (in dou) per bundle of lower grain

# Equation 1: 3x + 6 = 10y
# Equation 2: 5y + 1 = 2x

# Solve for x and y
# From Equation 1: 3x + 6 = 10y -> x = (10y - 6) / 3
# Substitute x into Equation 2: 5y + 1 = 2((10y - 6) / 3)
# Simplify:
# 5y + 1 = (20y - 12) / 3
# Multiply through by 3 to eliminate the fraction:
# 15y + 3 = 20y - 12
# Simplify:
# 3 + 12 = 20y - 15y
# 15 = 5y
# y = 3

# Substitute y = 3 into Equation 1 to solve for x:
# 3x + 6 = 10(3)
# 3x + 6 = 30
# 3x = 24
# x = 8

# Results
a = 1  # One bundle of upper grain
b = Fraction(8)  # Grain per bundle of upper grain in dou
c = 1  # One bundle of lower grain
d = Fraction(3)  # Grain per bundle of lower grain in dou

# Final answer:
# 上禾 1秉 實 8斗
# 下禾 1秉 實 3斗
"""
"""

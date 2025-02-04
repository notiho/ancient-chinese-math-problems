"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾).

- 3 bundles of upper grain plus 6 dou of grain are equivalent to 10 bundles of lower grain.
- 5 bundles of lower grain plus 1 dou of grain are equivalent to 2 bundles of upper grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain yield?

Answer: One bundle of upper grain yields *a* dou, and one bundle of lower grain yields *b* dou.
"""

from fractions import Fraction

# Let x = the yield of one bundle of upper grain (in dou)
# Let y = the yield of one bundle of lower grain (in dou)

# Equation 1: 3x + 6 = 10y
# Equation 2: 5y + 1 = 2x

# Solve for x and y using substitution
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

# Final result
a = Fraction(8)  # Yield of one bundle of upper grain
b = Fraction(3)  # Yield of one bundle of lower grain

a, b  # Output the results
"""
"""

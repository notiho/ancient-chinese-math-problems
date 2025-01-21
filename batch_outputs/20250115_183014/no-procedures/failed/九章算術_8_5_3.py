"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
Suppose there are two types of grain: upper grain (上禾) and lower grain (下禾).
- 3 bundles of upper grain plus 6 dou of grain are equivalent to 10 bundles of lower grain.
- 5 bundles of lower grain plus 1 dou of grain are equivalent to 2 bundles of upper grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain yield?

Answer: One bundle of upper grain yields *a* dou, and one bundle of lower grain yields *b* dou.
"""

from fractions import Fraction

# Let x = the amount of grain (in dou) from one bundle of upper grain
# Let y = the amount of grain (in dou) from one bundle of lower grain

# Equation 1: 3x + 6 = 10y
# Equation 2: 5y + 1 = 2x

# Solve for x and y using substitution
# From Equation 1: 3x + 6 = 10y -> x = (10y - 6) / 3
# Substitute x into Equation 2: 5y + 1 = 2x
# 5y + 1 = 2 * ((10y - 6) / 3)
# 5y + 1 = (20y - 12) / 3
# Multiply through by 3 to eliminate fractions:
# 15y + 3 = 20y - 12
# Simplify:
# 3 + 12 = 20y - 15y
# 15 = 5y
# y = 3

# Substitute y = 3 into x = (10y - 6) / 3:
# x = (10 * 3 - 6) / 3
# x = (30 - 6) / 3
# x = 24 / 3
# x = 8

# Results
a = Fraction(8)  # Upper grain yields 8 dou per bundle
b = Fraction(3)  # Lower grain yields 3 dou per bundle

# Final output
a, b
"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'b' has wrong value. Expected: 8, Actual: 3
Missing variable in output: 'c'
Missing variable in output: 'd'"""

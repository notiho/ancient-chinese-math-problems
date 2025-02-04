"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾).

- 3 bundles (秉) of upper grain, when 6 dou are added, are equivalent to 10 bundles of lower grain.
- 5 bundles of lower grain, when 1 dou is added, are equivalent to 2 bundles of upper grain.

Question: How much grain (in dou) does one bundle of upper grain and one bundle of lower grain yield?

Answer: One bundle of upper grain yields *a* dou, and one bundle of lower grain yields *b* dou.
"""

from fractions import Fraction

# Let the yield of one bundle of upper grain be `a` dou
# Let the yield of one bundle of lower grain be `b` dou

# Equation 1: 3a + 6 = 10b
# Equation 2: 5b + 1 = 2a

# Solve for `a` and `b` using substitution or elimination

# From Equation 1: 3a + 6 = 10b => a = (10b - 6) / 3
# Substitute into Equation 2: 5b + 1 = 2((10b - 6) / 3)
# Simplify:
# 5b + 1 = (20b - 12) / 3
# Multiply through by 3:
# 15b + 3 = 20b - 12
# Simplify:
# 5b = 15
# b = 3

# Substitute b = 3 into Equation 1 to solve for a:
# 3a + 6 = 10(3)
# 3a + 6 = 30
# 3a = 24
# a = 8

# Final results:
a = Fraction(8)  # Upper grain yield per bundle
b = Fraction(3)  # Lower grain yield per bundle

# Output:
a, b  # a = 8 dou, b = 3 dou
"""
"""

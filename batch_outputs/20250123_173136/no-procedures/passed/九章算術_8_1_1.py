"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
Suppose there are two types of grain: upper grain (上禾) and lower grain (下禾).

- Seven bundles of upper grain lose 1 dou of grain, but when 2 bundles of lower grain are added, the total becomes 10 dou.
- Eight bundles of lower grain gain 1 dou of grain, but when 2 bundles of upper grain are added, the total becomes 10 dou.

Question: How much grain does one bundle of upper grain (上禾) and one bundle of lower grain (下禾) yield?

Answer: One bundle of upper grain yields *a* dou, and one bundle of lower grain yields *b* dou.
"""

from fractions import Fraction

# Let x = amount of grain in one bundle of upper grain (上禾)
# Let y = amount of grain in one bundle of lower grain (下禾)

# Equation 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11

# Equation 2: 8y + 1 + 2x = 10
# Simplify: 2x + 8y = 9

# Solve the system of equations:
# From Equation 1: 7x + 2y = 11
# From Equation 2: 2x + 8y = 9

# Multiply Equation 1 by 4 to eliminate y:
# 28x + 8y = 44
# Subtract Equation 2:
# (28x + 8y) - (2x + 8y) = 44 - 9
# 26x = 35
x = Fraction(35, 26)

# Substitute x into Equation 1 to solve for y:
# 7x + 2y = 11
# 7(Fraction(35, 26)) + 2y = 11
# Fraction(245, 26) + 2y = 11
# 2y = 11 - Fraction(245, 26)
# 2y = Fraction(286, 26) - Fraction(245, 26)
# 2y = Fraction(41, 26)
y = Fraction(41, 52)

# Final results:
a = x  # Grain in one bundle of upper grain
b = y  # Grain in one bundle of lower grain

a, b  # Output the results
"""
"""

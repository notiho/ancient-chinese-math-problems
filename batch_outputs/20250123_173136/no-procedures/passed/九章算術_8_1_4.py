"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
Suppose there are 7 bundles of upper-grade grain, which lose 1 dou of grain, but when 2 bundles of lower-grade grain are added, the total becomes 10 dou.  
Similarly, 8 bundles of lower-grade grain, when 1 dou is added and 2 bundles of upper-grade grain are added, also total 10 dou.  

Question: How much grain does one bundle of upper-grade grain and one bundle of lower-grade grain yield, respectively?

Answer: One bundle of upper-grade grain yields *a* dou, and one bundle of lower-grade grain yields *b* dou.
"""

from fractions import Fraction

# Let x = yield of one bundle of upper-grade grain (in dou)
# Let y = yield of one bundle of lower-grade grain (in dou)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Simplify the equations:
# 7x + 2y = 11  (from Equation 1)
# 2x + 8y = 9   (from Equation 2)

# Solve the system of equations:
# Multiply Equation 1 by 4 to align coefficients of y:
# 28x + 8y = 44
# Subtract Equation 2 from the scaled Equation 1:
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
a = x  # Yield of one bundle of upper-grade grain
b = y  # Yield of one bundle of lower-grade grain

a, b  # Outputs the results
"""
"""

"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: upper grain (2 bundles), middle grain (3 bundles), and lower grain (4 bundles). None of the bundles are full dou.
If one bundle of the upper grain is taken from the middle grain, one bundle of the middle grain is taken from the lower grain, and one bundle of the lower grain is taken from the upper grain, then each becomes exactly 1 dou.

Question: How much dou does one bundle of upper grain, middle grain, and lower grain contain respectively?

Answer: One bundle of upper grain contains *a* dou, one bundle of middle grain contains *b* dou, and one bundle of lower grain contains *c* dou.
"""

from fractions import Fraction

# Let the amount of dou in one bundle of upper, middle, and lower grain be `a`, `b`, and `c` respectively.
# From the problem:
# 1. Upper grain: 2a + b = 1
# 2. Middle grain: 3b + c = 1
# 3. Lower grain: 4c + a = 1

# Solve the system of equations step by step:

# From equation 1: b = 1 - 2a
# Substitute b into equation 2: 3(1 - 2a) + c = 1
# Simplify: 3 - 6a + c = 1
# c = 6a - 2

# Substitute c into equation 3: 4(6a - 2) + a = 1
# Simplify: 24a - 8 + a = 1
# 25a = 9
a = Fraction(9, 25)

# Substitute a back into b = 1 - 2a:
b = 1 - 2 * a
b = Fraction(7, 25)

# Substitute a into c = 6a - 2:
c = 6 * a - 2
c = Fraction(8, 25)

# Final results:
a斗 = a  # Upper grain
b斗 = b  # Middle grain
c斗 = c  # Lower grain

# Output results
a斗, b斗, c斗#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 4/25, Actual: 8/25"""

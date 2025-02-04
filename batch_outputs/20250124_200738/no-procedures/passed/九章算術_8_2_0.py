"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: upper grain (shang he), middle grain (zhong he), and lower grain (xia he).
Initially, there are 2 bundles of upper grain, 3 bundles of middle grain, and 4 bundles of lower grain, but none of them are full dou.

If 1 bundle of middle grain is taken from the upper grain, 1 bundle of lower grain is taken from the middle grain, and 1 bundle of upper grain is taken from the lower grain, then each becomes exactly 1 dou.

Question: How much grain does each bundle of upper, middle, and lower grain contain?

Answer: Each bundle of upper grain contains *a* dou, each bundle of middle grain contains *b* dou, and each bundle of lower grain contains *c* dou.
"""

# Let the amount of grain in each bundle of upper, middle, and lower grain be a, b, and c respectively
from fractions import Fraction

# Equations based on the problem:
# 2a + b = 1 (upper grain becomes full dou after taking 1 bundle of middle grain)
# 3b + c = 1 (middle grain becomes full dou after taking 1 bundle of lower grain)
# 4c + a = 1 (lower grain becomes full dou after taking 1 bundle of upper grain)

# Solve the system of equations:
# From the first equation: b = 1 - 2a
# Substitute b into the second equation: 3(1 - 2a) + c = 1
# Simplify: 3 - 6a + c = 1 -> c = 6a - 2
# Substitute c into the third equation: 4(6a - 2) + a = 1
# Simplify: 24a - 8 + a = 1 -> 25a = 9 -> a = 9/25

a = Fraction(9, 25)  # Upper grain per bundle
b = 1 - 2 * a        # Middle grain per bundle
c = 6 * a - 2        # Lower grain per bundle

# Final results:
a, b, c  # a = 9/25 dou, b = 7/25 dou, c = 8/25 dou#----- content ends here -----

"""
"""

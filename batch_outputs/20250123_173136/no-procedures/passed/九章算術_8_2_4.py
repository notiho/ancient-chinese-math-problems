"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe). 
Initially, there are 2 bundles of upper grain, 3 bundles of middle grain, and 4 bundles of lower grain, but none of them are full dou (斗). 
If one bundle of middle grain is added to the upper grain, one bundle of lower grain is added to the middle grain, and one bundle of upper grain is added to the lower grain, then each becomes exactly 1 dou.

Question: How much does one bundle of upper grain, middle grain, and lower grain weigh, respectively?

Answer: One bundle of upper grain weighs *a* dou, one bundle of middle grain weighs *b* dou, and one bundle of lower grain weighs *c* dou.
"""

from fractions import Fraction

# Let the weight of one bundle of upper grain, middle grain, and lower grain be `a`, `b`, and `c` respectively.
# The problem gives us the following equations:
# 2a + b = 1  (upper grain becomes full when 1 bundle of middle grain is added)
# 3b + c = 1  (middle grain becomes full when 1 bundle of lower grain is added)
# 4c + a = 1  (lower grain becomes full when 1 bundle of upper grain is added)

# Solve the system of equations step by step:

# From the first equation: b = 1 - 2a
# Substitute b = 1 - 2a into the second equation: 3(1 - 2a) + c = 1
# Simplify: 3 - 6a + c = 1
# c = 6a - 2

# Substitute c = 6a - 2 into the third equation: 4(6a - 2) + a = 1
# Simplify: 24a - 8 + a = 1
# 25a = 9
# a = 9 / 25

# Substitute a = 9 / 25 into b = 1 - 2a:
# b = 1 - 2(9 / 25)
# b = 1 - 18 / 25
# b = 7 / 25

# Substitute a = 9 / 25 into c = 6a - 2:
# c = 6(9 / 25) - 2
# c = 54 / 25 - 50 / 25
# c = 4 / 25

# Final results:
a = Fraction(9, 25)  # Upper grain, one bundle
b = Fraction(7, 25)  # Middle grain, one bundle
c = Fraction(4, 25)  # Lower grain, one bundle

# Output the results
a, b, c  # a斗, b斗, c斗
"""
"""

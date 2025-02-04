"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe). 
Initially, there are 2 bundles of upper grain, 3 bundles of middle grain, and 4 bundles of lower grain, but none of them are full dou. 
When 1 bundle is taken from the middle grain and added to the upper grain, 1 bundle is taken from the lower grain and added to the middle grain, 
and 1 bundle is taken from the upper grain and added to the lower grain, each becomes exactly 1 dou.

Question: How much does 1 bundle of upper, middle, and lower grain weigh respectively?

Answer: 1 bundle of upper grain weighs *a* dou, 1 bundle of middle grain weighs *b* dou, and 1 bundle of lower grain weighs *c* dou.
"""

from fractions import Fraction

# Let the weight of 1 bundle of upper grain, middle grain, and lower grain be a, b, and c respectively
# Given equations based on the problem:
# 2a + b = 1  (upper grain becomes full dou after adding 1 middle grain bundle)
# 3b + c = 1  (middle grain becomes full dou after adding 1 lower grain bundle)
# 4c + a = 1  (lower grain becomes full dou after adding 1 upper grain bundle)

# Solve the system of equations step by step
# From the first equation: b = 1 - 2a
# Substitute b into the second equation: 3(1 - 2a) + c = 1
# Simplify: 3 - 6a + c = 1
# c = 6a - 2
# Substitute a and c into the third equation: 4(6a - 2) + a = 1
# Simplify: 24a - 8 + a = 1
# 25a = 9
# a = 9 / 25

# Substitute a back to find b and c
a = Fraction(9, 25)
b = 1 - 2 * a
c = 6 * a - 2

# Results
a, b, c  # a = upper grain, b = middle grain, c = lower grain#----- content ends here -----

"""
"""

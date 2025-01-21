"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b斗 ，中禾 c秉 實 d斗 ，下禾 e秉 實 f斗 。
"""

"""
Suppose there are three types of grain: upper grain (shanghe), middle grain (zhonghe), and lower grain (xiahe). 
Initially, there are 2 bundles of upper grain, 3 bundles of middle grain, and 4 bundles of lower grain, but none of them are full dou. 
If one bundle of middle grain is added to the upper grain, one bundle of lower grain is added to the middle grain, 
and one bundle of upper grain is added to the lower grain, then each becomes exactly 1 dou.

Question: How much grain does one bundle of upper, middle, and lower grain contain?

Answer: One bundle of upper grain contains *a* bundles and *b* dou, 
one bundle of middle grain contains *c* bundles and *d* dou, 
and one bundle of lower grain contains *e* bundles and *f* dou.
"""

from fractions import Fraction

# Let the amount of grain in one bundle of upper, middle, and lower grain be x, y, and z respectively (in dou).
# The problem gives us the following equations:
# 2x + y = 1  (upper grain becomes full when 1 bundle of middle grain is added)
# 3y + z = 1  (middle grain becomes full when 1 bundle of lower grain is added)
# 4z + x = 1  (lower grain becomes full when 1 bundle of upper grain is added)

# Solve the equations step by step:

# From the first equation: y = 1 - 2x
# Substitute y into the second equation: 3(1 - 2x) + z = 1
# Simplify: 3 - 6x + z = 1
# z = 6x - 2

# Substitute x and z into the third equation: 4(6x - 2) + x = 1
# Simplify: 24x - 8 + x = 1
# 25x = 9
# x = 9 / 25

# Now substitute x back to find y and z:
x = Fraction(9, 25)
y = 1 - 2 * x
z = 6 * x - 2

# Simplify y and z:
y = Fraction(7, 25)
z = Fraction(8, 25)

# The results:
a, b = 1, x  # Upper grain: 1 bundle contains x dou
c, d = 1, y  # Middle grain: 1 bundle contains y dou
e, f = 1, z  # Lower grain: 1 bundle contains z dou

# Final values:
a, b, c, d, e, f
"""
Variable 'f' has wrong value. Expected: 4/25, Actual: 8/25"""

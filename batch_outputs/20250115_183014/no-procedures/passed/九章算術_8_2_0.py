"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b斗 ，中禾 c秉 實 d斗 ，下禾 e秉 實 f斗 。
"""

"""
Suppose there are three types of grain: upper grain (2 sheaves), middle grain (3 sheaves), and lower grain (4 sheaves). 
Each sheaf is not full to 1 dou. If the upper grain takes 1 sheaf from the middle grain, the middle grain takes 1 sheaf from the lower grain, 
and the lower grain takes 1 sheaf from the upper grain, then each becomes exactly 1 dou.

Question: How much does each sheaf of upper, middle, and lower grain contain?

Answer: Each sheaf of upper grain contains *a* sheaves and *b* dou, 
each sheaf of middle grain contains *c* sheaves and *d* dou, 
and each sheaf of lower grain contains *e* sheaves and *f* dou.
"""

from fractions import Fraction

# Let the amount of grain in one sheaf of upper, middle, and lower grain be x, y, and z respectively.
# Given:
# 2x + y = 1 (upper grain becomes 1 dou after taking 1 sheaf from middle grain)
# 3y + z = 1 (middle grain becomes 1 dou after taking 1 sheaf from lower grain)
# 4z + x = 1 (lower grain becomes 1 dou after taking 1 sheaf from upper grain)

# Solve the system of equations:
# From the first equation: y = 1 - 2x
# Substitute y into the second equation: 3(1 - 2x) + z = 1
# Simplify: 3 - 6x + z = 1 -> z = 6x - 2
# Substitute z into the third equation: 4(6x - 2) + x = 1
# Simplify: 24x - 8 + x = 1 -> 25x = 9 -> x = 9/25
x = Fraction(9, 25)

# Solve for y: y = 1 - 2x
y = 1 - 2 * x

# Solve for z: z = 6x - 2
z = 6 * x - 2

# Results:
a, b = 1, x  # Each sheaf of upper grain contains x dou
c, d = 1, y  # Each sheaf of middle grain contains y dou
e, f = 1, z  # Each sheaf of lower grain contains z dou

a, b, c, d, e, f
"""
"""

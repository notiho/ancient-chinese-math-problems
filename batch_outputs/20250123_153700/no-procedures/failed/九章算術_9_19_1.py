"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
荅曰： a步 。
"""

"""
Suppose there is a square city (a walled square area) of unknown size, with gates at the center of each side.
From the north gate, walking 20 bu north, there is a tree.
From the south gate, walking 14 bu south, then turning west and walking 1775 bu, the same tree is seen.
Question: what is the side length of the square city?

Answer: the side length of the square city is *a* bu.
"""

# Let the side length of the square city be `a` (in bu).

# From the problem, the north gate is at the center of the northern side of the square.
# The south gate is at the center of the southern side of the square.

# The total north-south distance from the north gate to the south gate is the side length of the square, `a`.
# The distance from the north gate to the tree is 20 bu.
# The distance from the south gate to the tree is 14 bu south + 1775 bu west.

# The north-south distance between the tree and the south gate is:
north_south_distance = 20 + 14  # 20 bu north + 14 bu south = 34 bu

# The westward distance from the south gate to the tree is given as 1775 bu.

# Using the Pythagorean theorem, the diagonal distance between the north gate and the south gate (which is the side length `a`) can be calculated:
# a^2 = (north_south_distance)^2 + (westward_distance)^2

from fractions import Fraction

# Calculate the side length `a`
north_south_distance = 34
westward_distance = 1775

a_squared = north_south_distance**2 + westward_distance**2
a = Fraction(a_squared).sqrt()

a
"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

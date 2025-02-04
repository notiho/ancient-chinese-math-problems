"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a square city (yi) of unknown size, with gates at the middle of each side.
From the north gate, walking 20 bu north leads to a tree.
From the south gate, walking 14 bu south and then turning west to walk 1775 bu also leads to the same tree.
Question: what is the side length of the square city?

Answer: the side length is *a* bu.
"""

# Let the side length of the city be `a` bu.

# From the problem:
# The distance from the north gate to the tree is 20 bu.
# The distance from the south gate to the tree is 14 bu south + 1775 bu west.

# The north gate and south gate are separated by the side length of the city (`a`).
# Therefore, the total vertical distance between the tree and the south gate is `a + 14`.

# Using the Pythagorean theorem:
# The horizontal distance (1775 bu west) and the vertical distance (`a + 14`) form a right triangle with the hypotenuse being the distance from the north gate to the tree (20 bu).

# Equation:
# (a + 14)^2 + 1775^2 = (a + 20)^2

from fractions import Fraction

# Expand the equation:
# (a + 14)^2 = a^2 + 28a + 196
# (a + 20)^2 = a^2 + 40a + 400
# Substituting into the equation:
# a^2 + 28a + 196 + 1775^2 = a^2 + 40a + 400

# Simplify:
# 28a + 196 + 1775^2 = 40a + 400
# 1775^2 = 3150625 (precomputed)
# 28a + 196 + 3150625 = 40a + 400
# 3150821 = 12a + 400
# 3150421 = 12a
# a = 3150421 / 12

# Solve for `a`:
a = Fraction(3150421, 12)

# The side length of the city is `a` bu.
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 250, Actual: 3150421/12"""

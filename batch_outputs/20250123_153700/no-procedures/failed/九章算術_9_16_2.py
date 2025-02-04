"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
荅曰： a步 。
"""

"""
Suppose there is a square city with sides of 200 bu. Each side has a gate in the middle.
From the east gate, walking 15 bu outward, there is a tree.
Question: how many bu must one walk outward from the south gate to see the tree?

Answer: *a* bu.
"""

# City side length
邑方 = 200

# Distance from the east gate to the tree
東門距木 = 15

# The east gate is at the middle of the east side, so its position is (200, 100) in a coordinate system.
# The tree's position is (200 + 15, 100).
木位置_x = 200 + 東門距木
木位置_y = 100

# The south gate is at the middle of the south side, so its position is (100, 0).
南門位置_x = 100
南門位置_y = 0

# Calculate the distance from the south gate to the tree using the Pythagorean theorem.
a = Fraction(((木位置_x - 南門位置_x) ** 2 + (木位置_y - 南門位置_y) ** 2) ** 0.5)

a
"""
Variable 'a' has wrong value. Expected: 2000/3, Actual: 670251321944833/4398046511104"""

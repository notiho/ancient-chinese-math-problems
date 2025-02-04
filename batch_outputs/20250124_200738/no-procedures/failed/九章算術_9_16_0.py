"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with each side 200 bu. Each side has a gate in the middle.
From the east gate, walking 15 bu outward, there is a tree.
Question: how many bu must one walk outward from the south gate to see the tree?

Answer: *a* bu.
"""

# Define the side length of the square city
side_length = 200

# The position of the tree relative to the east gate
tree_position_east = 15

# The east gate is in the middle of the east side
east_gate_position = side_length / 2

# The south gate is in the middle of the south side
south_gate_position = side_length / 2

# The distance from the south gate to the tree forms a right triangle
# Using the Pythagorean theorem:
# (distance_from_south_gate)^2 + (east_gate_position - tree_position_east)^2 = (south_gate_position)^2
a = Fraction((tree_position_east**2 + south_gate_position**2).sqrt())#----- content ends here -----

"""
Code error: 'float' object has no attribute 'sqrt'"""

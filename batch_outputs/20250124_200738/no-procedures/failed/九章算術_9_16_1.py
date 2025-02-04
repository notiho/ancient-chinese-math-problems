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

# The east gate and south gate are at the middle of their respective sides
gate_position = side_length / 2

# The tree is 15 bu east of the east gate
tree_position_x = gate_position + 15
tree_position_y = 0  # The tree is directly east, so its y-coordinate is 0

# From the south gate, calculate the distance to the tree
# The south gate is at (0, -gate_position)
south_gate_position_x = 0
south_gate_position_y = -gate_position

# Use the Pythagorean theorem to calculate the distance
a = Fraction((tree_position_x**2 + (tree_position_y - south_gate_position_y)**2)**0.5)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2000/3, Actual: 670251321944833/4398046511104"""

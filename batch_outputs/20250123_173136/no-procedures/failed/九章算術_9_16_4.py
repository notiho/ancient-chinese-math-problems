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

# Define the side length of the square city
side_length = 200

# The east gate is in the middle of the east side, so its position is (200, 100) in a coordinate system
east_gate_position = (200, 100)

# The tree is 15 bu east of the east gate, so its position is (200 + 15, 100)
tree_position = (200 + 15, 100)

# The south gate is in the middle of the south side, so its position is (100, 0)
south_gate_position = (100, 0)

# Calculate the distance from the south gate to the tree using the Pythagorean theorem
horizontal_distance = abs(tree_position[0] - south_gate_position[0])
vertical_distance = abs(tree_position[1] - south_gate_position[1])

# The total distance is the hypotenuse of the right triangle formed
a = Fraction((horizontal_distance**2 + vertical_distance**2)**0.5)

# Result
a
"""
Variable 'a' has wrong value. Expected: 2000/3, Actual: 670251321944833/4398046511104"""

"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
荅曰： a步 。
"""

"""
Suppose there is a square city (yi) of unknown size, with gates at the center of each side. 
From the north gate, walking 20 bu north reaches a tree. 
From the south gate, walking 14 bu south, then turning west and walking 1775 bu, also reaches the same tree.
Question: what is the side length of the square city?

Answer: the side length of the city is *a* bu.
"""

# Define known values
north_gate_to_tree = 20  # Distance from the north gate to the tree in bu
south_gate_to_tree = 14  # Distance from the south gate to the tree in bu
south_to_west_distance = 1775  # Distance walked west after leaving the south gate

# Let the side length of the square city be "a"
# The total north-south distance from the north gate to the south gate is the side length of the city (a).
# The distance from the north gate to the tree is equal to the distance from the south gate to the tree plus the side length of the city.

# Equation: north_gate_to_tree = south_gate_to_tree + a
# Solve for a
a = north_gate_to_tree + south_gate_to_tree

# The westward distance forms a right triangle with half the side length of the city and the total north-south distance.
# Using the Pythagorean theorem:
# (a / 2)^2 + south_to_west_distance^2 = (north_gate_to_tree + south_gate_to_tree)^2

from fractions import Fraction

# Solve for a
a = Fraction(2 * south_to_west_distance**2, north_gate_to_tree + south_gate_to_tree) ** 0
"""
Variable 'a' has wrong value. Expected: 250, Actual: 1"""

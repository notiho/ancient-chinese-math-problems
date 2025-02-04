"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a square city (yi) of unknown size, with gates in the middle of each side. 
From the north gate, walking 20 bu north leads to a tree. 
From the south gate, walking 14 bu south, then turning west and walking 1775 bu, also leads to the same tree. 
Question: what is the side length of the square city?

Answer: the side length is *a* bu.
"""

from fractions import Fraction

# Define the known values
north_distance_to_tree = 20  # Distance from the north gate to the tree
south_distance_to_tree = 14  # Distance from the south gate to the tree
west_distance_to_tree = 1775  # Distance west after leaving the south gate

# Let the side length of the square city be "a"
# The total north-south distance between the north gate and south gate is equal to the side length of the city.
# From the problem, we know:
# a = north_distance_to_tree + south_distance_to_tree + west_distance_to_tree

# Using the Pythagorean theorem:
# The westward distance (1775) forms the base of a right triangle, and the difference in distances to the tree (20 + 14 = 34) forms the height.
# The hypotenuse of this triangle is the side length of the square city (a).

# Solve for the side length of the city (a):
a_squared = (north_distance_to_tree + south_distance_to_tree) ** 2 + west_distance_to_tree ** 2
a = Fraction(a_squared).sqrt()

# Final result
a#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""

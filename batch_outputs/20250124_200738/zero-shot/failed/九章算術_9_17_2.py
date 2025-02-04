"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the number of steps from the south gate to the point where the tree becomes visible. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the city
east_west_distance = 7  # in li
north_south_distance = 9  # in li

# Conversion: 1 li = 1800 steps
li_to_steps = 1800

# Distance from the east gate to the tree
distance_to_tree_from_east_gate = 15 * li_to_steps  # in steps

# Steps from the east gate to the southeast corner
east_gate_to_southeast_corner = (north_south_distance / 2) * li_to_steps  # in steps

# Steps from the south gate to the southeast corner
south_gate_to_southeast_corner = (east_west_distance / 2) * li_to_steps  # in steps

# Calculate the number of steps from the south gate to the point where the tree is visible
a = Fraction(east_gate_to_southeast_corner * south_gate_to_southeast_corner, distance_to_tree_from_east_gate)

# Result
a  # in steps
#----- content ends here -----


"""


This code calculates the number of steps (`a`) from the south gate to the point where the tree becomes visible. The result is stored in the variable `a`.
"""


"""
Code error: both arguments should be Rational instances"""

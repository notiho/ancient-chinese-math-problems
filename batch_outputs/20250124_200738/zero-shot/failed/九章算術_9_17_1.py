"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
術曰：東門南至隅步數，以乘南門東至隅步數為實。以木去門步數為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the number of steps from the south gate to the point where the tree becomes visible. Here's the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
east_west_distance = 7  # in li
north_south_distance = 9  # in li
distance_to_tree_from_east_gate = 15  # in li

# Convert li to steps (1 li = 1800 steps)
east_west_steps = east_west_distance * 1800
north_south_steps = north_south_distance * 1800
distance_to_tree_steps = distance_to_tree_from_east_gate * 1800

# Calculate the steps from the south gate to the point where the tree is visible
a = Fraction(north_south_steps * east_west_steps, distance_to_tree_steps)

# Result
a  # in steps
#----- content ends here -----


"""


The variable `a` will contain the number of steps from the south gate to the point where the tree becomes visible.
"""


"""
Variable 'a' has wrong value. Expected: 315, Actual: 7560"""
